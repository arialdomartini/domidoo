red="\033[0;31m"
green="\033[0;32m"
yellow="\033[0;33m"
violet="\033[0;35m"
reset="\033[0m"

function msg() {
    message=$1
    echo -e "${green}${message}${reset}"
}

function log() {
    msg "> ${1}"
}
