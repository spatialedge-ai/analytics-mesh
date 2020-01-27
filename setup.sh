#!/bin/bash

if [[ -z "$ENV_PASSWORD" ]]; then
	echo "ERROR: password required for root ssh connection"
fi
echo "$ENV_PASSWORD"
echo -e "\n  Setting root password for ssh connection"
echo "root:$ENV_PASSWORD"| chpasswd

cp /app/sshd_config /etc/ssh/sshd_config

echo " Setup the sftp folders"
mkdir -p /var/sftp/uploads

service ssh start 

echo -e "  Done \n"
cat
