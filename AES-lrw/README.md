$ python truecrypt.py System_LetsGoJungle segahardpassword SegaBoot.img

http://blog.bjrn.se/2008/01/truecrypt-explained.html

https://www.usenix.org/legacy/event/sec08/tech/full_papers/halderman/halderman_html/index.html

In order to speed tweak computations, implementations commonly precompute multiplication tables of the values K2 xi mod P, where x is the primitive element and P is an irreducible polynomial over GF(2128) [26]. In practice, Q x mod P is computed by shifting the bits of Q left by one and possibly XORing with P.

Given a value K2 xi, we can recover nearly all of the bits of K2 simply by shifting right by i. The number of bits lost depends on i and the nonzero elements of P. An entire multiplication table will contain many copies of nearly all of the bits of K2, allowing us to reconstruct the key in much the same way as the DES key schedule.

As an example, we apply this method to reconstruct the LRW key used by the TrueCrypt 4 disk encryption system. TrueCrypt 4 precomputes a 4048-byte multiplication table consisting of 16 blocks of 16 lines of 4 words of 4 bytes each. Line 0 of block 14 contains the tweak key.

The multiplication table is generated line by line from the LRW key by iteratively applying the shift-and-XOR multiply function to generate four new values, and then XORing all combinations of these four values to create 16 more lines of the table. The shift-and-XOR operation is performed 64 times to generate the table, using the irreducible polynomial P = x128+x7+x2+x+1. For any of these 64 values, we can shift right i times to recover 128 − (8+i) of the bits of K2, and use these recovered values to reconstruct K2 with high probability.


generate the first table as it has no shifting (from which we make the other tables)
https://android.googlesource.com/platform/external/dropbear/+/refs/heads/donut-release/libtomcrypt/src/modes/lrw/lrw_start.c

