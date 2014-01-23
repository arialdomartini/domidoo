#set -e
#set -u

source lib/functions.sh

function setup() {
    echo "This script is meant to be used in a box where python, pip and virtualenv are installed."
    echo "Since this script will pip install several packages, it's also reccomended that a virtualenv has been activated."
    echo
    while true; do
        read -p "Continue with installation? [y|n] " yn
        case $yn in
            [Yy]* ) do_setup; break;;
            [Nn]* ) exit;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}


function do_setup() {

    ######################
    # Install python tools
    ###################### 

    log "Installing and configuring ansible"
    pip install paramiko
    pip install pyyaml
    pip install jinja2


    log "Installing and configuring ansible"
    pip install ansible
    mkdir -p /etc/ansible

    log "I need to setup a /etc/ansible/hosts file for ansible. Please, enter your password"
    sudo cp resources/hosts /etc/ansible/hosts
    chmod 644 /usr/local/etc/ansible/hosts
    pip install --pre python-keyczar

    msg "Sweet!"
    msg "Now you are ready to setup the server, running"
    msg "./build-server.sh"
}


setup

