## truecrypt.py - partial TrueCrypt implementation in Python.
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

import struct
try:
    import psyco
    psyco.full()
except ImportError:
    pass

import sys
import os

from rijndael import Rijndael
from lrw import *
from keystrengthening import *

#
# Utilities.
#

import struct
import time
import binascii

def Log(message):
    print >> sys.stderr, "Progress:", message

def CRC32(data):
    """Compute CRC-32."""
    crc = binascii.crc32(data)
    # Convert from signed to unsigned word32.
    return crc % 0x100000000

def BE16(x):
    """Bytes to 16 bit big endian word."""
    return struct.unpack(">H", x)[0]

def BE32(x):
    """Bytes to 32 bit big endian word."""
    return struct.unpack(">L", x)[0]

def BE64(x):
    """Bytes to 64 bit big endian word."""
    a, b = struct.unpack(">LL", x)
    return (a<<32) | b

def Win32FileTime2UnixTime(filetime):
    """Converts a win32 FILETIME to a unix timestamp."""
    return filetime / 10000000 - 11644473600

#
# Ciphers.
#

class CipherChain:
    def __init__(self, ciphers):
        self.ciphers = [ciph() for ciph in ciphers]
    def set_key(self, keys):
        i = 0
        for cipher in self.ciphers:
            cipher.set_key(keys[i])
            i += 1
    def encrypt(self, data):
        for cipher in self.ciphers:
            data = cipher.encrypt(data)
        return data
    def decrypt(self, data):
        for cipher in reversed(self.ciphers):
            data = cipher.decrypt(data)
        return data
    def get_name(self):
        return '-'.join(reversed([cipher.get_name() for cipher in self.ciphers]))

Cascades = [
    [Rijndael],
]

HMACs = [
    (HMAC_RIPEMD160, "RIPEMD-160"),
]

#
# TrueCrypt.
#

TC_SECTOR_SIZE = 512
TC_HIDDEN_VOLUME_OFFSET = 1536

class TrueCryptVolume:
    """Object representing a TrueCrypt volume."""
    def __init__(self, fileobj, password, progresscallback=lambda x: None):

        self.fileobj = fileobj
        self.decrypted_header = None
        self.cipher = None
        self.master_lrwkew = None
        self.hidden_size = 0

        for volume_type in ["normal", "hidden"]:
            fileobj.seek(0)
            if volume_type == "hidden":
                fileobj.seek(-TC_HIDDEN_VOLUME_OFFSET, 2)

            progresscallback("Is this a " + volume_type + " volume?")
            
            salt = fileobj.read(64)
            header = fileobj.read(448)
            
            assert len(salt) == 64
            assert len(header) == 448

            for hmac, hmac_name in HMACs:
                # Generate the keys needed to decrypt the volume header.
                iterations = 2000

                info = ''
                if hmac_name == "RIPEMD-160":
                    info = ' (this will take a while)'
                progresscallback("Trying " + hmac_name + info)
                
                for cascade in Cascades:
                    # Try each cipher and cascades and see if we can successfully
                    # decrypt the header with it.
                    cipher = CipherChain(cascade)
                    
                    progresscallback("..." + cipher.get_name())
                    
		    print("Using a hijacked lrw & master keys as stolen from memory")

		    # Example keys from Update Partition
                    master_lrwkey = '\x96M\xc5\x8e\xc1\xdb\xf4\x01@\xa9F\xabDD\x95g'
		    print repr(master_lrwkey)
                    master_key1 = '\xd5\x1fc\x95\x11\xf7\xb8\x1b!\x12r%\x97Z\xb7^\x14af#\xb7\x13/6\xbe.\xfd\xf4\xb0x\r\t'
		    print repr(master_key1)
                    master_key2 = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
		    print repr(master_key2)
                    master_key3 = '\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
		    print repr(master_key3)

                    self.master_lrwkey = master_lrwkey
                    self.cipher = cipher
                    self.cipher.set_key([master_key1, master_key2, master_key3])
                    self.hidden_size = 429916160
                    self.format_ver = 0x2

                    # We don't really need the information below but we save
                    # it so it can be displayed by print_information()
                    self.info_hash = hmac_name

                    progresscallback("Success!")
                    return
        # Failed attempt.
        raise KeyError, "incorrect password (or not a truecrypt volume)"

    def __repr__(self):
        if not self.decrypted_header:
            return "<TrueCryptVolume>"
        return "<TrueCryptVolume %s %s>" % (self.cipher.get_name(), self.info_hash)

def TCReadSector(tc, index):
    """Read a sector from the volume."""
    assert index > 0
    tc.fileobj.seek(0, 2)
    file_len = tc.fileobj.tell()

    # The LRW functions work on blocks of length 16. Since a TrueCrypt
    # sector is 512 bytes each call to LRWMany will decrypt 32 blocks,
    # and each call to this function must therefore advance the block
    # index 32. The block index also starts at 1, not 0. index 1
    # corresponds to lrw_index 1, index 2 corresponds to lrw_index 33 etc.
    lrw_index = (index - 1) * 32 + 1 # LRWSector2Index(index)

    # For a regular (non-hidden) volume the file system starts at byte
    # 512. However for a hidden volume, the start of the file system
    # is not at byte 512. Starting from the end of the volume, namely
    # byte file_len, we subtract the hidden volume salt+header (at offset
    # 1536 from the end of the file). We then subtract the size of the
    # hidden volume.
    mod = 0
    last_sector_offset = TC_SECTOR_SIZE
    if tc.hidden_size:
        mod = file_len - tc.hidden_size - TC_HIDDEN_VOLUME_OFFSET
        # We subtract another sector from mod because the index starts
        # at 1 and not 0.
        mod -= TC_SECTOR_SIZE
        last_sector_offset = TC_SECTOR_SIZE + TC_HIDDEN_VOLUME_OFFSET
    seekto = mod + TC_SECTOR_SIZE * index

    # last_sector_offset is the beginning of the last sector relative
    # the end of the file. For a regular non-hidden volume this is simply
    # 512 bytes from the end of the file. However for hidden volumes we
    # must not read past the headers, so the last sector begins 512 bytes
    # before the header offset.
    if seekto > file_len - last_sector_offset:
        return ''

    tc.fileobj.seek(seekto)
    data = tc.fileobj.read(TC_SECTOR_SIZE)
    
    return LRWMany(tc.cipher.decrypt, tc.master_lrwkey, lrw_index, data)          

def TCSectorCount(tc):
    """How many sectors can we read with TCReadSector?"""

    volume_size = 0
    if tc.hidden_size:
        volume_size = tc.hidden_size
    else:
        tc.fileobj.seek(0, 2)
        volume_size = tc.fileobj.tell()
        # Minus the salt+header.
        volume_size -= 512
    return volume_size / TC_SECTOR_SIZE

def TCPrintInformation(tc):
    if not tc.decrypted_header:
        return

    header = tc.decrypted_header
    program_ver = BE16(header[6:8])
    volume_create = Win32FileTime2UnixTime(BE64(header[12:12+8]))
    header_create = Win32FileTime2UnixTime(BE64(header[20:20+8]))

    print "="*60
    print "Raw Header"
    print "="*60
    print repr(tc.decrypted_header)
    print "="*60
    print "Parsed Header"
    print "="*60    
    print "Hash          :", tc.info_hash
    print "Cipher        :", tc.cipher.get_name()
    if tc.hidden_size:
        print "Volume Type   : Hidden"
        print "Hidden size   :", tc.hidden_size
    else:
        print "Volume Type   : Normal"
    print "Format ver    :", hex(tc.format_ver)
    print "Min prog. ver :", hex(program_ver)
    print "Volume create :", time.localtime(volume_create)
    print "Header create :", time.localtime(header_create)
    print "="*60
    #sys.exit(0)
def cmdline():
    scriptname = sys.argv[0]
    try:
        path, outfile = sys.argv[1:]
    except ValueError:
        print >> sys.stderr, "%s volumepath password outfile" % scriptname
        sys.exit(1)

    if os.path.exists(outfile):
        print >> sys.stderr, "outfile %s already exists. use another " \
              "filename and try again (we don't want to overwrite " \
              "files by mistake)" % outfile
        sys.exit(1)

    try:
        fileobj = file(path, "rb")
    except IOError:
        print >> sys.stderr, "file %s doesn't exist" % path
        sys.exit(1)

    try:
        tc = TrueCryptVolume(fileobj, Log)
    except KeyError:
        print >> sys.stderr, "incorrect password or not a TrueCrypt volume"
        fileobj.close()
        sys.exit(1)
    except KeyboardInterrupt:
        print >> sys.stderr, "aborting"
        fileobj.close()
        sys.exit(1)

    TCPrintInformation(tc)

    outfileobj = file(outfile, "ab")
    num_sectors = TCSectorCount(tc)
    num_written = 0
    try:
        for i in xrange(1, num_sectors + 1):
            if i % 100 == 0:
                Log("Decrypting sector %d of %d." % (i, num_sectors))
            outfileobj.write(TCReadSector(tc, i))
            num_written += 1
    except KeyboardInterrupt:
        print "Aborted decryption."
        pass
    outfileobj.close()
    print "Wrote %d sectors (%d bytes)." % (num_written,
                                            num_written * TC_SECTOR_SIZE)
    fileobj.close()
    sys.exit(0)

if __name__ == '__main__':
    cmdline()

## If you want to use the code from the toploop:
##
#fileobj = file("volume.tc", "rb")
#tc = TrueCryptVolume(fileobj, "password", Log)
#TCPrintInformation(tc)
#print repr(TCReadSector(tc, 1))
#print repr(TCReadSector(tc, 2))
