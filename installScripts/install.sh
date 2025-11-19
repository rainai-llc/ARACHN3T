#!/usr/bin/bash
# Author: Jeremiah Jackson-Williams
#
# Copyrights: Rainai Inc. @2025
#

git clone https://github.com/Rainai-Inc/Autopilot
apt install golang subfinder
GO111MODULE=on go install github.com/sw33tLie/bbscope@latest
mv $HOME/go/bin/bbscope /usr/bin


#https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json
