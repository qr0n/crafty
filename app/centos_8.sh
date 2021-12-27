#!/bin/bash
sudo dnf update -y
sudo dnf group install "Development tools" -y
sudo dnf install git wget python3 python3-devel java-1.8.0-openjdk java-1.8.0-openjdk-devel java-11-openjdk-devel java-17-openjdk-devel -y
mkdir /tmp/crafty
cd /tmp/crafty
wget -O java-16.rpm https://gitlab.com/bobsfriend12/files-repo/-/raw/main/jdk-16.0.1_linux-x64_bin.rpm?inline=false
rpm -ivh java-16.rpm
sudo useradd crafty -s /bin/bash
