#!/bin/bash

# MAXA.UZ - Auto Installer
# =========================

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

clear

echo -e "${GREEN}"
echo "╔═══════════════════════════════════════════╗"
echo "║         MAXA.UZ - AUTO INSTALLER          ║"
echo "╚═══════════════════════════════════════════╝"
echo -e "${NC}"

if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}[!] Root huquqi kerak! Sudo bilan ishga tushiring:${NC}"
    echo -e "${YELLOW}    sudo ./install.sh${NC}"
    exit 1
fi

echo -e "${GREEN}[+] Tizim yangilanmoqda...${NC}"
apt update -y && apt upgrade -y

echo -e "${GREEN}[+] Kerakli paketlar o'rnatilmoqda...${NC}"
apt install -y python3 python3-pip git curl wget nmap net-tools
apt install -y hydra john hashcat aircrack-ng
apt install -y wireshark tcpdump dnsutils
apt install -y openssh-client openssh-server
apt install -y steghide exiftool
apt install -y crunch cewl
apt install -y tor proxychains4

echo -e "${GREEN}[+] Python modullar o'rnatilmoqda...${NC}"
pip3 install -r requirements.txt
pip3 install --upgrade pip

echo -e "${GREEN}[+] Tool papkalari yaratilmoqda...${NC}"
mkdir -p wordlists output config/modules

echo -e "${GREEN}[+] Skript huquqlari berilmoqda...${NC}"
chmod +x maxa.sh maxa.py

echo -e "${YELLOW}"
echo "╔═══════════════════════════════════════════╗"
echo "║         O'rnatish muvaffaqiyatli!         ║"
echo "║         Ishga tushirish: ./maxa.sh        ║"
echo "╚═══════════════════════════════════════════╝"
echo -e "${NC}"
