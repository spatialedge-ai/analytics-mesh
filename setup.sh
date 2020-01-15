#!/bin/bash

if [[ -z "$ENV_PASSWORD" ]]; then
	echo "ERROR: password required for root ssh connection"
fi
echo "$ENV_PASSWORD"
echo -e "\n  Setting root password for ssh connection"
echo "root:$ENV_PASSWORD"| chpasswd

echo -e "  Modifying sshd_config to accept password authentication on ssh"
sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config  

echo "  Modifying sshd_config to allow root user password"
sed -i 's/PermitRootLogin .*$/PermitRootLogin yes/g' /etc/ssh/sshd_config

echo " Setup the sftp folders"
mkdir -p /var/sftp/uploads

service ssh start 

echo -e "  Done \n"
cat
