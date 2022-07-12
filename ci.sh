#!/bin/bash
export $(cat  variables | xargs)

# base requirements
yum install python39 sshpass -y
python3.9 -m pip install --upgrade pip --user
python3.9 -m pip install ansible --user

# ansible work
cd ansible/
ansible-config view
ansible -m ping all

cd ..