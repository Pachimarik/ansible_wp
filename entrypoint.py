import platform
import os
from distutils.version import LooseVersion

# fix repository on centos 8
def fix_repo():
    fix = input("You need fix repository? [y/n]:" )
    if fix == "y" or fix =="yes" or fix == "Y":
        os.system("sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*")
        os.system("sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*")
        os.system("yum update -y")
        ask_version_py()
    else:
        ask_version_py()

#check version python
def ask_version_py():
    if LooseVersion(platform.python_version()) <= LooseVersion("3.7.0"):
        print ( "Your python version" , platform.python_version())
        ver = input("""your version of python does not meet the requirements for ansible. 
        Do you want to install python version 3.9? [y/n]: """)
        if ver == "y" or ver =="yes" or ver == "Y":
            os.system("yum install python39 -y")
            install_ansible()
        else:
            exit()
    else:
        print("Your version of python meets the requirements. Begin install ansible")
        install_ansible()

#install ansible and sshpass
def install_ansible():
    os.system("yum install sshpass")
    os.system("python3 -m pip install --upgrade pip --user")
    os.system("python3 -m pip install ansible --user")
    os.system("cd ansible/ && ansible-config view && ansible -m ping all")
    choice_install()

def choice_install():
    base = input("""WARNING!!! wordpress works in docker, 
    if you have everything prepared, you can skip this paragraph, 
    otherwise you need to run the playbook with preparation 
    [Need preparation (y)/ I don`t need preparation (n)] """)
    if base == "y" or base == "Y":
        os.system("cd ansible/ && ansible-playbook centos8_common.yml")
    web_srv = input("""There are two versions of wordpress
    first is based on nginx
    second is based on apache. 
    Select version [nginx( n )/apache( a )]:""")
    if web_srv == "n" or web_srv == "nginx":
        db_ch=input("""Two ways to install wordpress 
        first way, installation with local database
        second way, installing ONLY WordPress 
        but you need to create a database and specify the necessary parameters for installation.
        [Local db( l ) / Remote db ( r )]:""")
        if db_ch == "l" or db_ch == "L":
            os.system("cd ansible/ && pwd && ansible-playbook wp_nginx_with_local_db.yml")
        else:
            os.system("cd ansible/ && pwd && ansible-playbook wp_nginx_with_remote_db.yml")

    elif web_srv == "a" or web_srv == "apache":
        db_ch=input("""Two ways to install wordpress 
        first way, installation with local database
        second way, installing ONLY WordPress 
        but you need to create a database and specify the necessary parameters for installation.
        [Local db( l ) / Remote db ( r )]:""")
        if db_ch == "l" or db_ch == "L":
            os.system("cd ansible/ && pwd && ansible-playbook wp_apache_with_local_db.yml")
        else:
            os.system("cd ansible/ && pwd && ansible-playbook wp_apache_with_remote_db.yml")

    print("INSTALL IS DONE!!!")

if __name__ == "__main__":
    fix_repo()
else:
    print("use file entrypoint.py")