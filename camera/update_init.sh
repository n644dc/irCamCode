#! /bin/sh

sudo chmod +x ./*
sudo cp *.py /usr/local/bin/
sudo cp listenForCamera.sh /etc/init.d/
sudo update-rc.d listenForCamera.sh defaults