#!/usr/bin/env bash

#Proxy switcher for Burpsuite. Basically to automate setting the HTTP & HTTPS Web Proxy.

#Validate sudo timestamp and ask for admisistrative password
sudo -v

# Keep-alive: update existing `sudo` time stamp until finished
while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &

# trap ctrl-c and call disable_proxy()
function disable_proxy() {
    sudo networksetup -setwebproxy $INTERFACE off
    echo "$(tput setaf 64)" #green
    echo "HTTP & HTTPS web proxy disabled."
    echo "$(tput sgr0)" # color reset
}
trap disable_proxy INT


sudo networksetup -setwebproxy 