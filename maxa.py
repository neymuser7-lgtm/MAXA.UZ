#!/usr/bin/env python3
# MAXA.UZ - Main Python Script
# ============================

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config.colors import Colors, banner
from modules.osint import OSINT
from modules.network import Network
from modules.cracker import Cracker

class MAXA:
    def __init__(self):
        self.osint = OSINT()
        self.network = Network()
        self.cracker = Cracker()
    
    def main_menu(self):
        print(banner())
        print(f"{Colors.CYAN}                MAXA.UZ v1.0{Colors.RESET}\n")
        
        while True:
            print(f"{Colors.CYAN}{'='*40}{Colors.RESET}")
            print(f"{Colors.GREEN}[1]{Colors.RESET} QIDIRUV (OSINT)")
            print(f"{Colors.GREEN}[2]{Colors.RESET} TARMOV (NETWORK)")
            print(f"{Colors.GREEN}[3]{Colors.RESET} PAROL (CRACKING)")
            print(f"{Colors.GREEN}[4]{Colors.RESET} WEB HUJUM")
            print(f"{Colors.GREEN}[5]{Colors.RESET} ZARARLI DASTUR")
            print(f"{Colors.GREEN}[6]{Colors.RESET} FIRIBGARLIK")
            print(f"{Colors.GREEN}[7]{Colors.RESET} SIMSIZ")
            print(f"{Colors.GREEN}[8]{Colors.RESET} FOYDALANISH")
            print(f"{Colors.GREEN}[9]{Colors.RESET} ORQAGA KIRISH")
            print(f"{Colors.GREEN}[0]{Colors.RESET} CHIQISH")
            print(f"{Colors.CYAN}{'='*40}{Colors.RESET}")
            
            choice = input(f"{Colors.BLUE}Tanlang: {Colors.RESET}")
            
            if choice == '1':
                self.osint_menu()
            elif choice == '2':
                self.network_menu()
            elif choice == '3':
                self.cracker_menu()
            elif choice == '0':
                print(f"{Colors.RED}[!] Dasturdan chiqildi!{Colors.RESET}")
                sys.exit(0)
            else:
                print(f"{Colors.RED}[!] Noto'g'ri tanlov!{Colors.RESET}")
    
    def osint_menu(self):
        print(f"\n{Colors.YELLOW}--- QIDIRUV MENU ---{Colors.RESET}")
        print(f"{Colors.GREEN}[1]{Colors.RESET} Username")
        print(f"{Colors.GREEN}[2]{Colors.RESET} Ism Familya")
        print(f"{Colors.GREEN}[3]{Colors.RESET} Email")
        print(f"{Colors.GREEN}[4]{Colors.RESET} Telefon")
        print(f"{Colors.GREEN}[5]{Colors.RESET} Domen")
        print(f"{Colors.GREEN}[6]{Colors.RESET} Hammasi")
        
        sub = input(f"{Colors.BLUE}Tanlang: {Colors.RESET}")
        
        if sub == '1':
            u = input("Username: ")
            self.osint.username_search(u)
        elif sub == '2':
            n = input("Ism Familya: ")
            self.osint.name_search(n)
        elif sub == '3':
            e = input("Email: ")
            self.osint.email_search(e)
        elif sub == '4':
            p = input("Telefon: ")
            self.osint.phone_search(p)
        elif sub == '5':
            d = input("Domen: ")
            self.osint.domain_search(d)
        elif sub == '6':
            a = input("Username: ")
            self.osint.all_search(a)
    
    def network_menu(self):
        t = input(f"{Colors.BLUE}Target IP: {Colors.RESET}")
        print(f"\n{Colors.YELLOW}--- TARMOV MENU ---{Colors.RESET}")
        print(f"{Colors.GREEN}[1]{Colors.RESET} Port Skan")
        print(f"{Colors.GREEN}[2]{Colors.RESET} Zaiflik Skan")
        print(f"{Colors.GREEN}[3]{Colors.RESET} DNS Enum")
        
        sub = input(f"{Colors.BLUE}Tanlang: {Colors.RESET}")
        
        if sub == '1':
            self.network.port_scan(t)
        elif sub == '2':
            p = input("Port (default 80): ") or '80'
            self.network.vuln_scan(t, int(p))
        elif sub == '3':
            self.network.dns_enum(t)
    
    def cracker_menu(self):
        h = input(f"{Colors.BLUE}Hash: {Colors.RESET}")
        self.cracker.identify_hash(h)
        
        if len(h) == 32:
            ml = int(input("Max uzunlik (default 6): ") or '6')
            self.cracker.crack_md5(h, ml)

if __name__ == "__main__":
    maxa = MAXA()
    maxa.main_menu()
