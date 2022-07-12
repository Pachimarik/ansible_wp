#!/bin/bash
export $(cat  variables | xargs)

# base requirements
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

yum install python39 sshpass -y
python3.9 -m pip install --upgrade pip --user
python3.9 -m pip install ansible --user

# ansible work
cd ansible/
ansible-config view
ansible -m ping all

ansible-playbook centos8_common.yml

cd ..