Big thanks to Mitsurugi_w, Darksoft, and Brizzo of Arcade Projects for finally allowing this to be published.

- written by hostile, with supporting information from 

<p align="center">
<img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/walsdawg.jpeg"><img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/darksoft.jpeg">
</p>

<p align="center">
  <img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/arcadeprojects.jpeg"><img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/brizzo.jpeg">
</p>

# Stage One:

"【お知らせ】サービスを終了いたしました。"<br>
As of Friday, March 31, 2017 at 27:59 The service has ended for “Puyo Puyo !! Quest Arcade”<br>
http://puyoquest-am.blog.jp/archives/1063562161.html<br>
https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text=http%3A%2F%2Fpuyoquest-am.blog.jp%2Farchives%2F1063562161.html<br>

<p align="center">
  <img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/puyo.jpeg">
</p>

Christmas 2018 of course, brought this game back to life via the amazing "TeknoParrot 1.81 X-Mas Reveal".<br>
Unfortunately this restoration only for PC users as opposed to arcade operators. <br>
https://archive.org/download/Arcade-Sega-RingEdge-2018-12-23

"Sorry guy, didn't see you there!" https://www.youtube.com/watch?v=-ds4xRnI-b8

"Now it is time to take out my Santa bag, and give you presents" https://youtu.be/-ds4xRnI-b8?t=190

What about *actual* Ring hardware owners, and arcade operators in need? Have they been left out of the most recent TeknoParrot CoronaVirus (COVID-19) Update just the same? 

"Hello my friends, it seems that we are in the middle of a cross road, and now I have decided that I will enable all the RingEdge, RindEdge2, and RingWide cores on Teknoparrot, directly to public. Also if the entire internet dies because of coronavirus, I have given the archive and the source code to a few friends, expect an update. Good luck everybody." https://www.youtube.com/watch?v=lS3gSW3ZskQ

Meanwhile, on the *other* side of the interwebs:<br>
"We set out rules and people couldn't follow them. This new stuff is bringing too much drama."<br>
https://www.arcade-projects.com/forums/index.php?thread/12974-ringedge-help-section/&postID=210050#post210050

RIP Sega Ringedge, Ringwide and Nu subgroup on AP.<br>
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

The initial manifesto that Jackalus laid down is actually a great place to start... "Still you don't have the system, for example newer ring games have custom protector that works with the rootkits and only runs when everything is in order and only on original machine. You cannot attach debugger, most debuggers can't even see the process because of ring0 stuff, you cannot dump the process without ring0 methods and even then not easily, you cannot press alt+tab or use any key combination keys (Unless you know how to go around them). The windows protection is very complicated and strong, you are still just speculating here. It's not some jumps you patch to skip the dongle check. And it's not as simple as Taito Type X2 which was mostly a joke."

The subsequent rant about his work as a Jr Malware Researcher for F-Secure (https://www.linkedin.com/in/giansanti/) was as follows: "I have unpacked hundreds of custom malware packers, Commercial protections: Securom (Yes with VM Redirects, Opcode VM, Constant Hook Stealer etc), SafeDisk(+Nanomites), ASProtect SKE(+VM) blablabla. And when I tell you newer sega games have good protection, it really does have it. Sure you can clone it but emulation and running on PC is pretty much impossible without deprotecting the binary and emulating entire MX drivers/libraries."

It was implied that running Ring games on PC was less than favorable<br>
"I have already run Ring games on PC but it's gay" - Jackalus, Jun 19, 2013

4 years later under a new moniker, the tune changes a bit:<br>
"Core work done for RingEdge 2 support, currently disabled. (amAuth emulation)"<br>
"Changes TeknoParrot 0.4a Patreon Build" - May 29, 2017<br>
https://www.teknogods.com/viewtopic.php?t=38580

"TeknoParrot Patreon 0.4a out, have fun. #teknoparrot" - May 29, 2017
https://twitter.com/ReaverTeknoGods/status/869293180730081280

TeknoParrot currently supports emulation of a good chunk of the Ring library. 
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/Transformers.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/SRC.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/SDR.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/ProjectDiva.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/PPQ.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/MaiMaiGreen.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/OG.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/LGS.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/VT4.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/LGI3D.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/KODrive.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/ID8.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/ID7.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/ID6.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/GGXrd.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/MB.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/LGI.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/GG.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/FightingClimaxIgnition.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/UDX.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/PhantomBreaker.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/DOA5.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/CaladriusAC.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/SSASR.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/Mballblitz.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/CC.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/BorderBreakScramble.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/Koihime.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/GGXrdSIGN.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/FightingClimax.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/BladeArcus.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/UnderNightInBirth.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/GGXX.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/ArcadeLove.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/MeltyBloodRE2.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/ShiningForceCrossRaid.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/ShiningForceCrossExlesia.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/ShiningForceCrossElysion.json

"this is not the place to ask for neither for teknoparrot nor for roms."
https://www.arcade-projects.com/forums/index.php?thread/9093-greetings-from-uk/&postID=145048#post145048

At a certain point interest picked up on the Arcade Projects forums about the Ring based systems, eventually leading to the need to censor some of the commentary on the security mechanisms employed by Sega.  
"What can one do with a RingEdge?"
http://archive.is/wOIjp

Once folks in the "Ringedge/2/wide/Nu game list" thread heard "they can run locally and offline!", the thirst began. 
https://webcache.googleusercontent.com/search?q=cache:CiZlw8FpwmEJ:https://www.arcade-projects.com/forums/index.php%3Fthread/6466-ringedge-2-wide-nu-game-list/%26pageNo%3D2+&cd=1&hl=en&ct=clnk&gl=us

# Stage Three
Well after the dick wagging on Assembler Games a random technical examination of the RingEdge popped up:<br>
"I have purchased a ring edge that starts a game with a key-chip"<br>
"And SSD is such a rare item... It is locked by ATA's SECURITY lock, but if you UNLOCK it, you can access it from Windows as usual via USB-SATA bridge. Well, as I wrote the other day, there are unknown partitions."<br>
"SSD and key-chip are not tied to the motherboard. In other words, even if SSD and key-chip are moved to another ring edge, it will work"<br>
"Key-chip is linked to the game title. The game does not work even if the key-chip of another game is inserted while it is installed"<br>
http://d4.princess.ne.jp/diary/20158.html

"Basically it looks like a normal PC. As you can see from the actual specifications, it is an AT compatible machine. The motherboard looks like MS-9667, but there is no stamp"<br>
"key-chip communication is a rather troublesome process. I don't know the key-chip because I can't get it."<br>
"NTFS is a basic 3 partition configuration consisting of 2 partitions and an extended partition (content unknown). The first NTFS will bring up the RINGEDGE system. Of course, since there is no key-chip, it will stop with an error. The second is a system update. Probably an update of RINGEDGE itself. Maybe the game installation is also over here? The contents of the extended partition are completely unknown. Is it decrypted using the key of the key-chip?"<br>
http://d4.princess.ne.jp/diary/20157.html

"See someone abroad who said that the contents of the hard disk partition can be decrypted by hot plugging, but it is too risky to do this. I wonder if there is a great god who has studied this problem here?"<br>
"Encrypted, I am afraid it is not so easy to unlock"<br>
"But even if you extract it, you still have to modify the exe"<br>
https://club.tgfcer.com/thread-7148133-1-1.html

The partition layout is as follows.<br>
Partition 1 - \System\ (Boot Partition)<br>
Partition 2 - \MiniNT  (Recovery Partition)<br>
Partition 3 - 518 Meg  (?TrueCrypt? Partition)<br>
Partition 4 - 	       (Update Partition - TrueCrypt Protected)<br>
Partition 5 -          (? ? Partition)<br>
Partition 6 -          (? OS Drivers ? Partition)<br>
Partition 7 -          (Game Partition  - TrueCrypt Protected)<br>


https://elektrotanya.com/msi_ms-9667_rev_0b_sch.pdf/download.html<br>
MS9667_rev_0a_sch.pdf and MS9667_rev_0b_sch_RING_AALG.pdf exist seemingly confirming the suspicion about it being an MS9667 based PC.  

"The RingEdge BIOS will only boot a SSD that has the valid TDK RS2 signature on the ATA Identify structure and is locked and also needs to have the password calculated by the BIOS and bassed on that TDK RS2 signature"<br>
https://web.archive.org/web/20170628094958/https://www.assemblergames.com/threads/sega-ringedge-motherboard-inside-pictures.46424/page-2#post-681443

GBDriver RS2 - 2010. RS3 - 2011<br>
https://product.tdk.com/en/products/flash-storage/flashstorage-catalog_en.pdf

Serial-ATA-II Compatible NAND-Type Flash Memory Controller IC GBDriver RS2 Series
https://product.tdk.com/info/en/catalog/datasheets/ew_015_rs2.pdf

"SegaBoot generates the KeyFile for the TC container of the game on the fly, using the KeyChip, <br>
the process is really complex, but it generates a file on c:\windows\temp with the keyfile, <br>
then mounts the TC container and after the TC Container is successfully mounted deletes the <br>
Keyfile from C:\windows\temp, is just 2 minutes to pach that, is only a matter to remove the<br>
DeleteFile function from SegaBoot with simple NOPs and let SegaBoot to mount the game, then the<br>
Keyfile will be there on c:\windows\temp"<br>
https://web.archive.org/web/20170628094958/https://www.assemblergames.com/threads/sega-ringedge-motherboard-inside-pictures.46424/page-2#post-681449

"You might be able to just take off the delete permission from windows temp"<br>
https://web.archive.org/web/20170630214524/https://www.assemblergames.com/threads/sega-ringedge-motherboard-inside-pictures.46424/page-3#post-681518

"Its much more easy than that, just get a file access tool like filemon and see the parameters segaboot is giving to truecrypt, you will know where its storing the binary file that truecrypt uses as password to decrypt the partition"<br>
https://www.assembler-games.com/threads/sega-ringedge-motherboard-inside-pictures.46424/

As expected it did not take long for folks to start selling "bootleg" versions of Ring games that did not require a key. Sometimes refered to as "NoKey" games.<br>

"Topic: Initial D8 Server Ringedge (Original, No Bootleg!)", so wait, where is the bootleg one you made then? lol.<br>
http://www.ukvac.com/forum/initial-d8-server-ringedge-original-no-bootleg_topic367630.html

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

"Hi from inside of the great firewall."<br>
https://github.com/Woodu

It is unclear at this time where Woodu obtained his Ring* knowledge.<br>
"This site is not official SEGAJINWIN corp. website, is hosted by Woodu at China Arcade"
https://segajinwin.com

It is clear he's really obsessed with Sega Jinwin based arcade stuff. 
"Bought a new domain name"<br>
"Jingwen Sega really is a magic company."<br>
"I miss it very much."<br>
https://woodu.me/youxinmailegeyuming/

You can see the original Sega Jinwin site in on The Internet Archive<br>
https://web.archive.org/web/20130910052147/http://www.segajinwin.com/

"Established in 2009, Sega Jinwin (Shanghai) Amusement Co. Ltd is a joint-venture of Shanghai Jingwen Investment Co. Ltd., Japan Sega Corporation and affiliated company of China National Center for developing Animation, Cartoon & Game Industry."<br>
http://www.amusewind.com/catalog/all_ENTERPRISES/2012629/27_201262912749768_1.html

Woodu has many interesting Ring related things on his site<br>
"It has been a long time since I started doing maimai's magical reform in 15 years, and I haven't even put energy on it for a long time. But still did something a little above. What I can take out recently is that I started selling alternative hard drives for the mainframe. This is also the only relatively legal thing"<br>
https://woodu.me/author/woodu/

"SSD for Ringseries. Click here to buy"<br>
https://woodu.me/eryijiuniansanyue/<br>
Ringedge2 120G 固态硬盘 ¥300.00 - 599.00<br>
https://item.taobao.com/item.htm?id=586390733234<br>

"Sega's arcade platform began to completely transform into an X86 based architecture PC, which opened the door to cracking. It is no exaggeration to say that, in addition to the latest arcades such as Ship Mother, DIVA, and Chunithm, SEGA's games can be said to be lost across the board" https://woodu.me/2017/03/<br>
"This arcade is an arcade machine that has been represented in the era of Jingwen Sega. It is a full Chinese version, and there are still people selling it on Taobao."<br>

Totally NOT bootleg "Lost on Island of Tropics"<br>
"海岛探险游戏机"<br>
http://www.haoyunlaigame.com/arc/view-119.html

"Island Adventure" is a joyful and thrilling shooting game, inheriting the system of the classic shooting game "Let's go jungle", with wonderful stories, compact plots and fun and simple operations to perform wonderfully And a thrilling trip to the island." http://m.amunion.com/product/247889.html

In addition to bootlegs, you could occasionally find folks offering archival services, the conversation below exposes the concept of a rekey.  <br>

"if you want any RingWide game for RingEdge, i can supply you it on a 32Gbytes SSD remastered for work on RingEdge, but you need to have an original keychip on the RingEdge (any one, like MJ5 is ok)... Not, i don't do multi kits for RingEdge. Those Games are expensive like hell and very difficult to buy. I was talking about a single game on a 32GB SSD. Game not patched, still 100% original just remastered RingWide Game OS for work on a RingEdge."<br>
https://www.assembler-games.com/threads/is-it-possible-to-get-ringedge-to-run-ringwide-games.60346/#post-866358<br>
https://web.archive.org/web/20190403174837/https://assemblergames.com/threads/is-it-possible-to-get-ringedge-to-run-ringwide-games.60346/

Mahjong for example is SBVF a VERY easy to obtain KeyChip... wonder why so may shared images are keyed to it? ;)<br>
https://gakman.forumgaming.fr/t72-ringedge-ringwide#454

There was an effort at one point to document as many chip ID's as possible on AP forums. <br>
https://webcache.googleusercontent.com/search?q=cache:kfuo1iRQy3wJ:https://www.arcade-projects.com/forums/index.php%3Fthread/4456-ringedge-keychip-id/+&cd=1&hl=en&ct=clnk&gl=us

Modern times have finally brought forth conversations about a Ring* keychip emulator.<br>
https://github.com/ArcadeHustle/RingEdge_SSD_Softmod/issues/1

# Stage Four

"It's pretty very much illegal and too new for this site's content anyway."
https://webcache.googleusercontent.com/search?q=cache:kPxP6VQIhZYJ:https://www.arcade-projects.com/forums/index.php%3Fthread/10695-sega-ringedge-2-questions-on-obtaining-systems-disks-etc/%26pageNo%3D1+&cd=2&hl=en&ct=clnk&gl=us

Yet the whole time in private, Ring* drives were for sale like hotcakes via PM on AP... this little gem, a patched version of mxsegaboot and mxkeychip enabling it all. 
https://archive.org/details/mxsegaboot

So, yeah the big "secret" is just Truecrypt, as noted above. 
https://en.wikipedia.org/wiki/TrueCrypt

https://github.com/DrWhax/truecrypt-archive/blob/master/doc/Version-History.md
Specifically the Ring system makes use of TrueCrypt 4.3 in AES LRW mode for TrueCrypt containers, alongside a keyfile and password. 

This will help you determine which disk encryption programs are compatable with LRW if you wish to try mounting TC images that *hard* way, opposed to just using TrueCrypt 
https://wiki2.org/en/Comparison_of_disk_encryption_software

For what ever reason Ring* information is often censored quickly, and with malice. There are few remaining bits of archived information. Among them however are these gems:
Both of the archived poss contain partially usable instructions, but can indeed be worked out into a usable technique.
https://pastebin.com/zQYxBU1e
https://pastebin.com/2qiQdPQ6

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

You can mount TrueCrypt images, and drives within linux, either encrypted files, dd images (via losetup), or actual drive partitions. 

First you will need a workign TrueCrypt setup. In theory some versions of Veracrypt are also usable, but LRW support must be present. This should work on linux, but probably will NOT on OSX due to hdiutil being used on the backend. 

Fuse makes LRW work on versions past 4.x, so you'll need that too. https://forums.gentoo.org/viewtopic-t-688399-start-0.html

```
https://github.com/DrWhax/truecrypt-archive
https://github.com/DrWhax/truecrypt-archive/blob/master/doc/Version-History.md

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

```
$ mkdir /tmp/tc
$ sudo truecrypt -p segahardpassword -k SystemKeyFile System /tmp/tc

$ ls /tmp/tc
d3dref9.dll         lockid.txt      mxgdeliver.exe   mxkeychip.exe  mxsegaboot_2052.dll  mxstorage.exe        $RECYCLE.BIN
default_regset.txt  mxauthdisc.exe  mxgfetcher.exe   mxmaster.exe   mxsegaboot.exe       ORIG_mxkeychip.exe   ringmaster_pub.pem
develop_regset.txt  mxgcatcher.exe  mxinstaller.exe  mxnetwork.exe  mxshellexecute.exe   ORIG_mxsegaboot.exe  System Volume Information

$ truecrypt -d /tmp/tc

```

A patched version of TrueCrypt can be used to mount images on OSX Catalina 10.15 as described here: 
http://www.nerdenmeister.org/2013/08/16/build-truecrypt-on-os-x-64-bit-with-hardware-acceleration/
https://gist.github.com/neurodroid/7059368
A pre-patched version is located here, but you will need to modify the Makefile to make it work on Catalina
https://github.com/neurodroid/TrueCrypt

If you make use of Paragon NTFS modules for Mac you can also write content to the mounted images. \
https://www.paragon-software.com/us/home/ntfs-mac/

You will first need to install wxwidgets via brew! 

Alternately you can also mount TC drives on OSX using CipherShed, but you'll need to use the patches from TrueCrypt to make them work on modern OSX
https://webcache.googleusercontent.com/search?q=cache:rCoVjQzFDMoJ:https://wiki.ciphershed.org/BuildOnOSX+&cd=1&hl=en&ct=clnk&gl=us
Patched versions of the CipherShed and TrueCrypt repos are included in this git repo, ready to compile on OSX Cataline 10.15. 

```
$ mkdir /tmp/z; ./CipherShed-OSX-64/src/Main/CipherShed -t System_Pengo -k SystemKeyFile /tmp/z -p segahardpassword 
Protect hidden volume (if any)? (y=Yes/n=No) [No]: 
```

To unmount 
```
$ ./CipherShed-OSX-64/src/Main/CipherShed -d
```

You may be wondering at this point how exactly the KeyFile was obtained. There were bried notes in the pastebin links above, but we really need to go in depth. 

A number of academic articles on attacking TrueCrypt seem applicable, there was so much news hype on weaknesses within the platform. How do they play out in the real world? How do they impact Sega's implementation? 
Lets examine a few of the papers: 
Detecting the use of TrueCrypt - http://docs.media.bitpipe.com/io_10x/io_102267/item_885954/RH%203%20Davies.pdf
Error Correction and the Cryptographic Key - ftp://ftp.cs.princeton.edu/techreports/2011/897.pdf
This page contains source code for some of the software that we developed in the course of this research - https://citp.princeton.edu/our-work/memory/code
Security Analysis of TrueCrypt 7.0a with an Attack on the Keyfile Algorithm - https://cyberside.net.ee/truecrypt/misc/truecrypt_7.0a-analysis-en.pdf, https://cyberside.net.ee/truecrypt/misc/
Mastering TrueCrypt: Windows 8 and Server 2012 Memory Forensics - https://downloads.volatilityfoundation.org/omfw/2013/OMFW2013_Ligh.pdf
A Security Analysis of TrueCrypt: Detecting hidden volumes and operating systems - https://www.ma.rhul.ac.uk/static/techrep/2014/RHUL-MA-2014-10.pdf
#TrueCrypt PlaidCTF Writeup: Fun with Firewire - https://mweissbacher.com/tag/truecrypt
truecrypt second encryption of the master and XTS key with a back door password - https://security.stackexchange.com/questions/19764/truecrypt-second-encryption-of-the-master-and-xts-key-with-a-back-door-password
TrueCrypt Master Key Extraction And Volume Identification - https://volatility-labs.blogspot.com/2014/01/truecrypt-master-key-extraction-and.html

The following tools also provide intellectual reading on the subject at hand. 
tckfs: This tool seeks asynchronously TrueCrypt key file using combinations of provided key files with provided password. - https://github.com/Octosec/tckfc
Untrue: Tool for checking passwords against TrueCrypt encrypted volumes and disks, and/or decrypting the data. - https://github.com/nccgroup/Untrue
Master Key Decryptor: is a python script to assist with decrypting encrypted volumes using the recovered masterkey for various truecrypt type encrypted volumes. https://github.com/AmNe5iA/MKDecrypt
Truecrypt volume parsing library - https://github.com/4144414D/pytruecrypt

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

unlock multi drive with ata password
decrypt partition 7 with keyfile in C:\RE2Multi\re2multi.key
Copy 'Virtua Tennis 4' folder into Game folder. It should look and be structured like the others already, but double check. game.bat file is setup and ready to go.
dismount truecrpt partition
relock drive with ata sec pass (if you wish! or just cut power)
test in RE1

If you with to tamper with Niko's multi live you'll probably want the SystemUser password as well as Admin level privs. 

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

The password for SystemUser is <6/=U=#tpe!$*3!5

<Add notes on BIOS password here>

Have fun! Be safe!

Official video tutorial for the RingEdge SSD softmod by Mitsu (as usual!) can be found here: https://www.youtube.com/watch?v=l0nq1pQXX90


