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
As of Friday, March 31, 2017 at 27:59 The service has ended for “Puyo Puyo !! Quest Arcade” - http://puyoquest-am.blog.jp/archives/1063562161.html<br>
https://translate.google.com/#view=home&op=translate&sl=auto&tl=en&text=http%3A%2F%2Fpuyoquest-am.blog.jp%2Farchives%2F1063562161.html

<p align="center">
  <img src="http://livedoor.blogimg.jp/am_puyoquest/imgs/4/3/436f7037.jpg">
</p>

...

Additional text relevant to this document can be found below: 

Exemptions to Prohibition against Circumvention of Technological Measures Protecting Copyrighted Works – Seventh 
Triennial Section 1201 Final Rule, Effective October 28, 2018 https://library.osu.edu/document-registry/docs/1027/stream 
"Video games in the form of computer programs, where outside server support has been discontinued, to allow individual 
play and preservation by an eligible library, archive, or museum"

https://library.osu.edu/site/copyright/2019/03/20/2018-dmca-section-1201-exemptions-announced/ "Video games in the 
form of computer programs, lawfully acquired as complete games 37 CFR §201.40(b)(12)" "For personal, local gameplay; 
or To allow preservation in a playable format..."

Please note that the following text is considered "for purposes of good-faith security research".

For now some of this information will be further gatekept. 

This write up will absolutly however give you all the access you need to backup and preserve your RingEdge hardware featuring Puyo Puyo !! Quest Arcade. 

Please note that this preservation may apply to other devices, and games in the Ring* family such as RingEdge2, and RingWide. 

Please remember the wise words of Mitsurugi_w "The info itself is not new or special. It's all over the web anyways" 

# Stage Two:

For a long time the details of how Ring* game images are ReKeyed, or NoKeyed has been a closely guarded, and heavily traded 
/ paid for secret. With the first decade of deployment coming to a close, it is also time to close off this "Internet Money Maker". 
As hardware begins to fail, the threat of required preservation looms. 

-----

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

Cursor.cur needs replaced also. C:\windows\Cursors, download a new one from the internet

http://registry-finder.com use the Find changes within date range feature 

Please note: You may no longer need to have the *proper* / *original* security key in order to play the cloned drive. Don't be a dick... 
like others before today. Use this to back up your hardware for preservation sake, not for resale purposes! Keep your orignal key chips
on hand. If you sell the drive, sell the key chip with it. Don't sell rekeyed, or nokeyed drives. 

Have fun! Be safe!

Official video tutorial for the RingEdge SSD softmod by Mitsu (as usual!) can be found here: https://www.youtube.com/watch?v=l0nq1pQXX90


