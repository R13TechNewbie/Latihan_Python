#!/bin/sh

pkg install python2
pkg install wget
wget -c http://manggalabroker.com/Tasya.zip -O tasya.zip
unzip tasya.zip
cd LINE/
python2 setup.py install
pip2 uninstall thrift
pip2 install thrift==0.9.3


echo 'masukin username LINE [enter]';
read username
echo 'masukin password LINE [enter]';
read password

cd examples/
cat echobot.py | grep -v 'client = Line' > dest.txt ; rm -rf echobot.py ; mv dest.txt echobot.py
sed -i "7i\ \ \ \ client = LineClient('"$username"', '"$password"')" echobot.py;

python2 echobot.py