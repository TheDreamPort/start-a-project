# Starting a DreamPort Project
this repository holds all of our efforts to stand-up our Project network at the push of a button. The DreamPort is a meant to be a place where anything can happen if it is going to help serve the needs of the United States Cyber Command (USCYBERCOM). We are creating a network we call 'HQ' or Headquarters. HQ is a combination of virtual and physical hosts who serve as the experiment environment to test out new products, techniques, perform vulnerability research and generally validate theories and requests from USCYBERCOM and their customers without hours not months or years. As such this network must be able to change rapidly  and with little to no effort. This GitHub repository is designed to be cloned from GitHub, modified as required and then used by a DreamPort visttor with physical access to our networks to create a new fucntional environment without touching any hosts!

NOTE: this project requires access to the DreamPort facility and networks. We are happy to share with the world but it won't do you much good unless you have knowledge of our design! Please contact us to learn more.

## Repository Security DISCLAIMER
This message (or similar variants will be attached to every resource we publish here on GitHub). While we make use of wonderful resources from multiple Internet articles and Ansible Galaxy, we wish to state up-front that there are no private details in this repo. There are no details about USCYBERCOM or any US government affiliate. This repository is public on purpose and while I've gone gone to great lengths to ensure there are no truly sensitive details contained within (yes there is 1 password and I won't say where it is not an Administrator password) it is always possible to make a mistake. FYI when I determine the best method to eliminate the need for that ONE password I will remove it from here and change the corresponding account.

If you wish to report something you consider suspicious please contact us dir3ectly and we will gladly thank you  publicly for your responsible reporting!

## Getting Started
The first step to working with this project is ensuring your environment is setup correctly. This project is built on Ubuntu Desktop 16.04.5 amd64 and uses the following Ansible version:

```
ansible 2.7.4
  config file = /home/developer/workspace/start-a-project/ansible.cfg
  configured module search path = [u'/home/developer/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python2.7/dist-packages/ansible
  executable location = /usr/local/bin/ansible
  python version = 2.7.12 (default, Nov 12 2018, 14:36:49) [GCC 5.4.0 20160609]
```

### Update your Windows inventory
We operate under the assumption that you have either installed all of the hosts you will use or are joining a project that is in-progress. You need to update your Windows host inventory  (the file hosts).

./list_computers.py Administrator PASSWORD 

as in the following example:
	
```
developer@ubuntu:~/workspace/start-a-project$ ./list_computers.py Administrator <PASSWORD>
```
The output of this command will be similiar to the following:
```
DNSHostName            
-----------            
AD.hq1.com        
MININT-2B1IUDO.hq1.com 
MISIDRE-TRS9FG3.hq1.com
MISIDRE-J7PBD8H.hq1.com
MISIDRE-SFFK8U3.hq1.com
WINDOWS-CO3ROVQ.hq1.com
WINDOWS-4HUIFAU.hq1.com
WINDOWS-LL6NVTH.hq1.com
WINDOWS-3OMLQ30.hq1.com
WINDOWS-9UKDUGK.hq1.com
WINDOWS-9B2QAO2.hq1.com
WINDOWS-J13F2FP.hq1.com
WINDOWS-4A72DK7.hq1.com
WINDOWS-C90TSJL.hq1.com
WINDOWS-8886CKV.hq1.com
WINDOWS-NUCKC2M.hq1.com
WINDOWS-OFPE262.hq1.com
WINDOWS-B1LH55C.hq1.com
WINDOWS-DJLP83E.hq1.com
WINDOWS-2285A37.hq1.com
WINDOWS-AUPC1C5.hq1.com
```
## Setup Windows Host
In this section we detail the process to setup a hardware host within HQ with Microsoft Windows. As you can see below, we have gone through painful efforts to setup the Windows Deployment Services (WDS) to automatically push out Microsoft Windows images to our hosts.

- Install using WDS (this now defaults to Windows 10 Enterprise)
- Login as an your user to the target (for example 'mark')
- Open 'Network', click to enable Network Discovery, enter HQ1 Administrator creds to authenticate
- Enter UNC path for HQADC16 domain controller in Network address bar
- Map network share to Z:
- Copy Z:\configureansible.ps1 C:\Users\mark\Downloads
- Start Powershell as administrator
- Run Set-ExecutionPolicy unrestricted, type 'Y' when prompted
- Return to prep host and run the following to test your connection:
⋅⋅* ```ansible windows -i hosts -m win_ping --ask-pass -u administrator```
s
