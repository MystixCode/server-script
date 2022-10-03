#!/usr/bin/env python3

import os

print("server-script")

def update_system():
    os.system("sudo apt -qq update && sudo apt -qq upgrade -y && sudo apt -qq full-upgrade -y && sudo apt -qq autoremove -y")

def install_openssh_server():
    os.system("sudo apt -qq -y install openssh-client openssh-server")
    print("Now stop here and run client-script on the computer u want to connect from to generate keys")
    input("When done press enter to continue...")
    src="sshd_config"
    dst="/etc/ssh/sshd_config"
    os.system(f"sudo cp -a {src} {dst}")
    os.system("sudo systemctl restart ssh")

def install_firewall():
    os.system("sudo apt -qq -y install ufw")
    os.system("sudo ufw allow SSH")
    os.system("sudo ufw allow 80")
    os.system("sudo ufw allow 443")
    os.system("sudo ufw allow 8899")
    os.system("echo 'y' | sudo ufw enable")
    os.system("sudo ufw status")

def install_fail2ban():
    os.system("sudo apt-get -yqq install fail2ban")
    os.system("sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local")
    # os.system("sudo sed -i '/\[nginx-http-auth\]/a enabled = true' /etc/fail2ban/jail.local")
    os.system("sudo systemctl start fail2ban")
    #os.system("sudo systemctl restart fail2ban")
    print("View fail2ban status with: sudo fail2ban-client status")
    print("View jail status with: sudo fail2ban-client status <jail>")

def install_docker():
    # install dependencies
    os.system("sudo apt-get -yqq install apt-transport-https ca-certificates curl gnupg lsb-release")
    # install key
    #curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor > /usr/share/keyrings/docker-archive-keyring.gpg
    os.system("curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor | sudo tee /usr/share/keyrings/docker-archive-keyring.gpg > /dev/null")
    # install repo
    os.system("echo \"deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
https://download.docker.com/linux/debian $(lsb_release -cs) stable\" \
| sudo tee /etc/apt/sources.list.d/docker.list > /dev/null")
    # update package list
    os.system("sudo apt-get -qq update")
    # install docker
    os.system("sudo apt-get -yqq install docker-ce docker-ce-cli containerd.io docker-compose-plugin")
    # add $USER to sudo group
    os.system("sudo usermod -aG docker $USER")
    #os.system("newgrp docker") #to initialise new group to session without logout/login
    # enable docker service
    os.system("sudo systemctl start docker.service")
    os.system("sudo systemctl enable docker.service")
    os.system("sudo systemctl enable containerd.service")
    os.system("docker --version")
    os.system("docker compose version")
    os.system("logout")

update_system()
install_openssh_server()
install_firewall()
install_fail2ban()
install_docker()