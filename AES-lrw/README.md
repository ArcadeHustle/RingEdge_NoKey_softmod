### Base Concept 

The code in this subfolder is borrowed from this paper: http://blog.bjrn.se/2008/01/truecrypt-explained.html
All unnecessary functions / code were removed for crypto options that don't apply to Sega's usage of TC4.3a

Next the code was modified to support keyfiles with a routine from pytruecrypt: https://github.com/4144414D/pytruecrypt

Now the code accepts one additional arguement pointing to a KeyFile. 
$ python truecrypt.py ~/Desktop/System_OperationGhost segahardpassword ~/Desktop/SystemKeyFile SegaBoot.img

The key file can be anything in practice, only the first 1024 bytes are read.  KeyFilesApply() in TrueCryptSource/Common/Keyfiles.c handles actually processing the key file and altering the password. 

A CRC32 function is run across the key file(s) and a Key pool is created from any available key files. Next the pool gets used as part of the "Mix" of crcd key file contents and password bytes.  

The password is used up to KeyPool length, at wich point keypool bytes are substituted. 

If we run 'segahardpassword' through this mixing routine alongside the system key file we get the following output. 

$ python KeyFileMixedPassGen.py | xxd 
00000000: 151f 2c56 88d1 8bcd 3333 4e1b 6247 839a  ..,V....33N.bG..
00000010: 3990 8f2f 35bc 76b6 2939 9208 8de5 e176  9../5.v.)9.....v
00000020: 3fae 0364 0999 0151 84ba f711 af55 e84b  ?..d...Q.....U.K
00000030: 61e0 f9c7 5d35 1683 8931 fa58 7dd9 beed  a...]5...1.X}...
00000040: 0a

A variant of the code has been created that does not need a keyfile, or a password, rather it can make use of a previosuly decrypted header file. 
$ python truecrypt_UseMasterKeys.py UpdatePartition UpdatePartition.img

This is the pre-cursor to using an extracted master key from memory . 


### AES LRW Key Recovery

There are techniques to recover LRW and Tweak keys from memory... 
https://www.usenix.org/legacy/event/sec08/tech/full_papers/halderman/halderman_html/index.html

In order to speed tweak computations, implementations commonly precompute multiplication tables of the values K2 xi mod P, where x is the primitive element and P is an irreducible polynomial over GF(2128) [26]. In practice, Q x mod P is computed by shifting the bits of Q left by one and possibly XORing with P.
Given a value K2 xi, we can recover nearly all of the bits of K2 simply by shifting right by i. The number of bits lost depends on i and the nonzero elements of P. An entire multiplication table will contain many copies of nearly all of the bits of K2, allowing us to reconstruct the key in much the same way as the DES key schedule.
As an example, we apply this method to reconstruct the LRW key used by the TrueCrypt 4 disk encryption system. TrueCrypt 4 precomputes a 4048-byte multiplication table consisting of 16 blocks of 16 lines of 4 words of 4 bytes each. Line 0 of block 14 contains the tweak key.
The multiplication table is generated line by line from the LRW key by iteratively applying the shift-and-XOR multiply function to generate four new values, and then XORing all combinations of these four values to create 16 more lines of the table. The shift-and-XOR operation is performed 64 times to generate the table, using the irreducible polynomial P = x128+x7+x2+x+1. For any of these 64 values, we can shift right i times to recover 128 − (8+i) of the bits of K2, and use these recovered values to reconstruct K2 with high probability.
generate the first table as it has no shifting (from which we make the other tables)
https://android.googlesource.com/platform/external/dropbear/+/refs/heads/donut-release/libtomcrypt/src/modes/lrw/lrw_start.c

### Memory pool tags

Next we will attempt to find the above AES artifacts in keyed memory pool tables. 
https://tribalchicken.net/recovering-bitlocker-keys-on-windows-8-1-and-10/


