## rijndael.py - pure Python implementation of the Rijndael algorithm.
## Bjorn Edstrom <be@bjrn.se> 31 december 2007.
##
## Copyrights
## ==========
##
## This code is a derived from an implementation by Mike Scott which is
## subject to the following license. This Python implementation is not
## subject to any other license.
##
##/* Rijndael Cipher
##
##   Written by Mike Scott 21st April 1999
##   Copyright (c) 1999 Mike Scott
##   See rijndael documentation
##
##   Permission for free direct or derivative use is granted subject 
##   to compliance with any conditions that the originators of the 
##   algorithm place on its exploitation.  
##
##   Inspiration from Brian Gladman's implementation is acknowledged.
##
##   Written for clarity, rather than speed.
##   Full implementation. 
##   Endian indifferent.
##*/
##
## The above copyright notice must not be removed.
##
## Information
## ===========
##
## Anyone thinking of using this code should reconsider. It's slow.
## Try python-mcrypt instead. In case a faster library is not installed
## on the target system, this code can be used as a portable fallback.

import struct
try:
    import psyco
    psyco.full()
except ImportError:
    pass

#
# Settings.
#

BLOCK_SIZE = 16 # Rijndael-128
#BLOCK_SIZE = 24 # Rijndael-192
#BLOCK_SIZE = 32 # Rijndael-256

#
# Public.
#

block_size = BLOCK_SIZE
key_size = 32

class Rijndael:
    
    def __init__(self, key=None):
        self.ctx = RijndaelCTX()
        if key:
            self.set_key(key)
            
    def set_key(self, key):
        self.ctx = RijndaelCTX()
        setkey(self.ctx, key)
        
    def decrypt(self, data):
        dlen = len(data)
        if dlen % BLOCK_SIZE:
            raise ValueError, "data must be multiple of %d" % BLOCK_SIZE
        plain = ''
        for d in xrange(dlen / BLOCK_SIZE):
            plain += decrypt(self.ctx, data[0:BLOCK_SIZE])
            data = data[BLOCK_SIZE:]
        return plain
    
    def encrypt(self, data):
        dlen = len(data)
        if dlen % BLOCK_SIZE:
            raise ValueError, "data must be multiple of %d" % BLOCK_SIZE
        cipher = ''
        for d in xrange(dlen / BLOCK_SIZE):
            cipher += encrypt(self.ctx, data[0:BLOCK_SIZE])
            data = data[BLOCK_SIZE:]
        return cipher
    
    def get_name(self):
        if BLOCK_SIZE == 16:
            return "Rijndael"
        return "Rijndael-%d" % (BLOCK_SIZE * 8)
    
    def get_key_size(self):
        return 32
    
    def get_block_size(self):
        return BLOCK_SIZE

#
# Private.
#

class RijndaelCTX:
    def __init__(self):
        self.Nk = 0 # int
        self.Nb = 0 # int
        self.Nr = 0 # int
        self.fi = [0]*24 # byte
        self.ri = [0]*24 # byte
        self.fkey = [0]*120 # word32
        self.rkey = [0]*120 # word32
    def __repr__(self):
        ft = (self.Nk, self.Nb, self.Nr, repr(self.fi), \
              repr(self.ri), repr(self.fkey), repr(self.rkey))
        return "<RijndaelCTX Nk=%d Nb=%d Nr=%d fi=%s ri=%s fkey=%s rkey=%s>" % ft

def ROTL(x):
    return (x>>7) | ((x<<1)&0xff)
def ROTL8(x):
    return (x>>24) | ((x<<8)&0xffffffff)
def ROTL16(x):
    return (x>>16) | ((x<<16)&0xffffffff)
def ROTL24(x):
    return (x>>8) | ((x<<24)&0xffffffff)

InCo = [0xb, 0xd, 0x9, 0xe]

fbsub = [0]*256 # byte
rbsub = [0]*256 # byte
ptab = [0]*256 # byte
ltab = [0]*256 # byte
ftable = [0]*256 # word32
rtable = [0]*256 # word32
rco = [0]*30 # word32
tables_ok = 0

def pack(b):
    #b %= 0x100000000
    return (b[3]<<24) | (b[2]<<16) | (b[1]<<8) | b[0]
def unpack(a, b):
    a %= 0x100000000
    b[0] = a & 0xff
    b[1] = (a >> 8) & 0xff
    b[2] = (a >> 16) & 0xff
    b[3] = (a >> 24) & 0xff
    return b
def xtime(a):
    a %= 0x100
    b = 0
    if a & 0x80:
        b = 0x1b
    a <<= 1
    a &= 0xff
    a ^= b
    return a
def bmul(x, y):
    x %= 0x100
    y %= 0x100
    if x and y:
        return ptab[(ltab[x] + ltab[y]) % 255]
    return 0
def SubByte(a):
    a %= 0x100000000
    b = [0,0,0,0]
    unpack(a, b)
    b[0] = fbsub[b[0]]
    b[1] = fbsub[b[1]]
    b[2] = fbsub[b[2]]
    b[3] = fbsub[b[3]]
    return pack(b)
def product(x, y):
    x %= 0x100000000
    y %= 0x100000000
    xb = [0,0,0,0]
    yb = [0,0,0,0]
    unpack(x, xb)
    unpack(y, yb)
    return bmul(xb[0], yb[0]) ^ bmul(xb[1], yb[1]) ^ \
           bmul(xb[2], yb[2]) ^ bmul(xb[3], yb[3])
def InvMixCol(x):
    x %= 0x100000000
    y, m = 0, 0
    b = [0,0,0,0]
    m = pack(InCo);
    b[3] = product(m, x);
    m = ROTL24(m);
    b[2] = product(m, x);
    m = ROTL24(m);
    b[1] = product(m, x);
    m = ROTL24(m);
    b[0] = product(m, x);
    y = pack(b);
    return y % 0x100000000;
def ByteSub(x):
    x %= 0x100
    y = ptab[255 - ltab[x]];
    x = y;
    x = ROTL(x);
    y ^= x;
    x = ROTL(x);
    y ^= x;
    x = ROTL(x);
    y ^= x;
    x = ROTL(x);
    y ^= x;
    y ^= 0x63;
    return y % 0x100;    

def gentables():
    i = 0
    y = 0
    b = [0,0,0,0]
    ltab[0] = 0
    ptab[0] = 1
    ltab[1] = 0
    ptab[1] = 3
    ltab[3] = 1
    for i in xrange(2, 256):
        ptab[i] = ptab[i - 1] ^ xtime(ptab[i - 1])
        ltab[ptab[i]] = i
    fbsub[0] = 0x63
    rbsub[0x63] = 0
    for i in xrange(1, 256):
        y = ByteSub(i % 0x100)
        fbsub[i] = y
        rbsub[y] = i
    y = 1
    for i in xrange(30):
        rco[i] = y
        y = xtime(y)
    for i in xrange(256):
        y = fbsub[i]
        b[3] = y ^ xtime(y)
        b[2] = y
        b[1] = y
        b[0] = xtime(y)
        ftable[i] = pack(b)
        y = rbsub[i]
        b[3] = bmul(InCo[0], y)
        b[2] = bmul(InCo[1], y)
        b[1] = bmul(InCo[2], y)
        b[0] = bmul(InCo[3], y)        
        rtable[i] = pack(b)
    pass

gentables()


#def setkey(rinst, key, nk):
def setkey(rinst, key):
    key = [ord(k) for k in key]
    keylen = len(key)
    assert keylen in [32, 24, 16]
    #nk = (keylen*8)/32
    nk = keylen
    #nb = 8
    nb = 0
    if BLOCK_SIZE == 16:
        nb = 4
    elif BLOCK_SIZE == 24:
        nb = 6
    elif BLOCK_SIZE == 32:
        nb = 8
    CipherKey = [0]*8
    nk /= 4
    if BLOCK_SIZE == 16 and nk < 4:
        nk = 4
    rinst.Nb = nb
    rinst.Nk = nk
    if rinst.Nb >= rinst.Nk:
        rinst.Nr = 6 + rinst.Nb
    else:
        rinst.Nr = 6 + rinst.Nk
    C1, C2, C3 = 1, 0, 0
    if rinst.Nb < 8:
        C2 = 2
        C3 = 3
    else:
        C2 = 3
        C3 = 4
    m = 0
    for j in xrange(nb):
        rinst.fi[m] = (j + C1) % nb
        rinst.fi[m + 1] = (j + C2) % nb
        rinst.fi[m + 2] = (j + C3) % nb
        rinst.ri[m] = (nb + j - C1) % nb
        rinst.ri[m + 1] = (nb + j - C2) % nb
        rinst.ri[m + 2] = (nb + j - C3) % nb          
        m += 3
    N = rinst.Nb * (rinst.Nr + 1)
    j = 0
    for i in xrange(rinst.Nk):
        CipherKey[i] = pack(key[j:j+4]) # XXX
        j += 4
    for i in xrange(rinst.Nk):
        rinst.fkey[i] = CipherKey[i]
    k = 0
    for j in xrange(rinst.Nk, N, rinst.Nk):
        rinst.fkey[j] = rinst.fkey[j - rinst.Nk] ^ SubByte(ROTL24(rinst.fkey[j - 1])) ^ rco[k]
        if rinst.Nk <= 6:
            i = 1
            while i < rinst.Nk and (i + j) < N:
                rinst.fkey[i + j] = rinst.fkey[i + j - rinst.Nk] ^ rinst.fkey[i + j - 1]
                i += 1
        else:
            i = 1
            while i < 4 and (i + j) < N:
                rinst.fkey[i + j] = rinst.fkey[i + j - rinst.Nk] ^ rinst.fkey[i + j - 1]
                i += 1
            if (j + 4) < N:
                rinst.fkey[j + 4] = rinst.fkey[j + 4 - rinst.Nk] ^ SubByte(rinst.fkey[j + 3])
            i = 5
            while i < rinst.Nk and (i + j) < N:
                rinst.fkey[i + j] = rinst.fkey[i + j - rinst.Nk] ^ rinst.fkey[i + j - 1]
                i += 1
        k += 1
    for j in xrange(rinst.Nb):
        rinst.rkey[j + N - rinst.Nb] = rinst.fkey[j]
    for i in xrange(rinst.Nb, N - rinst.Nb, rinst.Nb):
        k = N - rinst.Nb - i
        for j in xrange(rinst.Nb):
            rinst.rkey[k + j] = InvMixCol(rinst.fkey[i + j])
    for j in xrange(N - rinst.Nb, N):
        rinst.rkey[j - N + rinst.Nb] = rinst.fkey[j]
    return

def encrypt(rinst, buff):
    buff = [ord(b) for b in buff]
    a = [0]*8
    b = [0]*8
    j = 0
    for i in xrange(rinst.Nb):
        a[i] = pack(buff[j:j+4])
        a[i] ^= rinst.fkey[i]
        j += 4
    k = rinst.Nb
    x = a
    y = b
    for i in xrange(1, rinst.Nr):
        m = 0
        for j in xrange(rinst.Nb):
            y[j] = rinst.fkey[k] ^ ftable[x[j]%0x100] ^ \
                   ROTL8(ftable[(x[rinst.fi[m+0]]>>8)%0x100]) ^ \
                   ROTL16(ftable[(x[rinst.fi[m+1]]>>16)%0x100]) ^ \
                   ROTL24(ftable[(x[rinst.fi[m+2]]>>24)%0x100])
            k += 1
            m += 3
        x, y = y, x
    m = 0
    for j in xrange(rinst.Nb):
        y[j] = rinst.fkey[k] ^ fbsub[x[j]%0x100] ^ \
               ROTL8(fbsub[(x[rinst.fi[m+0]]>>8)%0x100]) ^ \
               ROTL16(fbsub[(x[rinst.fi[m+1]]>>16)%0x100]) ^ \
               ROTL24(fbsub[(x[rinst.fi[m+2]]>>24)%0x100])
        k += 1
        m += 3
    j = 0
    for i in xrange(rinst.Nb):
        buff[j:j+4] = unpack(y[i], buff[j:j+4])[:]
        x[i] = y[i] = 0
        j += 4
    return ''.join([chr(b) for b in buff])


def decrypt(rinst, buff):
    buff = [ord(b) for b in buff]
    a = [0]*8
    b = [0]*8
    j = 0
    for i in xrange(rinst.Nb):
        a[i] = pack(buff[j:j+4])
        a[i] ^= rinst.rkey[i]
        j += 4
    k = rinst.Nb
    x = a
    y = b
    for i in xrange(1, rinst.Nr):
        m = 0
        for j in xrange(rinst.Nb):
            y[j] = rinst.rkey[k] ^ rtable[x[j]%0x100] ^ \
                   ROTL8(rtable[(x[rinst.ri[m+0]]>>8)%0x100]) ^ \
                   ROTL16(rtable[(x[rinst.ri[m+1]]>>16)%0x100]) ^ \
                   ROTL24(rtable[(x[rinst.ri[m+2]]>>24)%0x100])
            k += 1
            m += 3
        x, y = y, x
    m = 0
    for j in xrange(rinst.Nb):
        y[j] = rinst.rkey[k] ^ rbsub[x[j]%0x100] ^ \
               ROTL8(rbsub[(x[rinst.ri[m+0]]>>8)%0x100]) ^ \
               ROTL16(rbsub[(x[rinst.ri[m+1]]>>16)%0x100]) ^ \
               ROTL24(rbsub[(x[rinst.ri[m+2]]>>24)%0x100])
        k += 1
        m += 3
    j = 0
    for i in xrange(rinst.Nb):
        buff[j:j+4] = unpack(y[i], buff[j:j+4])[:]
        x[i] = y[i] = 0
        j += 4
    return ''.join([chr(b) for b in buff])
    
#
# Tests.
#

if BLOCK_SIZE == 16:
    assert Rijndael('012345678abcdefgh00112233xyzqwer').encrypt('a'*16) == '%\x98\x8a \xf8\\\x10\x9c\x17\x16\x9bb\x9e\xd6*\x96'
    assert Rijndael('012345678abcdefgh00112233xyzqwer').decrypt('%\x98\x8a \xf8\\\x10\x9c\x17\x16\x9bb\x9e\xd6*\x96') == 'a'*16
    assert Rijndael('\x10'*32).encrypt('1234'*4) == '\xba\xad\xaawV|S\xc36>1\x03\xfd\x9e+\x9d'

##import Crypto.Cipher.AES
##
##class Rijndael:
##    def __init__(self, key=None):
##        if key:
##            self.aes = Crypto.Cipher.AES.new(key)
##    def set_key(self, key):
##        self.aes = Crypto.Cipher.AES.new(key)
##    def decrypt(self, data):
##        return self.aes.decrypt(data)
##    def encrypt(self, data):
##        return self.aes.encrypt(data)
##    def get_name(self):
##        return "Rijndael"
##    def get_key_size(self):
##        return 32
##    def get_block_size(self):
##        return 16
