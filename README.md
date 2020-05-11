*PRE-RELEASE DO NOT SHARE THIS MESS*

Big thanks to Mitsurugi_w, Darksoft, and Brizzo of Arcade Projects for finally allowing this to be published.
- written by hostile, with supporting information from the community at large!

<p align="center">
<img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/walsdawg.jpeg"><img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/darksoft.jpeg">
</p>

<p align="center">
  <img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/arcadeprojects.jpeg"><img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/brizzo.jpeg">
</p>

* [Stage One: Bye Bye Puyo Puyo!](#stage-one)
* [Stage Two: Early Ring history](#stage-two)
* [Stage Three: Ring Piracy Deep Dive](#stage-three)
	* [Enter TrueCrypt](#enter-truecrypt)
	* [The Chinese Jinwin Sega connection?](#the-chinese-jinwin-sega-connection)
* [Stage Four: Academic Exercises & Censorship](#stage-four)
	* [Unlocking the drive](#unlocking-the-drive)
	* [Modifying the OS boot image](#modifying-the-os-boot-image)
	* [Mounting TrueCrypt containers](#mounting-truecrypt-containers)
	* [Obtaining the KeyFile and Volume Password](#obtaining-the-keyfile-and-volume-password)
	* [Playing around with Volatility](#playing-around-with-volatility)
* [Final Boss: Changing games on Niko's Multi](#final-boss)
* [Bonus Level: RE2Multi on RE1?1](#bonus-level)

# Stage One:

"【お知らせ】サービスを終了いたしました。"<br>
As of Friday, March 31, 2017 at 27:59 The service has ended for “Puyo Puyo !! Quest Arcade”<br>
http://puyoquest-am.blog.jp/archives/1063562161.html<br>
https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text=http%3A%2F%2Fpuyoquest-am.blog.jp%2Farchives%2F1063562161.html<br>

<p align="center">
  <img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/puyo.jpeg">
</p>

Christmas 2018 of course, brought this game back to life via the amazing "TeknoParrot 1.81 X-Mas Reveal".<br>
Unfortunately this restoration was only for PC users as opposed to arcade operators. <br>
https://archive.org/download/Arcade-Sega-RingEdge-2018-12-23

"Sorry guy, didn't see you there!"<br>
[![Sorry Guy](http://img.youtube.com/vi/-ds4xRnI-b8/0.jpg)](https://www.youtube.com/watch?v=-ds4xRnI-b8?t=190 )<br>
"Now it is time to take out my Santa bag, and give you presents"

What about *actual* Ring hardware owners, and arcade operators in need? Have we been left out of the most recent TeknoParrot CoronaVirus (COVID-19) Update just the same? Are there no presents for us? 

[![Hello my friends](http://img.youtube.com/vi/lS3gSW3ZskQ/0.jpg)](https://www.youtube.com/watch?v=lS3gSW3ZskQ)<br>
"Hello my friends, it seems that we are in the middle of a cross road, and now I have decided that I will enable all the RingEdge, RindEdge2, and RingWide cores on Teknoparrot, directly to public. Also if the entire internet dies because of coronavirus, I have given the archive and the source code to a few friends, expect an update. Good luck everybody."

Meanwhile, on the *other* side of the interwebs:<br>
"We set out rules and people couldn't follow them. This new stuff is bringing too much drama."<br>
https://www.arcade-projects.com/forums/index.php?thread/12974-ringedge-help-section/&postID=210050#post210050

Lets all pour out some liquor for the Sega Ringedge, Ringwide and Nu subgroup on AP. Rest In Peace!<br>
[![liquor pour](http://img.youtube.com/vi/oK9gLkXe0xw/0.jpg)](https://www.youtube.com/watch?v=oK9gLkXe0xw)<br>
https://web.archive.org/web/20171014003744/http://www.arcade-projects.com/forums/index.php?board/73-sega-ringedge-ringwide-and-nu/

Additional text relevant to this document can be found below: 

Exemptions to Prohibition against Circumvention of Technological Measures Protecting Copyrighted Works<br>
Seventh Triennial Section 1201 Final Rule, Effective October 28, 2018 <br>
https://library.osu.edu/document-registry/docs/1027/stream<br>
"Video games in the form of computer programs, where outside server support has been discontinued, to allow individual play and preservation by an eligible library, archive, or museum"

https://library.osu.edu/site/copyright/2019/03/20/2018-dmca-section-1201-exemptions-announced/ <br>
"Video games in the form of computer programs, lawfully acquired as complete games 37"<br> 
"CFR §201.40(b)(12)"<br> 
"For personal, local gameplay; or To allow preservation in a playable format..."<br>

Please note that the following text is considered "for purposes of good-faith security research". This write up will give you all the knowledge, and access you need to backup and preserve your RingEdge hardware featuring Puyo Puyo !! Quest Arcade. This preservation may also apply to other devices, and games in the Ring* family such as RingEdge2, and RingWide. 

Please remember the wise words of Mitsurugi_w "The info itself is not new or special. It's all over the web anyways" 

# Stage Two:

For a long time the details of how Ring* game images are ReKeyed, or NoKeyed has been a closely guarded, and heavily traded / paid for secret. With the first decade of deployment coming to a close, it is also time to close off this "Internet Money Maker". None the less, as hardware begins to fail, the threat of required preservation looms. 

One of the earlier forum disucssions on the Ring* subject was founded on Assembler games. Several known scene players can be seen waving their dicks around: "Get system, then come talk. This is why this information is not public because people who have no knowledge come to public and act like experts with no stripes."
https://web.archive.org/web/20170630214524/https://assemblergames.com/threads/sega-ringedge-motherboard-inside-pictures.46424/page-3

The initial manifesto that Jackalus laid down is actually a great place to start... 
```
"Still you don't have the system, for example newer ring games have custom protector that works with the rootkits 
and only runs when everything is in order and only on original machine. You cannot attach debugger, most debuggers 
can't even see the process because of ring0 stuff, you cannot dump the process without ring0 methods and even then 
not easily, you cannot press alt+tab or use any key combination keys (Unless you know how to go around them). The 
windows protection is very complicated and strong, you are still just speculating here. It's not some jumps you 
patch to skip the dongle check. And it's not as simple as Taito Type X2 which was mostly a joke."
```

The subsequent rant about his work as a Jr Malware Researcher for F-Secure (https://www.linkedin.com/in/giansanti/) was seemingly unrelated, but will be included anyway on the offhand event you need to measure his e-peen: "I have unpacked hundreds of custom malware packers, Commercial protections: Securom (Yes with VM Redirects, Opcode VM, Constant Hook Stealer etc), SafeDisk(+Nanomites), ASProtect SKE(+VM) blablabla. And when I tell you newer sega games have good protection, it really does have it. Sure you can clone it but emulation and running on PC is pretty much impossible without deprotecting the binary and emulating entire MX drivers/libraries."

Immediately after said rant, reaver implied that running Ring games on PC was less than favorable anyway, implying that the discussion was pointless.<br>
"I have already run Ring games on PC but it's gay" - Jackalus, Jun 19, 2013

4 years later, running Ring games on PC is determined to be favorable, especially with paying Patreon customers!<br>
"Core work done for RingEdge 2 support, currently disabled. (amAuth emulation)"<br>
"Changes TeknoParrot 0.4a Patreon Build" - May 29, 2017<br>
https://www.teknogods.com/viewtopic.php?t=38580

"TeknoParrot Patreon 0.4a out, have fun. #teknoparrot" - May 29, 2017
https://twitter.com/ReaverTeknoGods/status/869293180730081280

TeknoParrot currently supports emulation of a good chunk of the Ring library. 
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/
```
Transformers.json SRC.json SDR.json ProjectDiva.json PPQ.json MaiMaiGreen.json OG.json LGS.json VT4.json 
LGI3D.json KODrive.json ID8.json ID7.json ID6.json GGXrd.json MB.json LGI.json GG.json FightingClimaxIgnition.json  
UDX.json PhantomBreaker.json DOA5.json CaladriusAC.json SSASR.json Mballblitz.json CC.json BorderBreakScramble.json 
Koihime.json GGXrdSIGN.json FightingClimax.json BladeArcus.json UnderNightInBirth.json GGXX.json ArcadeLove.json 
MeltyBloodRE2.json ShiningForceCrossRaid.json ShiningForceCrossExlesia.json ShiningForceCrossElysion.json
```

AP on the otherhand refuses to allow anything related to Teknoparrot, or Ringedge to be discussed as a general rule.<br>
"this is not the place to ask for neither for teknoparrot nor for roms."<br>
https://www.arcade-projects.com/forums/index.php?thread/9093-greetings-from-uk/&postID=145048#post145048

At a certain point interest picked up on the Arcade Projects thread "What can one do with a RingEdge?", eventually leading to the need to censor some of the commentary on the security mechanisms employed by Sega.  
http://archive.is/wOIjp

Once folks in the "Ringedge/2/wide/Nu game list" thread heard "they can run locally and offline!", the *real* thirst began. 
https://webcache.googleusercontent.com/search?q=cache:CiZlw8FpwmEJ:https://www.arcade-projects.com/forums/index.php%3Fthread/6466-ringedge-2-wide-nu-game-list/%26pageNo%3D2+&cd=1&hl=en&ct=clnk&gl=us

# Stage Three
Well after the dick wagging on Assembler Games a random technical examination of the RingEdge popped up:<br>
```
"I have purchased a ring edge that starts a game with a key-chip"
"And SSD is such a rare item... It is locked by ATA's SECURITY lock, but if you UNLOCK it, you can access it from Windows as usual via USB-SATA bridge. Well, as I wrote the other day, there are unknown partitions."
"SSD and key-chip are not tied to the motherboard. In other words, even if SSD and key-chip are moved to another ring edge, it will work"
"Key-chip is linked to the game title. The game does not work even if the key-chip of another game is inserted while it is installed"
```
http://d4.princess.ne.jp/diary/20158.html

The ATA locks were a hurdle that was noted by other folks that were doing similar research into how the Ring* platform works.<br>
"The RingEdge BIOS will only boot a SSD that has the valid TDK RS2 signature on the ATA Identify structure and is locked and also needs to have the password calculated by the BIOS and bassed on that TDK RS2 signature"<br>
https://web.archive.org/web/20170628094958/https://www.assemblergames.com/threads/sega-ringedge-motherboard-inside-pictures.46424/page-2#post-681443

The manufacturing timeline for TDK GBDriver RS2 & RS3 indicates that the RS2 came out in 2010, and the RS3 in 2011. https://product.tdk.com/en/products/flash-storage/flashstorage-catalog_en.pdf

Documentation for the RS2 is located here: https://product.tdk.com/en/products/flash-storage/flashstorage-catalog_en.pdf
"Serial-ATA-II Compatible NAND-Type Flash Memory Controller IC GBDriver RS2 Series"

Documentation for the RS3 likewise can be found here: https://product.tdk.com/info/en/catalog/datasheets/ew_018_rs3.pdf
"Serial ATA 3Gbps Compatible NAND-Type Flash Memory Controller IC GBDriver RS3 Series"

The RS2, and RS3 series drives support ATA drive locking functionality to prevent casual access, where as the drive encryption itself is actually handled by TrueCrypt. 

Bypassing the ATA lock is trivial, at this point the key has proliferated as: 7242525ABA526A5AEA726278CA42DA4A2A223A2A0A221A2A6A027A0A5CCE4A0A<br>

The ATA key can be acquired via commercial SATA analyzer, ghetto style wirewrap+OpenBench, or even something along the lines of a firmware patched SSD based on OCZ Vertex / Jasmine hardware. 

<img src=https://blog.shackspace.de/wp-content/uploads/2011/04/DSC_2883.jpg>

"Open Sesame: Harddrive Password Hacking with a OpenBench Logic Sniffer"
https://shackspace.de/2011/04/27/open-sesame-harddrive-password-hacking-with-a-openbench-logic-sniffer/

https://hackaday.com/2011/04/28/ide-bus-sniffing-and-hard-drive-password-recovery/

"The Evil SSD Project - When your storage has a mind of its own"<br>
https://www.os3.nl/_media/2016-2017/courses/ot/martijn_yonne.pdf

See also the IRATEMONK example for ideas on how an SSD drive could be used to extract the calculated passwords presented by the Sega ATA unlock routines. 
https://www.schneier.com/blog/archives/2014/01/iratemonk_nsa_e.html

None the less the ATA key has been public as early as 2018.
https://pastebin.com/2qiQdPQ6

The commentary offers a great starting point for resarch into Ring* security. 

```
"Basically it looks like a normal PC. As you can see from the actual specifications, it is an AT compatible machine. The motherboard looks like MS-9667, but there is no stamp"
"key-chip communication is a rather troublesome process. I don't know the key-chip because I can't get it."
"NTFS is a basic 3 partition configuration consisting of 2 partitions and an extended partition (content unknown). The first NTFS will bring up the RINGEDGE system. Of course, since there is no key-chip, it will stop with an error. The second is a system update. Probably an update of RINGEDGE itself. Maybe the game installation is also over here? The contents of the extended partition are completely unknown. Is it decrypted using the key of the key-chip?"
```
http://d4.princess.ne.jp/diary/20157.html
```

The disk encryption was something that confused folks at first. 
"See someone abroad who said that the contents of the hard disk partition can be decrypted by hot plugging, but it is too risky to do this. I wonder if there is a great god who has studied this problem here?"
"Encrypted, I am afraid it is not so easy to unlock"
"But even if you extract it, you still have to modify the exe"
```
https://club.tgfcer.com/thread-7148133-1-1.html


Even the hint that Ring* products are just commodity PC hardware is supported by documentation on MS9667, and even Sega's specific variant. The documents MS9667_rev_0a_sch.pdf and MS9667_rev_0b_sch_RING_AALG.pdf can be used to confirm the suspicion about Sega Ring* technology being based on MS9667 based PC.
https://elektrotanya.com/msi_ms-9667_rev_0b_sch.pdf/download.html<br>

### Enter TrueCrypt
The nuances of TrueCrypt on Ring* platform has been a heavily censored topic, although not a complicated one at it's root. In essence you need to acquire both the keys and password to the TrueCrypt container. Both tasks are fairly trivial at the end of the day.  

```
"SegaBoot generates the KeyFile for the TC container of the game on the fly, using the KeyChip,
the process is really complex, but it generates a file on c:\windows\temp with the keyfile,
then mounts the TC container and after the TC Container is successfully mounted deletes the
Keyfile from C:\windows\temp, is just 2 minutes to pach that, is only a matter to remove the
DeleteFile function from SegaBoot with simple NOPs and let SegaBoot to mount the game, then the
Keyfile will be there on c:\windows\temp"
```
https://web.archive.org/web/20170628094958/https://www.assemblergames.com/threads/sega-ringedge-motherboard-inside-pictures.46424/page-2#post-681449

"You might be able to just take off the delete permission from windows temp"<br>
https://web.archive.org/web/20170630214524/https://www.assemblergames.com/threads/sega-ringedge-motherboard-inside-pictures.46424/page-3#post-681518

"Its much more easy than that, just get a file access tool like filemon and see the parameters segaboot is giving to truecrypt, you will know where its storing the binary file that truecrypt uses as password to decrypt the partition"<br>
https://www.assembler-games.com/threads/sega-ringedge-motherboard-inside-pictures.46424/

As expected with this sort of information floating around, it did not take long for folks to start selling "bootleg" versions of Ring games that did not require a key. Sometimes refered to as "NoKey" games, these games made use of leaked TrueCrypt keys to subsequently modify the games behavior preventing it from requiring a proper KeyChip from Sega.<br>

"Topic: Initial D8 Server Ringedge (Original, No Bootleg!)", so wait, where is the bootleg one you made then? lol.<br>
http://www.ukvac.com/forum/initial-d8-server-ringedge-original-no-bootleg_topic367630.html

In addition to bootlegs, you could occasionally find folks offering archival services, the conversation below exposes the concept of a rekey.<br>

"if you want any RingWide game for RingEdge, i can supply you it on a 32Gbytes SSD remastered for work on RingEdge, but you need to have an original keychip on the RingEdge (any one, like MJ5 is ok)... Not, i don't do multi kits for RingEdge. Those Games are expensive like hell and very difficult to buy. I was talking about a single game on a 32GB SSD. Game not patched, still 100% original just remastered RingWide Game OS for work on a RingEdge."<br>
https://web.archive.org/web/20190403174837/https://assemblergames.com/threads/is-it-possible-to-get-ringedge-to-run-ringwide-games.60346/

Mahjong for example has a KeyChip ID of SBVF, and it is a VERY easy to obtain KeyChip... I wonder why so may shared images are rekeyed to it? ;)<br>
https://gakman.forumgaming.fr/t72-ringedge-ringwide#454

There was an effort at one point to document as many chip ID's as possible on AP forums, this sort of effort is extremely useful for archival of all known KeyChips. <br>
https://webcache.googleusercontent.com/search?q=cache:kfuo1iRQy3wJ:https://www.arcade-projects.com/forums/index.php%3Fthread/4456-ringedge-keychip-id/+&cd=1&hl=en&ct=clnk&gl=us

If we come full circle to modern times, folks have finally brought forth conversations about a Ring* keychip emulator. This sort of concept has been deployed in private for quite some time by various players.<br>
https://github.com/ArcadeHustle/RingEdge_SSD_Softmod/issues/1

### The Chinese Jinwin Sega connection? 
One of the first examples of bootlegging was a Chinese Operation Ghost Nokey.<br>
"I've got a RINGEDGE cabient and game is OPERATION GHOST but it seems be a Chinese bootleg don't need the key chip and make me awesome... I want to unplug the SSD driver and explore the game file, but it also a gbdriver rs3, and has encrypted." -  Nov 15, 2015<br>
http://archive.is/M1hvR

There were some interesting *leaks* from the Chinese sega Factory: "the guy who send this to me is at the factory... The seller sells many ODM motherboards,including Ringedge and Lindbergh boards.and he called me and send this to me today earlier. 
Anyone knows what's this?"<br>
https://assembler-games.com/threads/so-recently-i-got-a-strange-board-from-a-factory-which-makes-sega-boards.57620/#post-825992

"Here I have a Simplified Chinese version music game called MaiMai running on RingEdge2 platform. In order to avoid the spam detector please send me a message if you want to get the raw iso data. We tried to make a copy of this disk but failed.If you have tools to decrypt it , please tell us."<br>
https://web.archive.org/web/20190404164948/https://assemblergames.com/threads/pc-based-arcade-games.42102/page-3#post-745324

"SEGA is giving up China market.The JingWen Sega co,ltd has closed at earlier this year,a music game needs frequently update.We have no choice. If nothing unexpected happens,this will be the last update of Wumeng(Chinese version MaiMai).The MaiMai overseas (Version Green) has periodic update per week and the program is totally different to the mainland China version.We cannot get updates and the company has gone.So we find help for carck it."<br>
https://web.archive.org/web/20190404164948/https://assemblergames.com/threads/pc-based-arcade-games.42102/page-3#post-745386

Much of the information above came from Woodu a seemingly random Chinese Sega entheusiast, "Hi from inside of the great firewall". It is unclear at this time where Woodu obtained his Ring* knowledge.<br>
https://github.com/Woodu

What is clear is that he's really obsessed with Sega Jinwin based arcade stuff! 
"Bought a new domain name"<br>
"Jingwen Sega really is a magic company."<br>
"I miss it very much."<br>
https://woodu.me/youxinmailegeyuming/

"This site is not official SEGAJINWIN corp. website, is hosted by Woodu at China Arcade". You can see the original Sega Jinwin site in on The Internet Archive<br>
https://segajinwin.com
https://web.archive.org/web/20130910052147/http://www.segajinwin.com/

So what is JingWin Sega? It was "Established in 2009, Sega Jinwin (Shanghai) Amusement Co. Ltd is a joint-venture of Shanghai Jingwen Investment Co. Ltd., Japan Sega Corporation and affiliated company of China National Center for developing Animation, Cartoon & Game Industry."<br>
http://www.amusewind.com/catalog/all_ENTERPRISES/2012629/27_201262912749768_1.html

Beyond his general love for Sega Woodu has many interesting Ring related things on his site, such as replacement drives<br>
"It has been a long time since I started doing maimai's magical reform in 15 years, and I haven't even put energy on it for a long time. But still did something a little above. What I can take out recently is that I started selling alternative hard drives for the mainframe. This is also the only relatively legal thing"<br>
https://woodu.me/author/woodu/

"SSD for Ringseries. Click here to buy"<br>
https://woodu.me/eryijiuniansanyue/<br>
Ringedge2 120G 固态硬盘 ¥300.00 - 599.00<br>
https://item.taobao.com/item.htm?id=586390733234<br>

"Sega's arcade platform began to completely transform into an X86 based architecture PC, which opened the door to cracking. It is no exaggeration to say that, in addition to the latest arcades such as Ship Mother, DIVA, and Chunithm, SEGA's games can be said to be lost across the board... This arcade is an arcade machine that has been represented in the era of Jingwen Sega. It is a full Chinese version, and there are still people selling it on Taobao."<br>
https://woodu.me/2017/03/<br>

The machine he mentions above is found here... it is a totally NOT bootleg "Lost on Island of Tropics" ("海岛探险游戏机"). "Island Adventure" is a joyful and thrilling shooting game, inheriting the system of the classic shooting game "Let's go jungle", with wonderful stories, compact plots and fun and simple operations to perform wonderfully And a thrilling trip to the island."<br>
http://www.amunion.com/product/247889.html<br>
http://www.haoyunlaigame.com/arc/view-119.html<br>

# Stage Four

Clearly folks have been profiting off the NoKey, and ReKey image instances, both in the form of Chinese Bootleg machines and their accompanying hardware as well as individual private sales. Discussion about the techniques employed have been forbidden fruit for quite some time, partially due to these profit motives. The guise has always been *fear* of Sega retaliating... 

"It's pretty very much illegal and too new for this site's content anyway."
https://webcache.googleusercontent.com/search?q=cache:kPxP6VQIhZYJ:https://www.arcade-projects.com/forums/index.php%3Fthread/10695-sega-ringedge-2-questions-on-obtaining-systems-disks-etc/%26pageNo%3D1+&cd=2&hl=en&ct=clnk&gl=us

Yet the whole time in private, Ring* drives were for sale like hotcakes via PM on AP... this little gem, a patched version of mxsegaboot and mxkeychip enabling it all. 
https://archive.org/details/mxsegaboot

So, yeah the big "secret" is just Truecrypt, as noted above. https://en.wikipedia.org/wiki/TrueCrypt

Specifically the Ring system makes use of TrueCrypt 4.3 in AES LRW mode for TrueCrypt containers, alongside a keyfile and password. This is coupled with a standard ATA lock as mentioned above. 
https://github.com/DrWhax/truecrypt-archive/blob/master/doc/Version-History.md

### Unlocking the drive

For what ever reason Ring* information is often censored quickly, and with malice. There are few remaining bits of archived information. Among them however are these gems:
Both of the archived posts contain partially usable instructions, but can indeed be worked out into a usable technique if you pay close attention.
https://pastebin.com/zQYxBU1e
https://pastebin.com/2qiQdPQ6

The first bit of information revealed in the posts was the static ATA unlock key for the TDK RS2 and RS3 hard drives use by default in Ring* machines. A simple hdparm command will unlock the drive, and allow you to interact with it. 
```
# hdparm --user-master u --security-unlock hex:7242525ABA526A5AEA726278CA42DA4A2A223A2A0A221A2A6A027A0A5CCE4A0A /dev/sdc
security_password: 72 42 52 5a ba 52 6a 5a ea 72 62 78 ca 42 da 4a 2a 22 3a 2a 0a 22 1a 2a 6a 02 7a 0a 5c ce 4a 0a

/dev/sdc:
 Issuing SECURITY_UNLOCK command, password="rBRZ?RjZ?rbx?B?J*":*
"*jz
\?J
", user=user

# fdisk -l /dev/sdb
Disk /dev/sdb: 29.8 GiB, 32017047552 bytes, 62533296 sectors

Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 33553920 bytes
Disklabel type: dos
Disk identifier: 0x06e05113

Device     Boot    Start      End  Sectors   Size Id Type
/dev/sdb1  *          63  2104514  2104452     1G  7 HPFS/NTFS/exFAT
/dev/sdb2        2104515  4209029  2104515     1G  7 HPFS/NTFS/exFAT
/dev/sdb3        4209030 62894474 58685445    28G  f W95 Ext'd (LBA)
/dev/sdb5        4209093  5269319  1060227 517.7M  6 FAT16
/dev/sdb6        5269383  9478349  4208967     2G  6 FAT16
/dev/sdb7        9478413 13687379  4208967     2G  6 FAT16
/dev/sdb8       13687443 45744549 32057107  15.3G  7 HPFS/NTFS/exFAT
/dev/sdb9       45744613 62532474 16787862     8G  6 FAT16

# mount /dev/sdb1 /tmp/a

# cd /tmp/a
# ls
 boot.ini                  NTDETECT.COM  'Program Files'   RECYCLER  'System Volume Information'   WERUNTIME.INI
'Documents and Settings'   ntldr         '$RECYCLE.BIN'    System    '$UGM'                        WINDOWS

```

If you are a Windows user you should be making use of Victoria for your drive unlock needs. http://archive.is/svEXF. 

OSX users currently will have to rely on the hot swap technique until a proper ATA passthrough tecnique is worked out to send the ATA unlock commands. 


### Mounting TrueCrypt containers

Once the drive has been mounted you will as expected encounter a number of TrueCrypt partitions, as well as a file based container in "C:\System\Execute\System". You can mount the TrueCrypt image, and drive partitionss within linux or OSX fairly easily if you do not prefer to use Windows. You can mount either encrypted files directly, or dd based drive images via losetup. Likewise you can of couse simply mount the actual drive partitions. 

You will find that the partition layout is as follows.
```
Partition 1 - \System\ (Boot Partition)
Partition 2 - \MiniNT  (Recovery Partition)
Partition 3 - 518 Meg  (?TrueCrypt? Partition)
Partition 4 - 	       (Update Partition - TrueCrypt Protected)
Partition 5 -          (? ? Partition)
Partition 6 -          (? OS Drivers ? Partition)
Partition 7 -          (Game Partition  - TrueCrypt Protected)
```

First you will need a working TrueCrypt setup of some sort, either the original, or a fork. In theory some versions of Veracrypt are usable, but LRW support must be present, your best bet is the Linux version. 
https://www.veracrypt.fr/code/VeraCrypt/tree/src/Common/Volumes.c?h=VeraCrypt_1.17&id=03867fbf5653c0260e71271e0ddf46ed1045b488#n805

FUSE software consists of a kernel extension and various user space libraries that makes LRW work on non Windows versions of TrueCrypt past 4.x. You'll need that too if you are an OSX, or Linux user trying to follow along. https://forums.gentoo.org/viewtopic-t-688399-start-0.html

Either path you choose you'll need some form of TrueCrypt source. The below example shows Truecrypt5 being installed on Ubuntu. The source code was pulled from the git repo below. 
https://github.com/DrWhax/truecrypt-archive
https://github.com/DrWhax/truecrypt-archive/blob/master/doc/Version-History.md

```
# wget https://github.com/stefansundin/truecrypt-archive/raw/master/truecrypt-5.1a-ubuntu-x64.tar.gz
# tar -zxvf truecrypt-5.1a-ubuntu-x64.tar.gz 
# ./truecrypt-5.1a-setup-ubuntu-x64 
...
Installation package file truecrypt_5.1a-0_amd64.deb extracted and placed in /tmp

# dpkg -i --force-all truecrypt_5.1a-0_amd64.deb
# truecrypt --version
TrueCrypt 5.1a

# dpkg -l fuse
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                                Version                Architecture           Description
+++-===================================-======================-======================-===========================================================================
ii  fuse                                2.9.4-1ubuntu3.1       amd64                  Filesystem in Userspace
```

Once fuse works, and your truecrypt has been installed you can mount TC containers. 

A patched version of TrueCrypt can be used to mount images on OSX Catalina 10.15 as described here: 
http://www.nerdenmeister.org/2013/08/16/build-truecrypt-on-os-x-64-bit-with-hardware-acceleration/
https://gist.github.com/neurodroid/7059368

A pre-patched version is located here, but you will need to modify the Makefile to make it work on Catalina. We've actually gone through the exercise and included it in our own git repo. 
https://github.com/neurodroid/TrueCrypt

If you make use of Paragon NTFS modules for Mac you can also write content to the mounted images.
https://www.paragon-software.com/us/home/ntfs-mac/

Alternately you can also mount TC drives on OSX using CipherShed, but you'll need to use the patches from TrueCrypt to make them work on modern OSX. Patched versions of the CipherShed and TrueCrypt repos are included in our repo, ready to compile on OSX Cataline 10.15. We actually include the binaries as well... 
https://webcache.googleusercontent.com/search?q=cache:rCoVjQzFDMoJ:https://wiki.ciphershed.org/BuildOnOSX+&cd=1&hl=en&ct=clnk&gl=us

This will help you determine which disk encryption programs are compatable with LRW if you wish to try mounting TC images that *hard* way, opposed to just using one of the methods outlined above. Using TrueCrypt on Windows is left as an exercise for the reader, especially considering how heavily documented it it. 
https://wiki2.org/en/Comparison_of_disk_encryption_software

Here is an example with TrueCrypt on Linux:
```
$ mkdir /tmp/tc
$ sudo truecrypt -p segahardpassword -k SystemKeyFile System /tmp/tc

$ ls /tmp/tc
d3dref9.dll         lockid.txt      mxgdeliver.exe   mxkeychip.exe  mxsegaboot_2052.dll  mxstorage.exe        $RECYCLE.BIN
default_regset.txt  mxauthdisc.exe  mxgfetcher.exe   mxmaster.exe   mxsegaboot.exe       ORIG_mxkeychip.exe   ringmaster_pub.pem
develop_regset.txt  mxgcatcher.exe  mxinstaller.exe  mxnetwork.exe  mxshellexecute.exe   ORIG_mxsegaboot.exe  System Volume Information

$ truecrypt -d /tmp/tc

```

Here is an example with CipherShed on OSX:
```
$ mkdir /tmp/z; ./CipherShed-OSX-64/src/Main/CipherShed -t System_Pengo -k SystemKeyFile /tmp/z -p segahardpassword 
Protect hidden volume (if any)? (y=Yes/n=No) [No]: 

$ ./CipherShed-OSX-64/src/Main/CipherShed -d
```

### Obtaining the KeyFile and Volume Password
You may be wondering at this point how exactly the KeyFile was obtained. There were brief notes in the pastebin links above for one technique, but we really need to go in depth into how TrueCrypt can be attacked for academic posterity. 

Hint: The technique most folks use involves patching several Sega binaries to not delete files in a TEMP folder, coupled with a hardcoded drive password similarly found with the same binaries. The below commentary will examine an alternate path to mounting an encrypted TC drive, post memory acquisition. 

Memory can be acquired via a number of means, perhaps the easiest being DMA access over PCI with something like PCILeech https://github.com/ufrisk/pcileech 
"PCILeech uses PCIe hardware devices to read and write target system memory. This is achieved by using DMA over PCIe. No drivers are needed on the target system"

USB3380EVB  (USB3380 Evaluation Board)
http://www.hwtools.net/Adapter/USB3380EVB.html

PicoDMA: DMA Attacks at Your Fingertips - https://www.youtube.com/watch?v=j8pCjgaByVo
https://i.blackhat.com/USA-19/Wednesday/us-19-Sandin-PicoDMA-DMA-Attacks-At-Your-Fingertips.pdf

https://shop.lambdaconcept.com/home/40-screamer-m2.html
"Screamer M.2 replaces PCIe Screamer R02 with an M.2 form factor and PCIe x4 connectivity"

It may be possible to exploit a software vulnerability in order to gain access to install LeechAgent
https://blog.frizk.net/2019/04/LeechAgent.html

"The LeechAgent is a 100% free open source endpoint solution geared towards remote physical memory acquisition and analysis on Windows endpoints in Active Directory environments."

There is even a possibility you can get fancy and exploit the IME for DMA access. That is way beyond the scope of this document however!
https://github.com/ptresearch/IntelTXE-PoC
IME of course "has full access to the whole DRAM (by using its own DMA engine)"
https://www.blackhat.com/docs/us-17/thursday/us-17-Evdokimov-Intel-AMT-Stealth-Breakthrough-wp.pdf

"Intel Management Engine (Intel ME) is a proprietary technology that consists of a microcontroller integrated into the Platform Controller Hub (PCH) chip and a set of built-in peripherals. The PCH carries almost all communication between the processor and external devices. Therefore, Intel ME has access to almost all data on the computer. The ability to execute third-party code on Intel ME would allow for a complete compromise of the platform... By exploiting the vulnerability that we found in the bup module, we were able to turn on a mechanism, PCH red unlock, that opens full access to all PCH devices for their use via the DFx chain—in other words, using JTAG. One such device is the x86 ME processor itself, and so we obtained access to its internal JTAG interface. With such access, we could debug code executed on ME, read memory of all processes and the kernel, and manage all devices inside the PCH. We found a total of about 50 internal devices to which only ME has full access, while the main processor has access only to a very limited subset of them."
https://www.blackhat.com/docs/eu-17/materials/eu-17-Goryachy-How-To-Hack-A-Turned-Off-Computer-Or-Running-Unsigned-Code-In-Intel-Management-Engine-wp.pdf

https://www.synacktiv.com/posts/pentest/practical-dma-attack-on-windows-10.html
"In order to proceed to a straightforward DMA attack, many prerequisites must be met"

A number of academic articles on attacking TrueCrypt seem applicable, there was so much news hype on weaknesses within the platform. How do they play out in the real world? How do they impact Sega's implementation? 
Lets examine a few of the papers: 
Detecting the use of TrueCrypt - http://docs.media.bitpipe.com/io_10x/io_102267/item_885954/RH%203%20Davies.pdf
"Of greatest use to a forensic investigator is the Registry location “HKEY_ LOCAL_MACHINE \system\MountedDevices”. The data stored in this key could confirm that a mounted volume is indeed a TrueCrypt volume. But it does not differentiate between the standard and hidden TrueCrypt volume types"

Error Correction and the Cryptographic Key - ftp://ftp.cs.princeton.edu/techreports/2011/897.pdf
"LRW implementations commonly precompute a large multiplication table generated from the tweak key, each entry of which is generated by shifting and possibly XORing with a known value. An entire multiplication table will contain many copies of nearly all of the bits of K2... rueCrypt 4 precomputes a 4048-byte multiplication table consisting of 16 blocks of 16 lines of 4 words of 4 bytes each. Line 0 of block 14 contains the tweak key... The multiplication table is generated line by line from the LRW key by iteratively applying the shift-and-XOR multiply function to generate four new values, and then XORing all combinations of these four values to create 16 more lines of the table."

"From 2004 to 2006, drafts of the P1619 standards used the Advanced Encryption Standard (AES) in LRW mode. In the 30 Aug 2006 meeting of the SISWG, a straw poll showed that most members would not approve P1619 as it was"
https://en.wikipedia.org/wiki/IEEE_P1619#LRW_issue

"RE: pay attention to P1619 so-called 'Pink herrings'" - https://web.archive.org/web/20160303184448/http://grouper.ieee.org/groups/1619/email/msg00923.html

"P1619: how serious is the leak of K2?"
https://web.archive.org/web/20170405155232/http://grouper.ieee.org:80/groups/1619/email/msg00962.html

https://citp.princeton.edu/our-work/memory/code
"These prototype applications are intended to illustrate the techniques described in the paper (Error Correction and the Cryptographic Key)"

Security Analysis of TrueCrypt 7.0a with an Attack on the Keyfile Algorithm - https://cyberside.net.ee/truecrypt/misc/truecrypt_7.0a-analysis-en.pdf
"Up to version 4.0 TrueCrypt applied the Cipher Block Chaining mode (CBC)... This mode, however, has considerable weaknesses if applied in the context of a volume encryption... In order to close that security breach TrueCrypt replaced the CBC mode with the LRW mode in version 4.1. The CBC mode was further supported for backward compatibility but new containers were only created with the LRW mode. The LRW mode is named after its inventers Liskov, Rivest and Wagner . In this mode a second key of the same length as the block length is multiplied with a block counter in a Galois field and the result of this mathematical operation is added as well to the plain text before encryption of the block as to the cipher text after that encryption... In version 5.0 TrueCrypt introduced the XTS mode as a replacement for the LRW mode . The XTS mode is a slight modification of the LRW mode designed to compensate for a theoretical little weakness of the LRW mode"

Mastering TrueCrypt: Windows 8 and Server 2012 Memory Forensics - https://downloads.volatilityfoundation.org/omfw/2013/OMFW2013_Ligh.pdf
"Force it to use ./master.key which came from the RAM dump... Patch based on code by Michael Weissbacher hpp://mweissbacher.com/blog/tag/truecrypt/"

#TrueCrypt PlaidCTF Writeup: Fun with Firewire - https://mweissbacher.com/tag/truecrypt
"Remember that TrueCrypt first decrypts the header with the password, and then reads the AES-key from the decrypted header. Reading in the header is done in Volume/VolumeHeader.cpp:VolumeHeader::Deserialize(.,.,.). We patch the code there, right after the master and secondary key was read from the decrypted header, and replace it with the hard-coded key value we found in the previous step"

A Security Analysis of TrueCrypt: Detecting hidden volumes and operating systems - https://www.ma.rhul.ac.uk/static/techrep/2014/RHUL-MA-2014-10.pdf
"TrueCrypt system volume layout containing a hidden operating system... "

truecrypt second encryption of the master and XTS key with a back door password - https://security.stackexchange.com/questions/19764/truecrypt-second-encryption-of-the-master-and-xts-key-with-a-back-door-password
"Since version 4.2a the format of TrueCrypt headers changed three times with the versions 5.0, 6.0 and 7.0"

TrueCrypt Master Key Extraction And Volume Identification - https://volatility-labs.blogspot.com/2014/01/truecrypt-master-key-extraction-and.html
"The truecryptsummary plugin gives you a detailed description of all TrueCrypt related artifacts in a given memory dump."

TrueCrypt Security: Securing Yourself against Practical TrueCrypt Attacks - https://resources.infosecinstitute.com/defeating-truecrypt-practical-attacks-truecrypt-security/#gref
"‘Aeskeyfind’ implements this approach, and we use it to search for AES keys in our memory image... Alternatively, you can use ‘bulk extractor’ to locate keys in memory... We now need to “patch” TrueCrypt so that it accepts the discovered AES keys. Here, we have patched TrueCrypt 7.1. For this purpose, we modify the ‘VolumeHeader.cpp’ file and hard code the AES keys in there" 
 
Recovery of Encryption Keys from Memory Using a Linear Scan - https://www.researchgate.net/publication/221548532_Recovery_of_Encryption_Keys_from_Memory_Using_a_Linear_Scan
"TrueCrypt encrypted containers appear to contain nothing but random data and have no file signature. However, the first 512 bytes of a TrueCrypt container are actually a header, but are encrypted using a Header Key so still appears to be random data... TrueCrypt decrypts the header using a user-supplied password or keyfile, salt from offset 0-64 (bytes) and then the process of trial and error using different encryption and key derivation algorithms, modes of encryption (CBC, LRW etc.) and key derivation algorithms. Successful decryption of the header is when bytes 64-68 decrypt to the ASCII string ‘TRUE’. The entire header is then decrypted which in the case of LRW mode, contains the Master Key and Secondary Master Key (Tweak Key) needed to decrypt the actual contents of the container, from the ‘Data Area’ which begins at offset 512."

The following tools also provide intellectual reading on the subject at hand. 
tckfs: This tool seeks asynchronously TrueCrypt key file using combinations of provided key files with provided password. - https://github.com/Octosec/tckfc
Untrue: Tool for checking passwords against TrueCrypt encrypted volumes and disks, and/or decrypting the data. - https://github.com/nccgroup/Untrue
Master Key Decryptor: is a python script to assist with decrypting encrypted volumes using the recovered masterkey for various truecrypt type encrypted volumes. https://github.com/AmNe5iA/MKDecrypt
Truecrypt volume parsing library - https://github.com/4144414D/pytruecrypt
Interrogate: https://sourceforge.net/projects/interrogate/
Bulk Extractor: https://github.com/simsong/bulk_extractor.git
Aes-Finder: https://github.com/mmozeiko/aes-finder.git
AesKeyFind: https://github.com/makomk/aeskeyfind
Stark aes_keyschedule: https://github.com/SideChannelMarvels/Stark/blob/master/aes_keyschedule.c

One theoretical way to obtain an unencrypted TrueCrypt image is by using the master key pulled from memory. 

./Common/Crypto.h:226:	unsigned __int8 master_keydata[MASTER_KEYDATA_SIZE];	/* ... For LRW (deprecated/legacy), it contains the tweak key before the master key(s). */

Take a memory dump by using mdd.exe, then lets search it for AES keys. 
```
$ src/bulk_extractor -o /tmp/TC_keys -E aes /Volumes/UNTITLED11/memdump.raw 
bulk_extractor version: 1.6.0
Hostname: xxx
Input file: /Volumes/UNTITLED11/memdump.raw
Output directory: /tmp/TC_keys
Disk Size: 2070982656
Threads: 4
Attempt to open /Volumes/UNTITLED11/memdump.raw
16:02:40 Offset 67MB (3.24%) Done in  0:01:05 at 16:03:45
16:02:42 Offset 150MB (7.29%) Done in  0:00:53 at 16:03:35
...
MD5 of Disk Image: f1b7aef524504e1253bc1299d6d5e6cf
Phase 2. Shutting down scanners
Phase 3. Creating Histograms
Elapsed time: 51.3567 sec.
Total MB processed: 2070
Overall performance: 40.3254 MBytes/sec (10.0814 MBytes/sec/thread)

$ cat /tmp/TC_keys/aes_keys.txt 
# BANNER FILE NOT PROVIDED (-b option)
# BULK_EXTRACTOR-Version: 1.6.0 ($Rev: 10844 $)
# Feature-Recorder: aes_keys
# Filename: /Volumes/UNTITLED11/memdump.raw
# Feature-File-Version: 1.1
161230888	5c 52 f8 f0 ec 65 38 dc bc 94 6d 70 41 b0 84 f1 4f ea f9 54 5f 28 a3 e9 ac f7 01 16 3c c4 83 43 	AES256
161427496	0d 0f cf 25 93 61 00 36 25 f7 cd 26 df 74 cd 22 e7 c2 41 3d 4a 90 e3 b9 9c 45 2e 8d 69 a7 c4 45 	AES256
163037224	f3 5c 32 3e 77 d8 81 b7 f3 45 a0 c8 c4 ba 16 8e a4 5a 3b 43 b3 25 1b a2 e6 bb 25 1f 51 8e a6 2b 	AES256
1825566060	00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 	AES256
1942490476	00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 	AES256
2019151212	00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f 10 11 12 13 14 15 16 17 18 19 1a 1b 1c 1d 1e 1f 	AES256


$ ./aeskeyfind -t 50 -v /Volumes/UNTITLED11/memdump.raw
Keyfind progress: 0%
FOUND POSSIBLE 256-BIT KEY AT BYTE 99c3028 

KEY: 5c52f8f0ec6538dcbc946d7041b084f14feaf9545f28a3e9acf701163cc48343

EXTENDED KEY: 
5c52f8f0ec6538dcbc946d7041b084f1
4feaf9545f28a3e9acf701163cc48343
41bee21baddbdac7114fb7b750ff3346
1cfc3a0e43d499e7ef2398f1d3e71bb2
d711d57d7aca0fba6b85b80d3b7a8b4b
fe2607bdbdf29e5a52d106ab81361d19
d6b50171ac7f0ecbc7fab6c6fc803d8d
4eeb20e0f319bebaa1c8b81120fea508
65b331c6c9cc3f0d0e3689cbf2b6b446
c7a5adba34bc13009574ab11b58a0e19
0b18e513c2d4da1ecce253d53e54e793
7585396641392a66d44d817761c78f6e
ed6b7afc2fbfa0e2e35df337dd0914a4
b484c32ff5bde94921f0683e4037e750
37ff29f518408917fb1d7a2026146e84

CONSTRAINTS ON ROWS:
0000001400000000000000000000000000000000000000000000000000000000
0000009900000000000000000000000000000000000000000000000000000000
000000f300000000000000000000000000000000000000000000000000000000
0000004800000000000000000000000000000000000000000000000000000000
0000002a00000000000000000000000000000000000000000000000000000000
0000001000000000000000000000000000000000000000000000000000000000
000000f6000000000000000000000000
3531f08e4ba2466d72eaf0e0ae086d7cec3596d9394d8c2c8e95b8b7bec5eb84
029086c67ec9a2027011adbf75f6a1feb08153874ef6869ca47a0c37902307b4
14afee4f0828648045decc8d05e70c41f4f5a4fffd983fb69f08b6e534590b83
fe38635b943d818e9c13b8274039c0cc5ce4ff6e225aa69f4121a6f4ab51bd66
07b56cfbc4681f781f4b86d5dc2a78eb0e4e34067feab1ea916abe38ea701b92
902530d818631955b2c11adfc361fe3e90ecbcf4fcda64b7538822917b1aa5aa
9450c89d1b14e4edc9eafa0571a0e4e142bcde268a434ebf2880f951cb00d419

$ ./interrogate -a aes -k 256 /Volumes/UNTITLED11/memdump.raw 
Interrogate  Copyright (C) 2008  Carsten Maartmann-Moe <carmaa@gmail.com>
This program comes with ABSOLUTELY NO WARRANTY; for details use `-h'.
This is free software, and you are welcome to redistribute it
under certain conditions; see bundled file licence.txt for details.

Using key size: 256 bits.
Using input file: /Volumes/UNTITLED11/memdump.raw.
Attempting to load entire file into memory, please stand by...
Success, starting search.

--------------------------------------------------------------------------------
Found (probable) AES key at offset 099c3028:

5c 52 f8 f0 ec 65 38 dc bc 94 6d 70 41 b0 84 f1 
4f ea f9 54 5f 28 a3 e9 ac f7 01 16 3c c4 83 43 

Expanded key:

5c 52 f8 f0 ec 65 38 dc bc 94 6d 70 41 b0 84 f1 
4f ea f9 54 5f 28 a3 e9 ac f7 01 16 3c c4 83 43 
41 be e2 1b ad db da c7 11 4f b7 b7 50 ff 33 46 
1c fc 3a 0e 43 d4 99 e7 ef 23 98 f1 d3 e7 1b b2 
d7 11 d5 7d 7a ca 0f ba 6b 85 b8 0d 3b 7a 8b 4b 
fe 26 07 bd bd f2 9e 5a 52 d1 06 ab 81 36 1d 19 
d6 b5 01 71 ac 7f 0e cb c7 fa b6 c6 fc 80 3d 8d 
4e eb 20 e0 f3 19 be ba a1 c8 b8 11 20 fe a5 08 
65 b3 31 c6 c9 cc 3f 0d 0e 36 89 cb f2 b6 b4 46 
c7 a5 ad ba 34 bc 13 00 95 74 ab 11 b5 8a 0e 19 
0b 18 e5 13 c2 d4 da 1e cc e2 53 d5 3e 54 e7 93 
75 85 39 66 41 39 2a 66 d4 4d 81 77 61 c7 8f 6e 
ed 6b 7a fc 2f bf a0 e2 e3 5d f3 37 dd 09 14 a4 
b4 84 c3 2f f5 bd e9 49 21 f0 68 3e 40 37 e7 50 
37 ff 29 f5 18 40 89 17 fb 1d 7a 20 26 14 6e 84 
```

### Playing around with Volatility

"I have used the Truecrypt plugins in Volatility but they simply do not work" https://www.forensicfocus.com/Forums/viewtopic/p=6582443/

We can use Volatility framework to examine a memory dump. https://github.com/volatilityfoundation/volatility/wiki/Command-Reference
This shows the lineage of the processes 
```
$ python vol.py -f /Volumes/UNTITLED11/memdump.raw pstree
Volatility Foundation Volatility Framework 2.6.1
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0x8a711a00:System                                      4      0     80   2636 1970-01-01 00:00:00 UTC+0000
...
..... 0x89ff49e0:mxstartup.exe                        252   1212      0 ------ 2020-05-05 08:28:12 UTC+0000
...... 0x89f04838:mxmaster.exe                        488    252      3     61 2020-05-05 08:28:13 UTC+0000
....... 0x89efe898:mxstorage.exe                      512    488      1     36 2020-05-05 08:28:13 UTC+0000
....... 0x89ef67e8:nxMount.exe                        520    488      1     32 2020-05-05 08:28:13 UTC+0000
....... 0x89e91368:mxgcatcher.exe                     640    488      2     41 2020-05-05 08:28:15 UTC+0000
....... 0x89e9cbc8:mxgdeliver.exe                     292    488      2     44 2020-05-05 08:28:15 UTC+0000
....... 0x89ef7b98:mxnetwork.exe                      504    488      1     68 2020-05-05 08:28:13 UTC+0000
....... 0x89e9d578:mxgfetcher.exe                     476    488      3     44 2020-05-05 08:28:15 UTC+0000
....... 0x89ef9598:mxkeychip.exe                      496    488      1    677 2020-05-05 08:28:13 UTC+0000
....... 0x89e95880:mxinstaller.exe                    632    488      6     53 2020-05-05 08:28:15 UTC+0000
....... 0x89deb748:nxAuth.exe                        2068    488      3    105 2020-05-05 08:28:41 UTC+0000

$ python vol.py -f /Volumes/UNTITLED11/memdump.raw truecryptsummary
Volatility Foundation Volatility Framework 2.6.1
Service              truecrypt state SERVICE_RUNNING
Kernel Module        truecrypt.sys at 0xb31f8000 - 0xb3225000
Symbolic Link        P: -> \Device\TrueCryptVolumeP mounted 2020-05-05 08:28:36 UTC+0000
Symbolic Link        Volume{556d4862-8eaa-11ea-93eb-00d0f1164195} -> \Device\TrueCryptVolumeO mounted 2020-05-05 08:28:35 UTC+0000
Symbolic Link        P: -> \Device\TrueCryptVolumeP mounted 2020-05-05 08:28:36 UTC+0000
Symbolic Link        S: -> \Device\TrueCryptVolumeS mounted 2020-05-05 08:28:13 UTC+0000
Symbolic Link        O: -> \Device\TrueCryptVolumeO mounted 2020-05-05 08:28:36 UTC+0000
Symbolic Link        Volume{556d485f-8eaa-11ea-93eb-00d0f1164195} -> \Device\TrueCryptVolumeS mounted 2020-05-05 08:28:13 UTC+0000
Symbolic Link        S: -> \Device\TrueCryptVolumeS mounted 2020-05-05 08:28:13 UTC+0000
Symbolic Link        Volume{556d4862-8eaa-11ea-93eb-00d0f1164195} -> \Device\TrueCryptVolumeO mounted 2020-05-05 08:28:35 UTC+0000
Symbolic Link        P: -> \Device\TrueCryptVolumeP mounted 2020-05-05 08:28:36 UTC+0000
Symbolic Link        Volume{556d4863-8eaa-11ea-93eb-00d0f1164195} -> \Device\TrueCryptVolumeP mounted 2020-05-05 08:28:36 UTC+0000
Symbolic Link        O: -> \Device\TrueCryptVolumeO mounted 2020-05-05 08:28:35 UTC+0000
Symbolic Link        P: -> \Device\TrueCryptVolumeP mounted 2020-05-05 08:28:36 UTC+0000
Symbolic Link        S: -> \Device\TrueCryptVolumeS mounted 2020-05-05 08:28:13 UTC+0000
...
File Object          \Device\TrueCryptVolumeP\RE2multi\menu\imageformats\qico.dll at 0x9947360
File Object          \Device\TrueCryptVolumeO\Games\Blade Arcus from Shining [SDAF]\Blade-Arcus-from-Shining.jpg at 0x994d778
File Object          \Device\TrueCryptVolumeP\RE2multi\menu\theme\CyberPunk\480p.style at 0x994dc58
File Object          \Device\TrueCryptVolumeP᱘E2multi\assets\JVSDll.dll at 0x994e648
File Object          \Device\TrueCryptVolumeP\RE2multi\assets\JVSDll.dll at 0x994e778
File Object          \Device\TrueCryptVolumeP\RE2multi\menu\imageformats\qjpeg.dll at 0x994e980
File Object          \Device\TrueCryptVolumeP孠E2multi\menu\plugins\video_output\libdirect2d_plugin.dll at 0x994ea80
File Object          \Device\TrueCryptVolumeP\RE2multi\menu\plugins\video_output\libcaca_plugin.dll at 0x994eb18
File Object          \Device\TrueCryptVolumeP鄈�multi\menu\plugins\video_output\libyuv_plugin.dll at 0x994f260
File Object          \Device\TrueCryptVolumeP\RE2multi\menu\plugins\video_output\libwingdi_plugin.dll at 0x994f2f8
File Object          \Device\TrueCryptVolumeP䞈៰multi\menu\plugins\video_output\libwingdi_plugin.dll at 0x994f570
File Object          \Device\TrueCryptVolumeP\RE2multi\menu\theme\CyberPunk\bg_480p.jpg at 0x994f980
File Object          \Device\TrueCryptVolumeP\RE2multi\menu\plugins\video_output\libglwin32_plugin.dll at 0x994fb80
File Object          \Device\TrueCryptVolumeP\RE2multi\menu\plugins\video_output\libyuv_plugin.dll at 0x9951300
File Object          \Device\TrueCryptVolumeP\RE2multi\menu\plugins\plugins.dat at 0x9951ae8
...
File Object          \Device\TrueCryptVolumeP\RE2multi\menu\plugins\access\librar_plugin.dll at 0xa1ed2a8
File Object          \Device\TrueCryptVolumeP\RE2multi\menu\plugins\access\libudp_plugin.dll at 0xa1edb68
Driver               \Driver\truecrypt at 0x9c56d78 range 0xb31f8000 - 0xb3224340
Device               TrueCryptVolumeP at 0x8a645030 type FILE_DEVICE_DISK
Container            Path: <HIDDEN>
Device               TrueCryptVolumeO at 0x8a644808 type FILE_DEVICE_DISK
Container            Path: \??\C:\Documents and Settings\k8team\Start Menu\Programs\Startup\desktop.ini?
Device               TrueCryptVolumeS at 0x89f06030 type FILE_DEVICE_DISK
Container            Path: \??\C:\System\Execute\System
Device               TrueCrypt at 0x89f9bcb0 type FILE_DEVICE_UNKNOWN

$ python vol.py -f /Volumes/UNTITLED11/memdump.raw dumpfiles --dump-dir /tmp/zzzz
Volatility Foundation Volatility Framework 2.6.1
DataSectionObject 0x8a11ab50   4      \Device\HarddiskVolume1\WINDOWS\system32\config\SYSTEM
SharedCacheMap 0x8a11ab50   4      \Device\HarddiskVolume1\WINDOWS\system32\config\SYSTEM
DataSectionObject 0x8a0abdd0   4      \Device\HarddiskVolume1\WINDOWS\system32\config\DEFAULT
SharedCacheMap 0x8a0abdd0   4      \Device\HarddiskVolume1\WINDOWS\system32\config\DEFAULT
DataSectionObject 0x8a0a9af0   4      \Device\HarddiskVolume1\WINDOWS\system32\config\SAM
SharedCacheMap 0x8a0a9af0   4      \Device\HarddiskVolume1\WINDOWS\system32\config\SAM
DataSectionObject 0x8a610a10   4      \Device\HarddiskVolume1\WINDOWS\system32\config\SOFTWARE
SharedCacheMap 0x8a610a10   4      \Device\HarddiskVolume1\WINDOWS\system32\config\SOFTWARE
DataSectionObject 0x8a134a50   4      \Device\HarddiskVolume1\WINDOWS\system32\config\SECURITY
SharedCacheMap 0x8a134a50   4      \Device\HarddiskVolume1\WINDOWS\system32\config\SECURITY
...
ImageSectionObject 0x89f88618   496    \Device\TrueCryptVolumeS\mxkeychip.exe
DataSectionObject 0x89f88618   496    \Device\TrueCryptVolumeS\mxkeychip.exe
ImageSectionObject 0x89f866d0   504    \Device\TrueCryptVolumeS\mxnetwork.exe
DataSectionObject 0x89f866d0   504    \Device\TrueCryptVolumeS\mxnetwork.exe
ImageSectionObject 0x89efb318   512    \Device\TrueCryptVolumeS\mxstorage.exe
DataSectionObject 0x89efb318   512    \Device\TrueCryptVolumeS\mxstorage.exe
ImageSectionObject 0x89f02b80   520    \Device\TrueCryptVolumeS\nxMount.exe
DataSectionObject 0x89f02b80   520    \Device\TrueCryptVolumeS\nxMount.exe
ImageSectionObject 0x89e9f768   632    \Device\TrueCryptVolumeS\mxinstaller.exe
DataSectionObject 0x89e9f768   632    \Device\TrueCryptVolumeS\mxinstaller.exe
ImageSectionObject 0x89e9c2b8   640    \Device\TrueCryptVolumeS\mxgcatcher.exe
DataSectionObject 0x89e9c2b8   640    \Device\TrueCryptVolumeS\mxgcatcher.exe
ImageSectionObject 0x8a5e3c28   476    \Device\TrueCryptVolumeS\mxgfetcher.exe
DataSectionObject 0x8a5e3c28   476    \Device\TrueCryptVolumeS\mxgfetcher.exe
ImageSectionObject 0x89e98358   292    \Device\TrueCryptVolumeS\mxgdeliver.exe
DataSectionObject 0x89e98358   292    \Device\TrueCryptVolumeS\mxgdeliver.exe
...

$ file /tmp/zzzz/*
/tmp/zzzz/file.1044.0x89fa3490.img:  PE32 executable (DLL) (console) Intel 80386, for MS Windows
/tmp/zzzz/file.1044.0x8a098380.img:  PE32 executable (GUI) Intel 80386, for MS Windows
/tmp/zzzz/file.1100.0x89fa30c8.img:  PE32 executable (DLL) (console) Intel 80386, for MS Windows
/tmp/zzzz/file.1100.0x89ff9b08.dat:  PE32 executable (DLL) (GUI) Intel 80386, for MS Windows
/tmp/zzzz/file.1100.0x8a0ae738.img:  PE32 executable (DLL) (console) Intel 80386, for MS Windows
/tmp/zzzz/file.1100.0x8a0b13e0.img:  PE32 executable (DLL) (GUI) Intel 80386, for MS Windows
/tmp/zzzz/file.1100.0x8a605290.img:  PE32 executable (DLL) (console) Intel 80386, for MS Windows
/tmp/zzzz/file.1100.0x8a690f30.img:  PE32 executable (DLL) (console) Intel 80386, for MS Windows
...
```

### Modifying the OS boot image

Regardless of how you obtained the key, once you get the drives mounted, you can begin modifying the system to be more friendly for casual non gaming use. (Such as dumping key chips)

First we use chntpw to list the users on the system. 
```
# cd /tmp/a/WINDOWS/system32/config
# wget https://pogostick.net/~pnh/ntpasswd/chntpw-source-140201.zip

# ./chntpw -l ../SAM
chntpw version 1.00 140201, (c) Petter N Hagen
Hive <../SAM> name (from header): <\SystemRoot\System32\Config\SAM>
ROOT KEY at offset: 0x001020 * Subkey indexing type is: 686c <lh>
File size 262144 [40000] bytes, containing 5 pages (+ 1 headerpage)
Used for data: 208/15824 blocks/bytes, unused: 6/4496 blocks/bytes.

| RID -|---------- Username ------------| Admin? |- Lock? --|
| 01f4 | Administrator                  | ADMIN  | dis/lock |
| 03e9 | AppUser                        |        |          |
| 01f5 | Guest                          |        | dis/lock |
| 03e8 | SystemUser                     | ADMIN  |          |

```

Next we begin to edit the registry to be more permissive. 
```

# ./chntpw -i ../SAM
chntpw version 1.00 140201, (c) Petter N Hagen
Hive <../SAM> name (from header): <\SystemRoot\System32\Config\SAM>
ROOT KEY at offset: 0x001020 * Subkey indexing type is: 686c <lh>
File size 262144 [40000] bytes, containing 5 pages (+ 1 headerpage)
Used for data: 208/15824 blocks/bytes, unused: 6/4496 blocks/bytes.



<>========<> chntpw Main Interactive Menu <>========<>

Loaded hives: <../SAM>

  1 - Edit user data and passwords
  2 - List groups
      - - -
  9 - Registry editor, now with full write support!
  q - Quit (you will be asked if there is something to save)


What to do? [1] -> 1


===== chntpw Edit User Info & Passwords ====

| RID -|---------- Username ------------| Admin? |- Lock? --|
| 01f4 | Administrator                  | ADMIN  | dis/lock |
| 03e9 | AppUser                        |        |          |
| 01f5 | Guest                          |        | dis/lock |
| 03e8 | SystemUser                     | ADMIN  |          |

Please enter user number (RID) or 0 to exit: [3e8] 03e8
================= USER EDIT ====================

RID     : 1000 [03e8]
Username: SystemUser
fullname: 
comment : 
homedir : 

00000220 = Administrators (which has 2 members)

Account bits: 0x0010 =
[ ] Disabled        | [ ] Homedir req.    | [ ] Passwd not req. | 
[ ] Temp. duplicate | [X] Normal account  | [ ] NMS account     | 
[ ] Domain trust ac | [ ] Wks trust act.  | [ ] Srv trust act   | 
[ ] Pwd don't expir | [ ] Auto lockout    | [ ] (unknown 0x08)  | 
[ ] (unknown 0x10)  | [ ] (unknown 0x20)  | [ ] (unknown 0x40)  | 

Failed login count: 0, while max tries is: 0
Total  login count: 44

- - - - User Edit Menu:
 1 - Clear (blank) user password
(2 - Unlock and enable user account) [seems unlocked already]
 3 - Promote user (make user an administrator)
 4 - Add user to a group
 5 - Remove user from a group
 q - Quit editing user, back to user select
Select: [q] > 1
Password cleared!
================= USER EDIT ====================

RID     : 1000 [03e8]
Username: SystemUser
fullname: 
comment : 
homedir : 

00000220 = Administrators (which has 2 members)

Account bits: 0x0010 =
[ ] Disabled        | [ ] Homedir req.    | [ ] Passwd not req. | 
[ ] Temp. duplicate | [X] Normal account  | [ ] NMS account     | 
[ ] Domain trust ac | [ ] Wks trust act.  | [ ] Srv trust act   | 
[ ] Pwd don't expir | [ ] Auto lockout    | [ ] (unknown 0x08)  | 
[ ] (unknown 0x10)  | [ ] (unknown 0x20)  | [ ] (unknown 0x40)  | 

Failed login count: 0, while max tries is: 0
Total  login count: 44
** No NT MD4 hash found. This user probably has a BLANK password!
** No LANMAN hash found either. Try login with no password!

- - - - User Edit Menu:
 1 - Clear (blank) user password
(2 - Unlock and enable user account) [seems unlocked already]
 3 - Promote user (make user an administrator)
 4 - Add user to a group
 5 - Remove user from a group
 q - Quit editing user, back to user select
Select: [q] > 2
Unlocked!

```

Once we've opened the users up a bit, we need to save. 

```

What to do? [1] -> q

Hives that have changed:
 #  Name
 0  <../SAM>
Write hive files? (y/n) [n] : y
 0  <../SAM> - OK

```

Next we move on to makign the UI more usable. 

```

# ./chntpw -i ../SYSTEM
chntpw version 1.00 140201, (c) Petter N Hagen
Hive <../SYSTEM> name (from header): <SYSTEM>
ROOT KEY at offset: 0x001020 * Subkey indexing type is: 686c <lh>
File size 6291456 [600000] bytes, containing 1387 pages (+ 1 headerpage)
Used for data: 113449/5924568 blocks/bytes, unused: 3464/183240 blocks/bytes.



<>========<> chntpw Main Interactive Menu <>========<>

Loaded hives: <../SYSTEM>

      - - -
  9 - Registry editor, now with full write support!
  q - Quit (you will be asked if there is something to save)


What to do? [1] -> 9
Simple registry editor. ? for help.

> cd ControlSet001\Services\kbfilter\Parameters
\ControlSet001\Services\kbfilter\Parameters> ls
Node has 0 subkeys and 1 values
  size     type              value name             [value if type DWORD]
     4  4 REG_DWORD          <FilterEnable>             1 [0x1]

\ControlSet001\Services\kbfilter\Parameters> ed FilterEnable
EDIT: <FilterEnable> of type REG_DWORD (4) with length 4 [0x4]
DWORD: Old value 1 [0x1], enter new value (prepend 0x if hex, empty to keep old value)
-> 0x0
DWORD: New value 0 [0x0], 

\ControlSet001\Services\kbfilter\Parameters> q


> cd \ControlSet001\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile\AuthorizedApplications
> cd List
(...)\DomainProfile\AuthorizedApplications\List> ls
Node has 0 subkeys and 3 values
  size     type              value name             [value if type DWORD]
    78  1 REG_SZ             <S:\mxgfetcher.exe>
    78  1 REG_SZ             <S:\mxgdeliver.exe>
    78  1 REG_SZ             <S:\mxgcatcher.exe>

(...)\Parameters\FirewallPolicy\DomainProfile> ed EnableFirewall
EDIT: <EnableFirewall> of type REG_DWORD (4) with length 4 [0x4]
DWORD: Old value 1 [0x1], enter new value (prepend 0x if hex, empty to keep old value)
-> 0
DWORD: New value 0 [0x0], 

cd ..
cd StandardProfile
(...)\Parameters\FirewallPolicy\StandardProfile> ed EnableFirewall
EDIT: <EnableFirewall> of type REG_DWORD (4) with length 4 [0x4]
DWORD: Old value 1 [0x1], enter new value (prepend 0x if hex, empty to keep old value)
-> 0
DWORD: New value 0 [0x0], 


<>========<> chntpw Main Interactive Menu <>========<>

Loaded hives: <../SYSTEM>

      - - -
  9 - Registry editor, now with full write support!
  q - Quit (you will be asked if there is something to save)


What to do? [1] -> q

Hives that have changed:
 #  Name
 0  <../SYSTEM>
Write hive files? (y/n) [n] : y
 0  <../SYSTEM> - OK

```

Some other keys to consider looking at
REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f 
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\HideIcons

HideMyComputerIcons in HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WindowsEmbedded\ProductVersion

Cursor.cur needs replaced also. C:\windows\Cursors, download a new one from the internet

You can use http://registry-finder.com use the Find changes within date range feature to find the changes Sega made to the base system image. 

Please note: You may no longer need to have the *proper* / *original* security key in order to play the a drive. Don't be a dick... 
like others before today. Use this to back up your hardware for preservation sake, not for resale purposes! Keep your orignal key chips
on hand. If you sell the drive, sell the key chip with it. Don't sell rekeyed, or nokeyed drives. 

# Final Boss

"Someone know how we can change games inside a ringedge motherboard?"
http://www.neo-arcadia.com/forum/viewtopic.php?t=62415

Editing Niko's RE2Multi is very straight forward. Steps 1, 2, 3, 4 we should all be familiar with...

```
unlock multi drive with ata password
decrypt partition 7 with keyfile in C:\RE2Multi\re2multi.key
Copy 'Virtua Tennis 4' folder into Game folder. It should look and be structured like the others already, but double check. game.bat file is setup and ready to go.
dismount truecrpt partition
relock drive with ata sec pass (if you wish! or just cut power)
test in RE1
```
If you with to tamper with Niko's multi live you'll probably want the SystemUser password as well as Admin level privs. 

```
Download ms11-080-AddUser.exe
Copy to USB stick
Download mimikatz: https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20200502/mimikatz_trunk.zip
Unzip mimikatz onto USB stick
Boot re2multi
hit C to go to commmand prompt
Plug in USB stick
type: D:
type: ms11-080-AddUser.exe -O XP
cd into win32 mimikatz directory
type: runas /user:hacker mimikatz.exe
type: sekurlsa::kerberos
(press alt+spacebar, then E, then L, to scroll)
```
The password for SystemUser is <6/=U=#tpe!$*3!5

<Add notes on BIOS password here>

Have fun! Be safe!

Official video tutorial for the RingEdge SSD softmod by Mitsu (as usual!) can be found here: https://www.youtube.com/watch?v=l0nq1pQXX90


