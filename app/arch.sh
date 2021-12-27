#!/bin/bash
sudo pacman -Syu
sudo pacman -S --noconfirm git extra/python extra/python-pip extra/jre8-openjdk extra/jdk8-openjdk jre11-openjdk-headless jre17-openjdk-headless
sudo useradd crafty -s /bin/bash
