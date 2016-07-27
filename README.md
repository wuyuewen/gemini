# Name: gemini
A project extends Apache Libcloud particularly on driver Libvirt and Docker.
Providing a RESTful API for users.

**Copyright: Institute of Software, Chinese Academy of Sciences**

**Authors: wuyuewen@otcaix.iscas.ac.cn, wuheng09@otcaix.iscas.ac.cn**

## Installation

**Step 1: **Installing Operating System from ISO image, CentOS 6/7 are supported.

**Step 2: **Updating current OS environment and installing required packages.
- `yum install centos-release-xen` (install xen repository for yum install)
- `yum install xen`
- `yum update`
- `sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config` (disable SELinux)
- `reboot`

After reboot please verify running kernel and xen.
- `uname -r`
- `xl info`

**Note: **Sometimes CentOS 7 may have a network connection problem, please close IPv6 and try again.
- <https://wiki.centos.org/FAQ/CentOS7> (Question 5 for details)

Installing libvirt and libvirt-python.
- `yum install rsync wget vim-enhanced openssh-clients`
- `yum install libvirt python-virtinst libvirt-daemon-xen libvirt-python`

System service settings for CentOS 7.
- `systemctl disable firewalld.service` (disable firewall)
- `systemctl stop firewalld.service` (stop firewall)
- `systemctl enable libvirtd.service` (enable libvirtd)
- `systemctl start libvirtd.service` (start libvirtd)

System service settings for CentOS 6.
- `chkconfig iptables off` (disable iptables)
- `service iptables stop` (stop iptables)
- `chkconfig libvirtd on` (enable libvirtd)
- `service libvirtd start` (start libvirtd)

**Step 3: **Installing python dependency via `pip install`
- `pip install apach-libcloud`
- `pip install flask-restful`
- `pip install xmltodict`

## Getting started
Run main program.
- `python RunServer.py`

Run a http-request for test.
- `curl -i "http://localhost:5000/libvirt/xen/host/system/json"`
