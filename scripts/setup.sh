#!/bin/bash

mkdir libraries
mkdir temp
cd temp
wget https://github.com/Kagami/nacl_sdk/archive/master.zip
unzip master.zip
mv nacl_sdk-master/naclsdk ../libraries/nacl
rm master.zip

mkdir libraries/libmpv
wget https://master.dl.sourceforge.net/project/mpv-player-windows/libmpv/mpv-dev-x86_64-20211107-git-ec16769.7z?viasf=1
unzip mpv-dev-x86_64-20211107-git-ec16769.7z
rm mpv-dev-x86_64-20211107-git-ec16769.7z
mv .* libraries/libmpv

cd ..
rmdir temp
