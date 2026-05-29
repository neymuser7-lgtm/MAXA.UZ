#!/bin/bash
# MAXA.UZ - Main Menu Script
# ==========================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

clear

echo -e "${RED}"
cat << "EOF"
    ███╗   ███╗ █████╗ ██╗  ██╗ █████╗   ██╗   ██╗███████╗
    ████╗ ████║██╔══██╗╚██╗██╔╝██╔══██╗  ██║   ██║╚══███╔╝
    ██╔████╔██║███████║ ╚███╔╝ ███████║  ██║   ██║  ███╔╝ 
    ██║╚██╔╝██║██╔══██║ ██╔██╗ ██╔══██║  ██║   ██║ ███╔╝  
    ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗██║  ██║  ╚██████╔╝███████╗
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═════╝ ╚══════╝
EOF
echo -e "${YELLOW}          HAQIQIY HAKERLAR UCHUN TERMINAL${NC}"
echo -e "${YELLOW}                 MAXA.UZ v1.0${NC}"
echo ""

while true; do
    echo -e "${CYAN}========================================${NC}"
    echo -e "${GREEN}[1]${NC} QIDIRUV (OSINT)"
    echo -e "${GREEN}[2]${NC} TARMOV (NETWORK)"
    echo -e "${GREEN}[3]${NC} PAROL (CRACKING)"
    echo -e "${GREEN}[4]${NC} WEB HUJUM (WEB ATTACK)"
    echo -e "${GREEN}[5]${NC} ZARARLI DASTUR (MALWARE)"
    echo -e "${GREEN}[6]${NC} FIRIBGARLIK (PHISHING)"
    echo -e "${GREEN}[7]${NC} SIMSIZ (WIRELESS)"
    echo -e "${GREEN}[8]${NC} FOYDALANISH (EXPLOITATION)"
    echo -e "${GREEN}[9]${NC} ORQAGA KIRISH (BACKDOOR)"
    echo -e "${GREEN}[0]${NC} CHIQISH"
    echo -e "${CYAN}========================================${NC}"
    
    read -p "$(echo -e ${BLUE}'Tanlang: '${NC})" choice
    
    case $choice in
        1)
            python3 -c "
from modules.osint import OSINT
osint = OSINT()
print()
print('\033[0;36m[1]\033[0m Username Qidirish')
print('\033[0;36m[2]\033[0m Ism Familya Qidirish')
print('\033[0;36m[3]\033[0m Email Qidirish')
print('\033[0;36m[4]\033[0m Telefon Qidirish')
print('\033[0;36m[5]\033[0m Domen Qidirish')
print('\033[0;36m[6]\033[0m Hammasini Birga')
sub = input('\033[0;34mTanlang: \033[0m')
if sub == '1':
    u = input('Username: ')
    osint.username_search(u)
elif sub == '2':
    n = input('Ism Familya: ')
    osint.name_search(n)
elif sub == '3':
    e = input('Email: ')
    osint.email_search(e)
elif sub == '4':
    p = input('Telefon: ')
    osint.phone_search(p)
elif sub == '5':
    d = input('Domen: ')
    osint.domain_search(d)
elif sub == '6':
    a = input('Username: ')
    osint.all_search(a)
"
            ;;
        2)
            python3 -c "
from modules.network import Network
net = Network()
print()
t = input('Target IP: ')
print('\033[0;36m[1]\033[0m Port Skan')
print('\033[0;36m[2]\033[0m Zaiflik Skan')
print('\033[0;36m[3]\033[0m DNS Enum')
sub = input('\033[0;34mTanlang: \033[0m')
if sub == '1':
    net.port_scan(t)
elif sub == '2':
    p = input('Port (default 80): ') or '80'
    net.vuln_scan(t, int(p))
elif sub == '3':
    net.dns_enum(t)
"
            ;;
        3)
            python3 -c "
from modules.cracker import Cracker
cr = Cracker()
print()
h = input('Hash: ')
cr.identify_hash(h)
if len(h) == 32:
    ml = int(input('Max uzunlik (default 6): ') or '6')
    cr.crack_md5(h, ml)
"
            ;;
        0)
            echo -e "${RED}Dasturdan chiqildi!${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}Notog'ri tanlov!${NC}"
            ;;
    esac
    
    echo ""
done
