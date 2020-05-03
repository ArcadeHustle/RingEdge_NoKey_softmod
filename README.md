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

Additional text relevant to this document can be found below: 

Exemptions to Prohibition against Circumvention of Technological Measures Protecting Copyrighted Works<br>
Seventh Triennial Section 1201 Final Rule, Effective October 28, 2018 <br>
https://library.osu.edu/document-registry/docs/1027/stream <br>
"Video games in the form of computer programs, where outside server support has been discontinued, to allow individual play and preservation by an eligible library, archive, or museum"

https://library.osu.edu/site/copyright/2019/03/20/2018-dmca-section-1201-exemptions-announced/ <br>
"Video games in the form of computer programs, lawfully acquired as complete games 37 CFR §201.40(b)(12)"<br> 
"For personal, local gameplay; or To allow preservation in a playable format..."<br>

Please note that the following text is considered "for purposes of good-faith security research".

This write up will give you all the knowledge, and access you need to backup and preserve your RingEdge hardware featuring Puyo Puyo !! Quest Arcade. 

Note that this preservation may apply to other devices, and games in the Ring* family such as RingEdge2, and RingWide. 

Please remember the wise words of Mitsurugi_w "The info itself is not new or special. It's all over the web anyways" 

# Stage Two:

For a long time the details of how Ring* game images are ReKeyed, or NoKeyed has been a closely guarded, and heavily traded / paid for secret. With the first decade of deployment coming to a close, it is also time to close off this "Internet Money Maker". As hardware begins to fail, the threat of required preservation looms. 

One of the earlier forum disucssions on the Ring* subject was found on Assembler games. Several known scene players can be seen waving their dicks around: <br><br>
"Get system, then come talk. This is why this information is not public because people who have no knowledge come to public and act like experts with no stripes."
https://web.archive.org/web/20170630214524/https://assemblergames.com/threads/sega-ringedge-motherboard-inside-pictures.46424/page-3

The initial manifesto that Jackalus laid down is actually a great place to start... "Still you don't have the system, for example newer ring games have custom protector that works with the rootkits and only runs when everything is in order and only on original machine. You cannot attach debugger, most debuggers can't even see the process because of ring0 stuff, you cannot dump the process without ring0 methods and even then not easily, you cannot press alt+tab or use any key combination keys (Unless you know how to go around them). The windows protection is very complicated and strong, you are still just speculating here. It's not some jumps you patch to skip the dongle check. And it's not as simple as Taito Type X2 which was mostly a joke."

The subsequent rant about his work as a Jr Malware Researcher for F-Secure (https://www.linkedin.com/in/giansanti/) was as follows: "I have unpacked hundreds of custom malware packers, Commercial protections: Securom (Yes with VM Redirects, Opcode VM, Constant Hook Stealer etc), SafeDisk(+Nanomites), ASProtect SKE(+VM) blablabla. And when I tell you newer sega games have good protection, it really does have it. Sure you can clone it but emulation and running on PC is pretty much impossible without deprotecting the binary and emulating entire MX drivers/libraries."

It was implied that running Ring games on PC were less than favorable<br>
"I have already run Ring games on PC but it's gay" - Jackalus, Jun 19, 2013

4 years later under a new moniker, the tune changes a bit... "Core work done for RingEdge 2 support, currently disabled. (amAuth emulation)" - Changes TeknoParrot 0.4a Patreon Build
TeknoParrot 0.4a PATREON - TeknoGods.com - May 29, 2017
https://www.teknogods.com/viewtopic.php?t=38580

TeknoParrot Patreon 0.4a out, have fun. #teknoparrot - May 29, 2017
https://twitter.com/ReaverTeknoGods/status/869293180730081280

TeknoParrot currently supports emulation of a good chunk of the Ring library. 
https://github.com/search?p=1&q=org%3Ateknogods+ring&type=Code
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/ShiningForceCrossRaid.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/ShiningForceCrossExlesia.json
https://github.com/teknogods/TeknoParrotUI/tree/master/TeknoParrotUi.Common/Descriptions/ShiningForceCrossElysion.json
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


# Stage Three

"The RingEdge BIOS will only boot a SSD that has the valid TDK RS2 signature on the ATA Identify structure and is locked and also needs to have the password calculated by the BIOS and bassed on that TDK RS2 signature"<br>
https://web.archive.org/web/20170628094958/https://www.assemblergames.com/threads/sega-ringedge-motherboard-inside-pictures.46424/page-2#post-681443

"SegaBoot generates the KeyFile for the TC container of the game on the fly, using the KeyChip, the process is really complex, but it generates a file on c:\windows\temp with the keyfile, then mounts the TC container and after the TC Container is successfully mounted deletes the Keyfile from C:\windows\temp, is just 2 minutes to pach that, is only a matter to remove the DeleteFile function from SegaBoot with simple NOPs and let SegaBoot to mount the game, then the Keyfile will be there on c:\windows\temp"<br>
https://web.archive.org/web/20170628094958/https://www.assemblergames.com/threads/sega-ringedge-motherboard-inside-pictures.46424/page-2#post-681449

"You might be able to just take off the delete permission from windows temp"
https://web.archive.org/web/20170630214524/https://www.assemblergames.com/threads/sega-ringedge-motherboard-inside-pictures.46424/page-3#post-681518

For what ever reason Ring* information is often censored quickly, and with malice. There are few remaining bits of archived information. Among them however are these gems:
https://pastebin.com/zQYxBU1e
https://pastebin.com/2qiQdPQ6

Both contain partially usable instructions, but can be worked out into a more usable technique.

```
# ./unlock.sh /dev/sdb 
Read 32 bytes from "file".

/dev/sdb:
 Issuing SECURITY_UNLOCK command, password="[read from file]", user=user

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

---------------
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



$ mkdir /tmp/tc
$ sudo truecrypt -p segahardpassword -k SystemKeyFile System /tmp/tc

$ ls /tmp/tc
d3dref9.dll         lockid.txt      mxgdeliver.exe   mxkeychip.exe  mxsegaboot_2052.dll  mxstorage.exe        $RECYCLE.BIN
default_regset.txt  mxauthdisc.exe  mxgfetcher.exe   mxmaster.exe   mxsegaboot.exe       ORIG_mxkeychip.exe   ringmaster_pub.pem
develop_regset.txt  mxgcatcher.exe  mxinstaller.exe  mxnetwork.exe  mxshellexecute.exe   ORIG_mxsegaboot.exe  System Volume Information

$ truecrypt -d /tmp/tc

---------------

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


----

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

...

What to do? [1] -> q

Hives that have changed:
 #  Name
 0  <../SAM>
Write hive files? (y/n) [n] : y
 0  <../SAM> - OK


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

REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f 
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\HideIcons

HideMyComputerIcons in HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\WindowsEmbedded\ProductVersion
```

Cursor.cur needs replaced also. C:\windows\Cursors, download a new one from the internet

http://registry-finder.com use the Find changes within date range feature 

Please note: You may no longer need to have the *proper* / *original* security key in order to play the cloned drive. Don't be a dick... 
like others before today. Use this to back up your hardware for preservation sake, not for resale purposes! Keep your orignal key chips
on hand. If you sell the drive, sell the key chip with it. Don't sell rekeyed, or nokeyed drives. 

"You can get it online without any restrictions, still it is delivered as an encrypted container, you should have a key."
http://www.emuline.org/topic/1836-under-night-in-birth-sega-ringedge-2-need-help-with-decrypting/?do=findComment&comment=67770

Have fun! Be safe!

Official video tutorial for the RingEdge SSD softmod by Mitsu (as usual!) can be found here: https://www.youtube.com/watch?v=l0nq1pQXX90


