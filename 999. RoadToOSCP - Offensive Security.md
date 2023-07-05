
# BASH SHELL

>**Bash** is a [Unix shell](https://en.wikipedia.org/wiki/Unix_shell "Unix shell") and [command language](https://en.wikipedia.org/wiki/Command_language "Command language") written by [Brian Fox](https://en.wikipedia.org/wiki/Brian_Fox_(computer_programmer) "Brian Fox (computer programmer)") for the [GNU Project](https://en.wikipedia.org/wiki/GNU_Project "GNU Project") as a [free software](https://en.wikipedia.org/wiki/Free_software "Free software") replacement for the [Bourne shell](https://en.wikipedia.org/wiki/Bourne_shell "Bourne shell"). First released in 1989, it has been used as the default [login](https://en.wikipedia.org/wiki/Login "Login") shell for most [Linux](https://en.wikipedia.org/wiki/Linux "Linux") distributions.[](https://en.wikipedia.org/wiki/Bash_(Unix_shell)#cite_note-zsh2-15)

## Important commands #bash_commands 
- ***Wifi password for Ethernet connection*** ls /etc/NetworkManager/system-connections
	- sudo cat /etc/NetworkManager/system-connections/`Name_of_the_connection`
- nmcli device wifi list
- ps -eo command **List all the commands who was execute on the machine**
- rdesktop -u ***user*** ***ip_adress*** [This allow us to connect on a Windows machine]
- dpkg -l '*utility*' **try this for remove with the name of the programm**
- tr '[G-ZA-Fg-za-g]' '[T-ZA-St-za-s]' **(ROT13)**
- tr ``' ' '\n'`` **Replace the output in line jumps**
- awk 'NF {print $NF}' **Print the last line**
- awk '{print $1}' **Print a specific line, in this case, the first**
- sed ``'s/^ *//'`` **Find blank spaces and replace with nothing**
- sed ``'/^\s*$/d'``  **Find blank spaces and replace with nothing**
- grep '^_word_' **Search in the line a word with start with a specific pattern**
- grep "Word" -A -B -C 1 **After, before, context and "NUM"**
- xxd -r **"Decrypts" a hexadecimal file**
- !$ **latest command used in the terminal**
- $? **Print the state of a code, STDIN, STDOUT, STDERR**
- echo '' > /dev/tcp/127.0.0.1/30000 **If the state is "0" the port is open**
- echo "**Argument to send**" |nc localhost ***port*** 
- nc -nlvp ***port*** **With this input NetCat listen in the defined port**
- telnet ***localhost*** _"port"_ **With this input Telnet listen in the definet port**
- bash -c _"command chain"_ && _another command_ **This enable the console mode for a command"
-  openssl sl_client -connect 127.0.0.1:***port*** **Listen with SSL for a specific port**
- nmap --open -T5 -v -n **Aggressive input**
- nmap -p31000-32000 **We define a range for the scan**
- mktemp -d **Create a temporal directory**
- chmod 600 _"file"_ **Only the owner can read and overwrite the file"
- diff _"file1_ _"file2_ **Lists the differences between files or process**
- nc -nlvp `port`
- echo "hello" |md5sum **This create a MD5 hass for the first input**
- watch -n 1 `command` **Allow to execute the command, in this case, one second at time** 

# PowerShell

## Microsoft Training

Even the most basic programs do one or more ofthe following tasks.

- 

1. $psversiontable.psversion - **Get the version of powershell**
2. get-verb 
3. get-command **Display the cmdlet lists of the available cmdlets on your system, you can see the aliases too**
4. get-help / help **Describes Powershell cmdlets, funcionts, scripts and modules, also include the elementals of Powershell**
	- Get-Help \<cmdlet-name> ***We can use the help too, this pipe Get-Help***
	- Get-Help \<cmdlet-name> -online 
	- Get-Help \<cmdlet-name> -examples
	- Get-Member
	- Get-Random **"Get" is the verb and "Random" the noun**
	- Get-Command -noun pdf* **Search the cmdlet with the noun "pdf"**
	- Get-Command -verb import* **Search the cmdlet with the verb "merge"
	- Update-Help -UICulture en-US -verbose
	- -full -detailed - examples - online - parameter **Useful flags** 
5. We can generate Hashes with **Get-filehash**
6. Get-Process -Name tor | Get-Member 
7. Get-Process -Name tor | Get-Member | Select-Object Name, MemberType 
8. Stop-Process ***Get Fun***
9. Get-Command -parametertype process
10. Get-Command -noun process
11. Get-Process | Select-Object Name | Where-Object Name -eq tor 
12. read-host -prompt "nothing"
13. write-output "olleh" 





---

1. Get-WmiObject -Class win32_OperatingSystem | select Version,BuildNumber **Winver and BuildNum**
2. Get-Service | ? {$_.Status -eq "Running"} | select -First 2 |fl
3. [ICACLS](https://ss64.com/nt/icacls.html) **Integrity Control Access Control List**
4. [List of Services in Windows](https://en.wikipedia.org/wiki/List_of_Microsoft_Windows_components#Services) In Windows, we have some [critical system services](https://docs.microsoft.com/en-us/windows/win32/rstmgr/critical-system-services) that cannot be stopped and restarted without a system restart. If we update any file or resource in use by one of these services, we must restart the system.
5. get-psrepository **Chek if the status is trusted**
6. set-psrepository -name psgallery -installationpolicy trusted
7. install-module -name importexcel **Whit this input we can install modules like "importexcel" in powersh**
8. find-module importexcel **show the version, name and repository of the module**
9. import-module importexcel **import the module for the current session in PowerShell**
	1. We can search for more module like pswritepdf or mergepdf for create, read, modify and merge pdf's
	2. Install modules like mergepdf, pswritepdf, pssharedgoods
10. import-excel `.\file_name` -worksheetname `sheet1` ***This load the worksheet***
11. mergepdf in a specific path with an amount of .pdf files will merge all the documents in only one :)
12. [$PSScriptRoot](https://shellgeek.com/powershell-psscriptroot-automatic-variable/)
13.  Customization - oh_my_posh
	1. [Local.Config](C:\Users\Julian.Gonzalez\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState)
	2. [PowerShell.Profile](\\XpFeSerFile\Datos$\Julian.Gonzalez\Mis documentos\PowerShell)
	3. [oh-my-posh Themes](C:\Users\Julian.Gonzalez\AppData\Local\Programs\oh-my-posh\themes)



___

# SSH

>**Secure Shell Protocol** is a [cryptographic](https://en.wikipedia.org/wiki/Cryptography "Cryptography") [network protocol](https://en.wikipedia.org/wiki/Network_protocol "Network protocol") for operating [network services](https://en.wikipedia.org/wiki/Network_service "Network service") securely over an unsecured network. 

## Important commands #bash_commands 
- ssh-keygen
1. _id_rsa.pub: ***public key*** 
	- cp id_rsa.pub authorized_keys (copy the "authorized_keys" into the .ssh directory for the user who want to make a remote connection)
2. id_rsa: ***private key*** 
	- ssh-copy-id -i id_rsa root@**("USER")**

-  ssh -i id_rsa root@**("USER")**
- ssh -i **password** ***USER***@***IP*** -p ***port***

___

# SCRIPTS/BASH

#bash_scripts

#### Script made to resolve the level 12 of Bandit in [OverTheWire](https://overthewire.org/wargames/bandit/bandit13.html)
```
**#!/bin/bash**

name_decompressed=$(7z l content.gzip |grep "Name" -A 2 |tail -n 1 |awk 'NF{print $NF}')
7z x content.gzip > /dev/null 2>&1

while true; do
        7z l $name_decompressed > /dev/null 2>&1

        if [ "$(echo $?)" == "0" ]; then
                decompressed_next=$(7z l $name_decompressed |grep "Name" -A 2 |tail -n 1 |awk 'NF{print $NF}')
                7z x $name_decompressed > /dev/null 2>&1 && name_decompressed=$decompressed_next
        else
                cat $name_decompressed; rm data* 2>/dev/null
                exit 1
        fi

done
```


___

# Important Terms - Linux OS
##### Useful terminologies on Cybersecurity
#terms

1. OSINT _Open Source Intelligence / Collection and analysis of data gathered from open sources to produce services of intelligence_
2. MSSQL _Microsoft Structured Query Language_
3. NULL _In data base represent the absence of a value in a certain field, his value is unknown_
4. TCP _Transmission Control Protocol_
5. UDP _User Datagram Protocol_
6. SSL _Secure Socket Layer_ > /tmp
7. OPENSSL _Software library who provide secure communications over the Network_
8. SETUID **Set user identity 
9. SETGID **Set group identity
	- Allow execute commands with a specific permissions respectively with the "setuid" or "setgid".
1. 127.0.0.1
2. ::1
3. AES-256
4. NCSC **National Cyber Security Centre** /// _CHECK certification_
5. ROE **Rules of Engagement**
	1. Permission
	2. Test Scope
	3. Rules
6. MITM **Man in the middle**
7. SOC **Security Operations Center**
8. DFIR **Digital Forensics and Incident Response**
9. SIEM **Security Information and Event Management**
10. CIA triad **Confidentiality, Integrity and Availability**
11. PIM **Privileged Identity Managment**
12. PAM **Privileged Acces Managment**
13. The Bell-La Padula Model - Can't read up, can read down
14. The Biba Model - Can read up, can't read down
15. STRIDE Model - For Threat analysis **Spoofing, Tampering, Repudiation, Info. Disclosure, Denial of Services, Elevation of Privilege**
16. PASTA Model - For Threat analysis ###
17. CSIRT **Computer Security Incident Response Team**
18. AJAX for Web Applications
19. [robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro) ***Example*** https://machine_ip/robots.txt
20. [OWASP_Favicon_Framework](https://wiki.owasp.org/index.php/OWASP_favicon_database) ***Example*** https://static-labs.tryhackme.cloud/sites/favicon/
21. [sitemap.xml](https://search.gov/indexing/sitemaps.html) ***Example*** https://machine_ip/sitemap.xml
22. [HTTP-Header](https://www.ionos.com/digitalguide/hosting/technical-matters/http-header/) ***Example*** curl http://machine_ip -v
23. [Google Dorks](https://www.avg.com/en/signal/google-dorks) site: inurl: filetype: intitle: 
24. [Wappalyzer](https://www.wappalyzer.com/) `Search the alternative for command line`
25. [Wayback Machine](https://archive.org/web/)
26. [Github/Git](https://www.git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F) **version control system**
27. [S3 Buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html)
28. 

# Important Terms - Windows OS
1. Get-WmiObject -Class win32_OperatingSystem | select Version,BuildNumber **Winver and BuildNum**
2. [DLL](https://learn.microsoft.com/en-us/troubleshoot/windows-client/deployment/dynamic-link-library) **Dynamic Link Library** - Much of the funcionality of the programs are provide of the DLL's
4. FAT32 **File Allocation Tables, the 32 refers to 32 bits of data for identifying data clusters on a storage device**
5. NTFS **New Technology File System offer a better support for metadata and better performance due to improved data structuring.
6. SMB Protocol **Sever Message Block** [Utility == smbclient]
8. ACL **Access Control List**
9. ACEs **Access Control 
10. ***The primary difference between a workgroup and a Windows Domain in terms of authentication, is with a workgroup the local SAM database is used and in a Windows Domain a centralized network-based database (Active Directory) is used.***
11. `Computer Management` is another tool we can use to identify and monitor shared resources on a Windows system.
12. `Event Viewer` is another good place to investigate actions completed on Windows. Almost every operating system has a logging mechanism and a utility to view the logs that were captured.
 ___

# Methodology

## The steps for penetration testings


| Stage                   | Description                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| _Information Gathering_ |                                                                                     This stage involves collecting as much publically accessible information about a target/organisation as possible, for example, OSINT and research. **Note: This does not involve scanning any systems.**                                                                                     |
|  _Enumeration/Scanning_ |                                                                                                              This stage involves _discovering applications and services running on the systems._ For example, finding a web server that may be potentially vulnerable.                                                                                                             |
|      _Exploitation_     |                                                                                                     This stage involves _leveraging vulnerabilities discovered on a system or application._ This stage can involve the use of public exploits or exploiting application logic.                                                                                                     |
|  _Privilege Escalation_ | Once you have successfully exploited a system or application (known as a foothold), _this stage is the attempt to expand your access to a system._ You can escalate horizontally and vertically, where horizontally is accessing another account of the same permission group (i.e. another user), whereas vertically is that of another permission group (i.e. an administrator). |
|   _Post-exploitation_   |                                                                             This stage involves a few sub-stages:  _1. What other hosts can be targeted (pivoting)_ **2. What additional information can we gather from the host now that we are a privileged user** _3.  Covering your tracks_ 4. Reporting                                                                             |

## Resources

 1. OSSTMM - [The Open Source Security Testing Methodology Manual](https://www.isecom.org/OSSTMM.3.pdf) 
	- The methodology focus on:
		1. Telecommunications (phones, VoIP,etc)
		2. Wired Networks
		3. Wireless communications
 1. OWASP - [Open Web Application Security project](https://owasp.org/)
	 - Regularly write reports starting with the top ten vulnerabilities
	 - This top ten have a focus on web applications and services
 2. NIST - [Cybersecurity Framework 1.1](https://www.nist.gov/cyberframework)
	 - 50% of the organizations use this framework and accreditation
	 - Very frequently updated
	 - Is designed to be implemented alongside with other frameworks
 3. NCSC CAF - [Cyber Assessment Framework (CAF)](https://www.ncsc.gov.uk/collection/caf/caf-principles-and-guidance)
	 - Data security
	 - System security
	 - Identity and access control
	 - Resiliency
	 - Monitoring
	 - Response and recovery planning

___
# Exercises HandsOn 

### Task completed are in a ***different color***
1. Convert binaries to decimals
2. Encode and Decode "Base 64" and "ROT13"
3. Learn about common forms of cryptography, and their uses on CyberSec.
4. Read about ***redis, impacket, smbclient, evilwinrm, telnet***
5. Customize the linux terminal with logs functions and powerlevel10k
6. **mode con lines=60** netsh **wlan** show profiles name="`SSID`" key=clear
7. ls /etc/NetworkManager/system-connections

___

# FootNotes

[^1]:https://en.wikipedia.org/wiki/Bash_(Unix_shell)