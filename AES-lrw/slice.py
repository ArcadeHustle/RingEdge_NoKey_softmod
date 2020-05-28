import sys
import binascii 
import truecrypt_BruteMasterKeys

# Seek location, read one byte, apply 64 byte slice template. 

import mmap

path = "/Users/kfinisterre/Desktop/System_NikoMulti" 

try:
	fileobj = file(path, "rb")
except IOError:
	print >> sys.stderr, "file %s doesn't exist" % path
	sys.exit(1)

with open(sys.argv[1], "r+") as f:
	# memory-map the file, size 0 means whole file
	map = mmap.mmap(f.fileno(), 0)

	filesize = map.size()
	print("Filesize is: " + str(filesize))
	pos = 0
        chunk = 1 # Move the window one byte at a time. 
	while pos < filesize-chunk:
		pos = pos+chunk

		window = map.read(64)  
		lrwkey = window[0:16]

		if len(lrwkey) <16:
			print("no more data left to make keys!")
			sys.exit(0)

		fourwords = window[16:32]  
		if len(fourwords) <16:
			print("no more data left to make keys!")
			sys.exit(0)
		aeskey = window[32:64]  
		if len(aeskey) <32:
			print("no more data left to make keys!")
			sys.exit(0)

#		print(binascii.hexlify(lrwkey))
#		print(binascii.hexlify(aeskey))

		map.seek(pos)

		try:
			tc = truecrypt_BruteMasterKeys.TrueCryptVolume(fileobj, lrwkey, aeskey)
			truecrypt_BruteMasterKeys.TCPrintInformation(tc)

		except KeyError:
			print >> sys.stderr, "incorrect password or not a TrueCrypt volume"
			fileobj.close()
		except KeyboardInterrupt:
			print >> sys.stderr, "aborting"
			fileobj.close()
			sys.exit(1)
	
map.close()

