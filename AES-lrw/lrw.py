## lrw.py - The LRW cryptographic mode.
## Copyright (c) 2008 Bjorn Edstrom <be@bjrn.se>
##
## Permission is hereby granted, free of charge, to any person
## obtaining a copy of this software and associated documentation
## files (the "Software"), to deal in the Software without
## restriction, including without limitation the rights to use,
## copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the
## Software is furnished to do so, subject to the following
## conditions:
##
## The above copyright notice and this permission notice shall be
## included in all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
## EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
## OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
## NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
## HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
## WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
## OTHER DEALINGS IN THE SOFTWARE.
## --
## Changelog
## Jan 4 2008: Initial version. Plenty of room for improvements.

try:
    import psyco
    psyco.full()
except ImportError:
    pass

from gf2n import *

# C_i = E_K1(P_i ^ (K2 x i)) ^ (K2 x i).
# Note that cipherfunc = E_K1, that is the key should already be set in E.
# lrwkey = K2.
def LRW(cipherfunc, lrwkey, i, block):
    """Perform a LRW operation."""

    def str2int(str):
        N = 0
        for c in str:
            N <<= 8
            N |= ord(c)
        return N

    def int2str(N):
        str = ''
        while N:
            str = chr(N & 0xff) + str
            N >>= 8
        return str

    def xorstring16(a, b):
        new = ''
        for p in xrange(16):
            new += chr(ord(a[p]) ^ ord(b[p]))
        return new

    assert len(block) == 16
    assert len(lrwkey) == 16
    K2 = str2int(lrwkey)
    # C_i = E_K1(P_i ^ K2i) ^ K2i
    K2i = int2str(gf2pow128mul(K2, i))
    K2i = '\x00' * (16 - len(K2i)) + K2i
    return xorstring16(K2i, cipherfunc(xorstring16(K2i, block)))

def LRWMany(cipherfunc, lrwkey, i, blocks):
    length = len(blocks)
    assert length % 16 == 0
    data = ''
    for b in xrange(length / 16):
        data += LRW(cipherfunc, lrwkey, i + b, blocks[0:16])
        blocks = blocks[16:]
    return data
