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
