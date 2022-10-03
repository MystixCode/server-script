#!/bin/bash

green=`echo -en "\e[32m"`
normal=`echo -en "\e[0m"`
orange=`echo -en "\e[33m"`

# Create ssh key if not exists
FILE=~/.ssh/id_ed25519.pub
if [ -f $FILE ]; then
    echo "$FILE exists. Using already existing ssh key"
else 
    echo "Create new ssh key"
    ssh-keygen -t ed25519 -C "${USER}@${HOSTNAME}" -f ~/.ssh/id_ed25519 -N ''
fi

read -e -i "${USER}" -p "${green}Please enter username on server: $normal" username
echo $username

read -e -i "192.168.1.3" -p "${green}Please enter servername: $normal" servername
echo $servername

# Copy public key to server
ssh-copy-id -i ~/.ssh/id_ed25519.pub $username@$servername

echo "${orange}Now u can continue with the ServerScript $normal"
