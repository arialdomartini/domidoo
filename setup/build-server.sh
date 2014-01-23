#!/bin/bash
set -e
set -u
source lib/functions.sh

SERVER=37.247.55.31

log "Setting permissions on remote server authorizing arialdomartini's ssh key"
cat keys/arialdomartini_rsa.pub | ssh root@${SERVER} -o 'StrictHostKeyChecking no' "mkdir -p ~/.ssh; cat > ~/.ssh/authorized_keys"

ansible-playbook init.yml -u root

msg "Accelerated mode can be used"

log "Creating remote users"
ansible-playbook account.yml -u root

log "Installing the software"
ansible-playbook software-server.yml -u root

msg "Sweet!"
msg "You can ssh the remote $SERVER and control it with ansible"
msg "All is setup to allow developers to test and deploy medmd on the VPS."
msg "\nYou are a remote machine sudoer, so you can even login as root."
msg "Too much power and no control may be harmful."
