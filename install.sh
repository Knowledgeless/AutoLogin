#!/bin/bash

# configure python 
sudo apt install python3-pip -y
pip3 install selenium 

#install chrome 
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb q
sudo dpkg -i google-chrome-stable_current_amd64.deb
