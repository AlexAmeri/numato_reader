#!/bin/bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
export PATH="/home/user/.local/bin:$PATH"
pip install PySerial
pip install pynput
