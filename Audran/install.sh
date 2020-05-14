#!/bin/bash
./partage.sh
sudo apt-get install python3-pip
pip3 install -U pip
sudo apt-get install gcc python3-dev
pip3 install psutil
pip3 install pygal
sudo apt install sqlite3
sudo apt-get install librrd-dev libpython3-dev
pip3 install rrdtool