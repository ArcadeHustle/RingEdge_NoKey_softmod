*Reminder, if you like these repos, fork them so they don't disappear* 
https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/fork

Big thanks to Mitsurugi_w, Darksoft, and Brizzo of Arcade Projects for finally allowing this to be published.
- written by hostile, with supporting information from the community at large!

<p align="center">
<img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/walsdawg.jpeg"><img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/darksoft.jpeg">
</p>

<p align="center">
  <img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/arcadeprojects.jpeg"><img src="https://github.com/ArcadeHustle/X3_USB_softmod/blob/master/brizzo.jpeg">
</p>

* [Stage One: Bye Bye Puyo Puyo!](#stage-one-bye-bye-puyo-puyo)
* [Stage Two: Early Ring history](#stage-two-early-ring-history)
* [Stage Three: Ring Piracy Deep Dive](#stage-three-ring-piracy-deep-dive)
	* [The Chinese Jinwin Sega connection?](#the-chinese-jinwin-sega-connection)
	* [Enter TrueCrypt](#enter-truecrypt)
* [Stage Four: Academic Exercises &amp; Censorship](#stage-four-academic-exercies--censorship)
	* [Unlocking the drive](#unlocking-the-drive)
	* [Mounting TrueCrypt containers](#mounting-truecrypt-containers)
	* [Obtaining the KeyFiles and Volume Password](#obtaining-the-keyfiles-and-volume-password)
	* [Modifying the OS boot image](#modifying-the-os-boot-image)
* [Final Boss: Changing games on Niko's Multi and other Ring platforms](#final-boss-changing-games-on-nikos-multi-and-other-ring-platforms)
	* [How to ReKey a Game drive to a new keychip](#how-to-rekey-a-game-drive-to-a-new-keychip)
	* [How to NoKey a drive](#how-to-nokey-a-drive)
	* [SystemUser privs on Nikos Multi and other Ring systems.](#systemuser-privs-on-nikos-multi-and-other-ring-systems)
	* [BIOS password](#bios-password)
* [Bonus level: RE2Multi on RE1?!](#bonus-level-re2multi-on-re1)

# Stage One: Bye Bye Puyo Puyo!

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
"Hello my friends, it seems that we are in the middle of a cross road, and now I have decided that I will enable all the RingEdge, RingEdge2, and RingWide cores on Teknoparrot, directly to public. Also if the entire internet dies because of coronavirus, I have given the archive and the source code to a few friends, expect an update. Good luck everybody."

Meanwhile, on the *other* side of the interwebs:<br>
"We set out rules and people couldn't follow them. This new stuff is bringing too much drama."<br>
https://www.arcade-projects.com/forums/index.php?thread/12974-ringedge-help-section/&postID=210050#post210050

Lets all pour out some liquor for the Sega Ringedge, Ringwide and Nu subgroup on AP, may it Rest In Peace!<br>
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

"Computer programs protected by dongles that prevent access due to malfunction or damage and which are obsolete. A dongle shall be considered obsolete if it is no longer manufactured or if a replacement or repair is no longer reasonably available in the commercial marketplace."
https://www.copyright.gov/fedreg/2006/71fr68472.html

"The final rule allows eligible libraries, archives, and museums to circumvent technological protection measures on certain lawfully acquired computer programs (including video games) to preserve computer programs and computer program-dependent materials."
https://clinic.cyber.harvard.edu/2018/10/26/a-victory-for-software-preservation-dmca-exemption-granted-for-spn/

"Exemption to Prohibition on Circumvention of Copyright Protection Systems for Access Control Technologies"
https://www.govinfo.gov/content/pkg/FR-2018-10-26/pdf/2018-23241.pdf

Please note that the following text is considered "for purposes of good-faith security research". This write up will give you all the knowledge, and access you need to backup and preserve your RingEdge hardware featuring Puyo Puyo !! Quest Arcade. This preservation may also apply to other devices, and games in the Ring* family such as RingEdge2, and RingWide. 

Please remember the wise words of Mitsurugi_w "The info itself is not new or special. It's all over the web anyways" 

# Stage Two: Early Ring history

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

Immediately after said rant, reaver implied that running Ring games on PC was less than favorable anyway, implying that the discussion was pointless. "I have already run Ring games on PC but it's gay" - Jackalus, Jun 19, 2013

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

# Stage Three: Ring Piracy Deep Dive
Well after the dick wagging on Assembler Games a random technical examination of the RingEdge popped up on Hiroyuki's home page (ひろゆきのホームページ):<br>
```
"I have purchased a ring edge that starts a game with a key-chip"
"And SSD is such a rare item... It is locked by ATA's SECURITY lock, but if you UNLOCK it, you can access it from Windows as usual via USB-SATA bridge. Well, as I wrote the other day, there are unknown partitions."
"SSD and key-chip are not tied to the motherboard. In other words, even if SSD and key-chip are moved to another ring edge, it will work"
"Key-chip is linked to the game title. The game does not work even if the key-chip of another game is inserted while it is installed"
```
http://d4.princess.ne.jp/diary/20158.html

ATA locks were a hurdle noted by other folks that were doing similar research into how the Ring* platform works.<br>
"The RingEdge BIOS will only boot a SSD that has the valid TDK RS2 signature on the ATA Identify structure and is locked and also needs to have the password calculated by the BIOS and bassed on that TDK RS2 signature"<br>
https://web.archive.org/web/20170628094958/https://www.assemblergames.com/threads/sega-ringedge-motherboard-inside-pictures.46424/page-2#post-681443

The manufacturing timeline for TDK GBDriver RS2 & RS3 indicates that the RS2 came out in 2010, and the RS3 in 2011. https://product.tdk.com/en/products/flash-storage/flashstorage-catalog_en.pdf

Documentation for the RS2 is located here:<br>
https://product.tdk.com/en/products/flash-storage/flashstorage-catalog_en.pdf<br>
"Serial-ATA-II Compatible NAND-Type Flash Memory Controller IC GBDriver RS2 Series"<br>

Documentation for the RS3 likewise can be found here:<br>
https://product.tdk.com/info/en/catalog/datasheets/ew_018_rs3.pdf<br>
"Serial ATA 3Gbps Compatible NAND-Type Flash Memory Controller IC GBDriver RS3 Series"

In the Sega Ring* plaftorm the RS2, and RS3 series drives provide support ATA drive locking functionality to prevent casual access, where as the drive encryption itself is actually handled by TrueCrypt. 

Bypassing the ATA lock is trivial, at this point the key has proliferated as: 7242525ABA526A5AEA726278CA42DA4A2A223A2A0A221A2A6A027A0A5CCE4A0A<br>

The ATA key can be acquired via commercial SATA analyzer, ghetto style SATA<->IDE Adapter+wirewrap+OpenBench, or even something along the lines of a firmware patched SSD based on OCZ Vertex / Jasmine hardware. 

<img src=https://blog.shackspace.de/wp-content/uploads/2011/04/DSC_2883.jpg>

"Open Sesame: Harddrive Password Hacking with a OpenBench Logic Sniffer"<br>
https://shackspace.de/2011/04/27/open-sesame-harddrive-password-hacking-with-a-openbench-logic-sniffer/<br>
https://hackaday.com/2011/04/28/ide-bus-sniffing-and-hard-drive-password-recovery/

"The Evil SSD Project - When your storage has a mind of its own"<br>
https://www.os3.nl/_media/2016-2017/courses/ot/martijn_yonne.pdf

See also the IRATEMONK example for ideas on how an SSD drive could be used to extract the calculated passwords presented by the Sega ATA unlock routines.<br> 
https://www.schneier.com/blog/archives/2014/01/iratemonk_nsa_e.html

None the less the ATA key has been public as early as 2018, and can be easily acquired even had it not been.
https://pastebin.com/2qiQdPQ6

Additional commentary on Hiroyuki's home page (ひろゆきのホームページ) offers a great starting point for research into Ring* security. 

```
"Basically it looks like a normal PC. As you can see from the actual specifications, it is an AT compatible machine. The motherboard looks like MS-9667, but there is no stamp"
"key-chip communication is a rather troublesome process. I don't know the key-chip because I can't get it."
"NTFS is a basic 3 partition configuration consisting of 2 partitions and an extended partition (content unknown). The first NTFS will bring up the RINGEDGE system. Of course, since there is no key-chip, it will stop with an error. The second is a system update. Probably an update of RINGEDGE itself. Maybe the game installation is also over here? The contents of the extended partition are completely unknown. Is it decrypted using the key of the key-chip?"
```
http://d4.princess.ne.jp/diary/20157.html

The disk encryption was something that confused folks at first, we obviously now know that it is based on TrueCrypt.
```
"See someone abroad who said that the contents of the hard disk partition can be decrypted by hot plugging, but it is too risky to do this. I wonder if there is a great god who has studied this problem here?"
"Encrypted, I am afraid it is not so easy to unlock"
"But even if you extract it, you still have to modify the exe"
```
https://club.tgfcer.com/thread-7148133-1-1.html

The mention of MS-9667 is intriguing, at first. Some of the early revisions of Ring* hardware still had this part number silk screened on the board, where as more modern variants including RingEdge 2 do not.<br>
"MSI foundry MS-9667 VER: 1.0 SEGA 775 professional repair of faulty motherboard"<br>
https://tw.bid.yahoo.com/item/【全國主機板維修聯盟】微星代工-MS-9667-VER-1-0-SEG-100693217459
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/MS9667.jpeg">

MS9667_rev_0a_sch.pdf and MS9667_rev_0b_sch_RING_AALG.pdf appear to be the schematic for the Sega MS9667 variant. 
https://elektrotanya.com/msi_ms-9667_rev_0b_sch.pdf/download.html<br>

Someone in China dumped the bios from this specific version citing a large number of deployed consoles in Panyu.<br>
"Dedicated anime game console motherboard BIOS, this motherboard BIOS is easy to break, upload it to everyone to repair this board, it is convenient" (file:SEGA MS-9667 rev1.0.zip)<br>
"I am here in Panyu, China's game console base, a large number of game console motherboard repair"<br>
https://www.chinafix.com/thread-991881-1-1.html

It should be noted that “the first criminal case in China involving an infringer of coin-op amusement games" occured in Panyu China. In the raid that took place at Chengtai factory in Panyu "10 suspected copies of complete Sega products" were seized. 
https://www.intergameonline.com/coin-op/news/counterfeit-megatouch-units-seized-in-china

This same company was later dismantled, along with it's conterfeit games. 
"In the ruling, Chengtai Electronics Science and Technology Company was found to have violated trademark laws, while also sustaining illegal business operations charges."
https://www.intergameonline.com/coin-op/news/china-sues-merit-game-thieves

### The Chinese Jinwin Sega connection? 
"Sega's arcade platform began to completely transform into an X86 based architecture PC, which opened the door to cracking. It is no exaggeration to say that, in addition to the latest arcades such as Ship Mother, DIVA, and Chunithm, SEGA's games can be said to be lost across the board... This arcade is an arcade machine that has been represented in the era of Jingwen Sega. It is a full Chinese version, and there are still people selling it on Taobao."<br>
https://woodu.me/2017/03/<br>

The machine mentioned above is found here... it is a totally NOT bootleg "Lost on Island of Tropics" ("海岛探险游戏机"). "Island Adventure" is a joyful and thrilling shooting game, inheriting the system of the classic shooting game "Let's go jungle", with wonderful stories, compact plots and fun and simple operations to perform wonderfully And a thrilling trip to the island."<br>
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/bootleg.jpeg">
http://www.haoyunlaigame.com/arc/view-119.html<br>
http://www.amunion.com/product/247889.html<br>
http://www.haoyunlaigame.com/arc/view-119.html<br>
https://youtu.be/ipwE6E6xrPw?t=45

"SEGA is giving up China market.The JingWen Sega co,ltd has closed at earlier this year,a music game needs frequently update.We have no choice. If nothing unexpected happens,this will be the last update of Wumeng(Chinese version MaiMai).The MaiMai overseas (Version Green) has periodic update per week and the program is totally different to the mainland China version.We cannot get updates and the company has gone.So we find help for carck it."<br>
https://web.archive.org/web/20190404164948/https://assemblergames.com/threads/pc-based-arcade-games.42102/page-3#post-745386

One of the first public examples of bootlegging was actually a Chinese Operation Ghost Nokey.<br>
"I've got a RINGEDGE cabient and game is OPERATION GHOST but it seems be a Chinese bootleg don't need the key chip and make me awesome... I want to unplug the SSD driver and explore the game file, but it also a gbdriver rs3, and has encrypted." -  Nov 15, 2015<br>
http://archive.is/M1hvR

"Here I have a Simplified Chinese version music game called MaiMai running on RingEdge2 platform. In order to avoid the spam detector please send me a message if you want to get the raw iso data. We tried to make a copy of this disk but failed.If you have tools to decrypt it , please tell us."<br>
https://web.archive.org/web/20190404164948/https://assemblergames.com/threads/pc-based-arcade-games.42102/page-3#post-745324

"MaiMai Green (another version than supported by teknoparrot. That one is the Chinese bootleg ?)"
http://www.emuline.org/topic/1696-arcade-pc-maimai-finale-sega-ringedge/?do=findComment&comment=60218

There were also a few interesting hardware *leaks* from the Chinese sega Factory: "the guy who send this to me is at the factory... The seller sells many ODM motherboards,including Ringedge and Lindbergh boards.and he called me and send this to me today earlier. Anyone knows what's this?"<br>
https://assembler-games.com/threads/so-recently-i-got-a-strange-board-from-a-factory-which-makes-sega-boards.57620/#post-825992

Much of the information above came from Woodu a seemingly random Chinese Sega entheusiast, it is unclear at this time where he obtained his Ring* knowledge.<br>
"Hi from inside of the great firewall" https://github.com/Woodu

What is clear is that he's really obsessed with Sega Jinwin based arcade stuff!<br> 
"Bought a new domain name"<br>
"Jingwen Sega really is a magic company."<br>
"I miss it very much."<br>
"This site is not official SEGAJINWIN corp. website, is hosted by Woodu at China Arcade".<br>
https://woodu.me/youxinmailegeyuming/<br>
https://segajinwin.com

You can see the original Sega Jinwin site in on The Internet Archive<br>
https://web.archive.org/web/20130910052147/http://www.segajinwin.com/

So what is JingWin Sega? It was "Established in 2009, Sega Jinwin (Shanghai) Amusement Co. Ltd is a joint-venture of Shanghai Jingwen Investment Co. Ltd., Japan Sega Corporation and affiliated company of China National Center for developing Animation, Cartoon & Game Industry."<br>
http://www.amusewind.com/catalog/all_ENTERPRISES/2012629/27_201262912749768_1.html

Beyond his general love for Sega Woodu has many interesting Ring related things on his site, such as replacement drives for the Ring series. 
"It has been a long time since I started doing maimai's magical reform in 15 years, and I haven't even put energy on it for a long time. But still did something a little above. What I can take out recently is that I started selling alternative hard drives for the mainframe. This is also the only relatively legal thing"<br>
https://woodu.me/author/woodu/

"SSD for Ringseries. Click here to buy"<br>
https://woodu.me/eryijiuniansanyue/<br>
Ringedge2 120G 固态硬盘 ¥300.00 - 599.00<br>
https://item.taobao.com/item.htm?id=586390733234<br>

### Enter TrueCrypt
The nuances of TrueCrypt on Ring* platform have been a heavily censored topic, although not a complicated one at it's root. In essence you need to acquire both the keys and password to the TrueCrypt containers that you wish to access. Both tasks are fairly trivial at the end of the day.  

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

Mahjong for example has a KeyChip ID of SBVF, and it is a VERY easy to obtain KeyChip... I wonder why so many shared images are rekeyed to it? https://gakman.forumgaming.fr/t72-ringedge-ringwide#454

There was an effort at one point to document as many chip ID's as possible on AP forums, this sort of effort is extremely useful for archival of all known KeyChips. <br>
https://webcache.googleusercontent.com/search?q=cache:kfuo1iRQy3wJ:https://www.arcade-projects.com/forums/index.php%3Fthread/4456-ringedge-keychip-id/+&cd=1&hl=en&ct=clnk&gl=us

If we come full circle to modern times, folks have finally brought forth conversations about a Ring* keychip emulator. This sort of concept has been deployed in private for quite some time by various players.<br>
https://github.com/ArcadeHustle/RingEdge_SSD_Softmod/issues/1

# Stage Four: Academic Exercies & Censorship

Clearly folks have been profiting off the NoKey, and ReKey image instances, both in the form of Chinese Bootleg machines and their accompanying hardware as well as individual private sales. Discussion about the techniques employed have been forbidden fruit for quite some time, partially due to these profit motives. The guise has always been *fear* of Sega retaliating... 

"It's pretty very much illegal and too new for this site's content anyway."
https://webcache.googleusercontent.com/search?q=cache:kPxP6VQIhZYJ:https://www.arcade-projects.com/forums/index.php%3Fthread/10695-sega-ringedge-2-questions-on-obtaining-systems-disks-etc/%26pageNo%3D1+&cd=2&hl=en&ct=clnk&gl=us

Yet the whole time in private, Ring* drives were for sale like hotcakes via PM on AP... this little gem, a patched version of mxsegaboot and mxkeychip enabling it all. 
https://archive.org/details/mxsegaboot

So, yeah the big "secret" is just Truecrypt, as noted above. https://en.wikipedia.org/wiki/TrueCrypt

Specifically the Ring system makes use of TrueCrypt 4.3 in AES LRW mode for TrueCrypt containers, alongside a keyfile and password. This is coupled with a standard ATA lock as mentioned above. 
https://github.com/DrWhax/truecrypt-archive/blob/master/doc/Version-History.md

### Unlocking the drive

Historically drive access has been gained without the need for the ATA unlock key due to the usage of the "Hot Swap" technique. 
The process will not be outlined here due to the simplicity, and because it was already proliferated during the ramp up of the original Xbox hacking scene. Simply apply the same process to your Ring* platform hard drives.<br>

"This is not a suggested method, but it has been known to work. The idea is that you start the Xbox and wait for the dashboard, at which point the drive will be unlocked. Then, while the Xbox is running, you disconnect the IDE cable (but not the power!), and then connect the drive to your PC. Then the drive can be mounted for read/write (using XboxHDM), or imaged directly."
https://xboxdevwiki.net/Hard_Drive#Unlocking_for_Backups

For what ever reason Ring* information is often censored quickly, and with malice. There are few remaining bits of archived information. Among them however are these gems:
Both of the archived posts contain partially usable instructions, but can indeed be worked out into a usable technique if you pay close attention.
https://pastebin.com/zQYxBU1e<br>
https://pastebin.com/2qiQdPQ6

The first bit of information revealed in the posts was the static ATA unlock key for the TDK RS2 and RS3 hard drives use by default in Ring* machines. A simple hdparm command will unlock the drive, and allow you to interact with it. As mentioned previously even without the pastebin posts the ATA key is trivial to obtain via a number of methods. 

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

On OSX the partition layout is as follows:
```
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *32.0 GB    disk5
   1:               Windows_NTFS Untitled                1.1 GB     disk5s1
   2:               Windows_NTFS Untitled                1.1 GB     disk5s2
   3:                 DOS_FAT_16                         542.8 MB   disk5s5
   4:                 DOS_FAT_16                         1.1 GB     disk5s6
   5:                 DOS_FAT_16                         1.1 GB     disk5s7
   6:               Windows_NTFS SBWA                    353.7 MB   disk5s8
   7:                 DOS_FAT_16                         2.9 GB     disk5s9
```

Several partitions are simply mountable as standard NTFS drives. 
```
$ mount  | grep disk5
/dev/disk5s1 on /Volumes/Untitled 1 (ufsd_NTFS, local, nodev, nosuid, noowners)
/dev/disk5s2 on /Volumes/Untitled 2 (ufsd_NTFS, local, nodev, nosuid, noowners)
/dev/disk5s8 on /Volumes/SBWA (ufsd_NTFS, local, nodev, nosuid, noowners)
```

The mounted partitions give us an idea of what is on the drive layout. 
```
$ ls /Volumes/Untitled\ 1/
$RECYCLE.BIN			System
Documents and Settings		System Volume Information
NTDETECT.COM			WERUNTIME.INI
Program Files			WINDOWS
RECYCLER			boot.ini
RHDSetup.log			ntldr

$ ls /Volumes/Untitled\ 2/
$RECYCLE.BIN			System Volume Information
Minint				WERUNTIME.INI
NTDETECT.COM			ntldr
RecoverOSVersion.txt

$ ls /Volumes/SBWA/
$RECYCLE.BIN			System Volume Information
```

In this case the drive is a RingWide Operation Ghost image. SBWA as seen in the mount path is the keychip ID. 
http://tms-designs.com/THESHED/default.asp?stockid=168955560

To mount the other partitions, first you will need a working TrueCrypt setup of some sort, either the original, or a fork. In theory some versions of Veracrypt are usable, but LRW support must be present, your best bet is the Linux version. 
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

Here is an example of how to mount the container found on the boot partition in \System\Execute\System with TrueCrypt on Linux:
```
$ mkdir /tmp/tc
$ sudo truecrypt -p segahardpassword -k SystemKeyFile System /tmp/tc

$ ls /tmp/tc
d3dref9.dll         lockid.txt      mxgdeliver.exe   mxkeychip.exe  mxsegaboot_2052.dll  mxstorage.exe        $RECYCLE.BIN
default_regset.txt  mxauthdisc.exe  mxgfetcher.exe   mxmaster.exe   mxsegaboot.exe       ORIG_mxkeychip.exe   ringmaster_pub.pem
develop_regset.txt  mxgcatcher.exe  mxinstaller.exe  mxnetwork.exe  mxshellexecute.exe   ORIG_mxsegaboot.exe  System Volume Information

$ truecrypt -d /tmp/tc

```

Here is the same example with CipherShed on OSX:
```
$ mkdir /tmp/z; ./CipherShed-OSX-64/src/Main/CipherShed -t System_Pengo -k SystemKeyFile /tmp/z -p segahardpassword 
Protect hidden volume (if any)? (y=Yes/n=No) [No]: 

$ ./CipherShed-OSX-64/src/Main/CipherShed -d
```

After mounting the file based container, move on and mount some of the partitions on the physical drive. 

This is the current documented understanding of the final partition layout. 
```
disk5
disk5s1 - (Boot Partition, \System\Execute\System container w/ SystemKeyFile)
disk5s2 - (Recovery Partition, \MiniNT)
        - (Extended Partition)
disk5s5 - (OS Update Partition - TrueCrypt)
disk5s6 - (unknown)
disk5s7 - (unknown)
disk5s8 - (Keychip ID partition, unclear what this is for)
disk5s9 - (Game Partition - TrueCrypt w/ GameKey)
```

### Obtaining the KeyFiles and Volume Password
You may be wondering at this point how exactly the KeyFiles are obtained. There were brief notes in the pastebin links above for one technique, but we really need to go in depth into how TrueCrypt on the Ring* platform can be attacked for academic posterity at the very least. 

<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/ADS.jpeg">

If you are not familiar with Alternate Data Streams on NTFS you will want to start here, because Sega chose to store the initial System and Update partition TrueCrypt keys in a hidden ADS stream right off the root of the drive in C:\System\Execute\DLL<br>
"Practical Guide to Alternative Data Streams in NTFS"<br>
http://www.irongeek.com/i.php?page=security/altds

"The NTFS file system provides applications the ability to create alternate data streams of information. By default, all data is stored in a file's main unnamed data stream, but by using the syntax 'file:stream', you are able to read and write to alternates." https://docs.microsoft.com/en-us/sysinternals/downloads/streams

From either a linux or Mac system we can view the streams via ls, or xattr
```
$ man ls
LS(1)                     BSD General Commands Manual                    LS(1)
...
     -@      Display extended attribute keys and sizes in long (-l) output.<br>
```

The first step both examining, and extracting the encrypted contents of a mounted RingEdge drive via OSX are shown below. Specifically the C:\System\Execute\DLL folder holds ADS streams containing the key files needed to mount both the C:\System\Execute\System file, and the Update partition on a Ring Game drive. You will need to extract them to make use of them. 
```
$ ls -l@  /Volumes/Untitled\ 1/System/Execute/
total 25194
drwxr-xr-x@ 0 mitsurugi  staff         0 Apr 29  2009 DLL
	SystemKeyFile	      53 
	UpdateKeyFile	      16 
-rwxr-xr-x  1 mitsurugi  staff  12582912 Dec 17  2008 System
-rwxr-xr-x  1 mitsurugi  staff    138240 Aug  7  2009 mxprestartup.exe
-rwxr-xr-x  1 mitsurugi  staff    178176 Aug  7  2009 mxstartup.exe

$ xattr-2.7 DLL
SystemKeyFile
UpdateKeyFile

$ xattr-2.7 -l DLL
SystemKeyFile: adsaf21519189aq1g56161asdff19as1f9:PF:CA[][_159191wef
UpdateKeyFile:
00000000  88 C2 DE 33 46 D1 B1 12 BC A1 F7 3F 94 2C DF 38  |...3F......?.,.8|
00000010

$ xattr-2.7 -p SystemKeyFile DLL/
adsaf21519189aq1g56161asdff19as1f9:PF:CA[][_159191wef

$ xattr-2.7 -p UpdateKeyFile DLL
88 C2 DE 33 46 D1 B1 12 BC A1 F7 3F 94 2C DF 38

$ xattr-2.7 -p UpdateKeyFile DLL | xxd -r -p | xxd
00000000: 88c2 de33 46d1 b112 bca1 f73f 942c df38  ...3F......?.,.8

$ xattr-2.7 -p UpdateKeyFile DLL | xxd -r -p > UpdateKeyFile
$ xxd UpdateKeyFile 
00000000: cc51 bae8 4a5e 00ff 461c 8d45 d4e8 6a42  .Q..J^..F..E..jB

```

The contents of the UpdateKeyFile have not been shared with the public in the past, however the SystemKeyFile has, without instruction on how to extract it as we've shown above. You can do the same process on windows via Nirsoft
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/ADS1.jpeg">
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/ADS2.jpeg">
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/ADS3.jpeg">
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/ADS4.jpeg">
This is only the first step, and it doesn't even net you access to the game partition. Quite the contrary, it only grants access to the programs that retrieve the game container TrueCrypt key from the physical hardware key. In other words, now that the first hurdle has been completed, the second shows its head. 

Once the SystemKeyfile has been obtained it can be coupled with a hardcoded mount password ("segahardpassword") that can be found within the same binary, and subsequently used to mount the associated TrueCrypt container file "System" inside of "C:\System\Execute".  
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/MountSystemPartitionSegaHardPass.png">

You can see from the disassembly that different keys are used at different times to mount volumes. 
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/MountUpdatePartition.png">
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/SilentMountHiddenDriveWithKey.png">

In order to get the game keys, we will need to understand where they come from, or alternately where they go. With the System container mounted we can begin to explore, we do know ultimately that both the key file and password are passed on to TrueCrypt as arguments. We can absolutly take advantage of that fact to our advantage to make dumping keys easy.   

Hint: The technique most folks use involves patching Sega mx* binaries to not delete files that are placed in the windows TEMP folder. During key generation the TrueCrypt keys that are derived from KeyChip interrogation are temporarily placed in C:\Windows\TEMP via mkstemp(), and subsequently deleted. The pastebin links shared above walk through a clunky process by which the files can be retrieved. This previously shared technique that has proliferated into the community involves patching DeleteFileA() inside of mxsegaboot.exe so that the resulting file can be collected from the TEMP folder. 

<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/DeletefileA.png">

We find it simpler to patch TrueCrypt to dump the keyfile and pass. TrueCrypt.exe does after all sit on a nonprotected portion of the file system. You can simply copy the patched files onto the game drive, and reboot to dump the keys.<br>
https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/TrueCrypt-win32_keydump.patch<br>
https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/tree/master/TrueCrypt-win32_keydump (binaries)

<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/BackdooredTrueCrypt.png">

<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/dumpedkey.png">

You should also note how geminifs is used to create symbolic links across the various mounted containers before presenting them for the game launch. 
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/UnmountTC.png">

<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/fsutil.jpeg">

The commentary linked below will examine an alternate path to mounting an encrypted TC drive, via stolen TrueCrypt master keys. This is post memory acquisition based technique that is generally outside the scope of this writeup. It has been included for academic posterity with regard to attacking TrueCrypt based systems.
https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/MemoryForensics.md

### Modifying the OS boot image

Regardless of how you obtained the various keys, once you get the ATA key entered, and the drive unlocked mounted, you can begin modifying the system. The core OS can be made more friendly for casual research, or other non gaming uses with a few registry edits. 

You can use Registry Finder from http://registry-finder.com to the find registry changes within a certain date range which will make the changes Sega made to the base system image stick out like a sore thumb. 

First we need to download chntpw, then as a sanity check we will use it to list the users on the system. 
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

Next we move on to making the UI more usable, by disabling the firewall, and kbfilter settings.  

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

There are a number of other keys to consider looking at in making your experience more usable for reverse engineering. 
```
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System\DisableTaskMgr
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\HideIcons
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\HideMyComputerIcons
```

If you are curious about the exact version of Windows used you can also take a quick look at the following key. 
```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WindowsEmbedded\ProductVersion
```

Finally perhaps the most annoying thing that needs changed, is the 1x1 pixel Cursor file that Sega chose to use to obfuscate the UI. C:\windows\Cursors\Cursor.cur will need to be deleted, and replaced with something more usable. (what happens if we just delete it? does it revert to a standard cursor?)

# Final Boss: Changing games on Niko's Multi and other Ring platforms

"Someone know how we can change games inside a ringedge motherboard?"<br>
http://www.neo-arcadia.com/forum/viewtopic.php?t=62415

The easy answer to the question above is to simply make use of Niko's Multi by editing it to suit your needs. Editing Niko's RE2Multi is very straight forward. At this point all the required steps should be familiar. 

```
1. Unlock Niko's multi drive with the ata password that you used to create it
2. Decrypt partition 7 with keyfile in C:\RE2Multi\re2multi.key
3. Copy a named game folder such as 'Virtua Tennis 4' into the Game folder. 
4. Make sure your game is structured like the others already.
5. Ensure that game.bat file is setup and ready to execute.
4. Unmount the game partition TrueCrypt container. 
5. Relock drive with ata password, or if you wish in some cases you can just cut power, and wait for a moment. 

Known Drive Keys:
PNY CS900 120GB SSD - (SSD7CS900-120-RB) Key: 0242826a1253ca5bf242ea78d263524ab213d22a0a460be66a467f865c8a5a86
Inland Professional 120GB SSD - (4335233676) Key: 324152498a530248ea42fa4aca42da4a2a223a2a0a221a2a6a027a0a4a025a0a
Crucial BX500 120GB SSD - (CT120BX500SSD1) Key: 3250aa589242b259f273627b2273da4a2a223a2a0a221a2a6a026b6e5bce4b86
TDK RS2, RS3 SSD - (OEM Sega) Key: 7242525ABA526A5AEA726278CA42DA4A2A223A2A0A221A2A6A027A0A5CCE4A0A
```

### How to ReKey a Game drive to a new keychip

This is simply a matter of using the built in TrueCrypt key functionality. <br>
"Volumes -> Add/Remove Keyfiles to/from Volume... This function allows you to re-encrypt a volume header with a header encryption key derived from any number of keyfiles (with or without a password), or no keyfiles at all. Thus, a volume which is possible to mount using only a password can be converted to a volume that require keyfiles (in addition to the password) in order to be possible to mount... This function can also be used to change/set volume keyfiles (i.e., to remove some or all keyfiles, and to apply new ones)."<br>
https://www.truecrypt71a.com/documentation/keyfiles/

Open up TrueCrypt, and adjust the keys as you see fit. Have an old Mahjong key that you want to use on another drive? Dump it using the patched TrueCrypt executables that were shared above, and then add the dumped key to the game container partition that you wish to use it with. 

### How to NoKey a drive

For now the inner workings of how the KeyChip emulators work will be left as an exercise for the reader, with access to Niko's multi image, and this document you have all you need to begin your studies. It should be fairly obvious that you don't need to understand how they work to successfully use them as replacements for existing mx* binaries. 

$ vbindiff mxsegaboot.exe ORIG_mxsegaboot.exe 
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/vbindiff.png">

Funny what the power of one little byte change can help lead to. 
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/compare.png">

Note the subtle difference in the build version on the original file, and its patched up replacement for this specific image? Completely different build versions are used. 

$ vbindiff mxkeychip.exe ORIG_mxkeychip.exe 
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/compare4.png">

It doesn't take a genius to figure out what is going on considering only mxsegaboot.exe and mxkeychip.exe are replaced. 

### SystemUser privs on Nikos Multi and other Ring systems. 
If you wish to tamper with Niko's as it runs live, you'll probably want the SystemUser password as well as Administrative level privleges. The password can be obtained by exploiting a kernel level vulnerability, and subsequently running MimiKatz. 

```
1. Download ms11-080-AddUser: https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS11-080
2. Copy ms11-080-AddUser.exe to USB stick
3. Download mimikatz: https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20200502/mimikatz_trunk.zip
4. Unzip mimikatz onto USB stick
5. Boot re2multi
6. hit C to go to commmand prompt
7. Plug in USB stick
8. type: D:
9. type: ms11-080-AddUser.exe -O XP
10. cd into win32 mimikatz directory
11. type: runas /user:hacker mimikatz.exe, and enter password Hacker!
12. type: sekurlsa::kerberos
```
The password for SystemUser is <6/=U=#tpe!$*3!5
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/MimiKatz.jpeg">

### BIOS password

#### RingWide
Currently unknown

#### RingEdge 1
Typing ctrl+alt+7 as the Ring* boots will get you a bios prompt. To obtain the BIOS password simply enter an incorrect password three times, within Phoenix TrustedCore(tm) Setup Utility. Notate the code that is displayed, because it is actually a checksum that can be used to derive the bios password. 
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/hash.png">

Two known passwords are: ynruq, and kalcj

These BIOS nuances are documented in a number of articles: 
"BIOS Password Backdoors in Laptops" 
https://dogber1.blogspot.com/2009/05/table-of-reverse-engineered-bios.html
https://281eaff2-a-62cb3a1a-s-sites.googlegroups.com/site/dogber1/blag/pwgen-5dec.py
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/biosbrute.jpeg">

The website for bios-pw.org is known to work for extracting the passwords if you are in a hurry. Their source code is shared here: https://github.com/bacher09/pwgen-for-bios

#### RingEdge 2
A completely different BIOS is used on RE2, so the above technique does not apply. 


# Bonus level: RE2Multi on RE1?!

There are basically two drivers that need to be installed on the RE2Multi image to make it work on RE1. These drivers are already present on Niko's multi in the following folders:<br>
C:\Program Files\NVIDIA Corporation\Drs\ 
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/nvidia.png">

C:\WINDOWS\system32\DRVSTORE\mxsram_84E083611D520D67EB8997E30D46709A4946EAF3\
<img src="https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/blob/master/pics/mxsram.png">

A "patch" in the form of a .zip file that can be uncompressed on Niko's multi can be found here:<br>
https://archive.org/details/niko-multi-re-1-c-drive-patch

Alternately you can find the proper installers for these drivers on the OSUpdate partition. 

Prepatched 32Gb versions of Niko's Multi Image that check for game files on a secondary drive can be downloaded from the Internet Archive: 
https://archive.org/details/re1multi32gb

No games are included, and the orignal TDK RS2, and RS3 drives can be used as a means to preserve original hardware. No new purchases are necessary. 

Most games work fine on either platform, however some games like DOA5 will require extra RAM. Other games for RingWige, and RingEdge should work fine as well, some however may require special IO boards, or other hardware like TrackBall's to work properly. 

You may also want to read the sister writeup: "Sega Ring[Edge*|Wide] alternate SSD softmod. Need a cloned drive? No problem..."
https://github.com/ArcadeHustle/RingEdge_SSD_Softmod

Have fun! Be safe!

Please note: You may no longer need to have the *proper* / *original* security key in order to play a Ring* platform game drive. Don't be a dick... like others before today. Use this to back up your hardware for preservation sake, not for resale purposes! Keep your orignal key chips on hand. If you sell the drive, sell the key chip with it. Don't sell rekeyed, or nokeyed drives. 

Questions should be submitted as git issues https://github.com/ArcadeHustle/RingEdge_NoKey_softmod/issues, or directed at Mitsurugi_w, or Darksoft on Arcade Projects via private message<br>
https://www.arcade-projects.com/forums/index.php?user/3-mitsurugi-w/<br>
https://www.arcade-projects.com/forums/index.php?user/1-darksoft/<br>

Official video tutorial for the RingEdge NoKey / ReKey / AddKey softmod by Mitsu (as usual!) can be found here: https://www.youtube.com/watch?v=l0nq1pQXX90



