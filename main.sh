#!/bin/sh
echo "name: $1"
pip install selenium
pip install pandas
pip install webdrivermanager
pip install requests
python3 main.py $1
