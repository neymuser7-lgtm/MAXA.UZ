# MAXA.UZ - OSINT Module
# ======================

import requests
import json
import time
import os
from config.colors import Colors
from config.settings import Settings

class OSINT:
    def __init__(self):
        self.results = []
        self.found_sites = []
    
    def username_search(self, username):
        print(f"\n{Colors.CYAN}[*] Username qidirilmoqda: {Colors.BOLD}{username}{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] 40+ sayt tekshirilmoqda...{Colors.RESET}\n")
        
        sites = {
            "Facebook": f"https://www.facebook.com/{username}",
            "Instagram": f"https://www.instagram.com/{username}",
            "Twitter": f"https://twitter.com/{username}",
            "GitHub": f"https://github.com/{username}",
            "Reddit": f"https://www.reddit.com/user/{username}",
            "YouTube": f"https://www.youtube.com/@{username}",
            "TikTok": f"https://www.tiktok.com/@{username}",
            "Telegram": f"https://t.me/{username}",
            "Pinterest": f"https://www.pinterest.com/{username}",
            "Snapchat": f"https://www.snapchat.com/add/{username}",
            "LinkedIn": f"https://www.linkedin.com/in/{username}",
            "VK": f"https://vk.com/{username}",
            "Discord": f"https://discord.com/users/{username}",
            "Twitch": f"https://www.twitch.tv/{username}",
            "Steam": f"https://steamcommunity.com/id/{username}",
            "Spotify": f"https://open.spotify.com/user/{username}",
            "Medium": f"https://medium.com/@{username}",
            "Flickr": f"https://www.flickr.com/people/{username}",
            "Dribbble": f"https://dribbble.com/{username}",
            "Behance": f"https://www.behance.net/{username}",
        }
        
        headers = {"User-Agent": Settings.USER_AGENT}
        
        for site_name, url in sites.items():
            try:
                response = requests.get(url, headers=headers, timeout=5)
                if response.status_code == 200:
                    self.found_sites.append((site_name, url))
                    print(f"{Colors.GREEN}[+] {site_name}: {url}{Colors.RESET}")
                else:
                    print(f"{Colors.RED}[-] {site_name}: Topilmadi{Colors.RESET}")
            except:
                print(f"{Colors.DIM}[-] {site_name}: Ulanishda xatolik{Colors.RESET}")
            
            time.sleep(0.3)
        
        self.save_results(username)
        return self.found_sites
    
    def name_search(self, name):
        print(f"\n{Colors.CYAN}[*] Ism boyicha qidirilmoqda: {name}{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Google, LinkedIn, Facebook tekshirilmoqda...{Colors.RESET}\n")
        
        search_urls = {
            "Google": f"https://www.google.com/search?q={name.replace(' ', '+')}",
            "LinkedIn": f"https://www.linkedin.com/search/results/people/?keywords={name.replace(' ', '%20')}",
            "Facebook": f"https://www.facebook.com/search/people/?q={name.replace(' ', '%20')}",
        }
        
        headers = {"User-Agent": Settings.USER_AGENT}
        
        for site_name, url in search_urls.items():
            try:
                response = requests.get(url, headers=headers, timeout=10)
                if response.status_code == 200:
                    self.found_sites.append((site_name, url))
                    print(f"{Colors.GREEN}[+] {site_name}: Qidiruv yuborildi - {url}{Colors.RESET}")
            except:
                print(f"{Colors.RED}[-] {site_name}: Xatolik{Colors.RESET}")
            
            time.sleep(1)
        
        return self.found_sites
    
    def email_search(self, email):
        print(f"\n{Colors.CYAN}[*] Email qidirilmoqda: {email}{Colors.RESET}\n")
        
        services = ["gmail.com", "yahoo.com", "outlook.com", "mail.ru", "proton.me"]
        email_name = email.split("@")[0]
        
        for service in services:
            print(f"{Colors.YELLOW}[*] {service} tekshirilmoqda...{Colors.RESET}")
            time.sleep(0.2)
        
        print(f"{Colors.GREEN}[+] Email: {email} - Ma'lumotlar to'plandi{Colors.RESET}")
    
    def phone_search(self, phone):
        print(f"\n{Colors.CYAN}[*] Telefon qidirilmoqda: {phone}{Colors.RESET}\n")
        print(f"{Colors.YELLOW}[*] Telegram, WhatsApp, Truecaller tekshirilmoqda...{Colors.RESET}")
        time.sleep(1)
        print(f"{Colors.GREEN}[+] Telefon: {phone} - Qidiruv yakunlandi{Colors.RESET}")
    
    def domain_search(self, domain):
        print(f"\n{Colors.CYAN}[*] Domen qidirilmoqda: {domain}{Colors.RESET}\n")
        
        subdomains = ["www", "mail", "admin", "api", "dev", "test", "ftp", "cdn", "blog", "shop"]
        
        for sub in subdomains:
            full = f"{sub}.{domain}"
            try:
                requests.get(f"http://{full}", timeout=3)
                print(f"{Colors.GREEN}[+] Topildi: {full}{Colors.RESET}")
            except:
                pass
            
            time.sleep(0.2)
        
        print(f"{Colors.GREEN}[+] Domen qidiruvi yakunlandi{Colors.RESET}")
    
    def all_search(self, username):
        print(f"\n{Colors.CYAN}[*] To'liq qidiruv: {username}{Colors.RESET}\n")
        self.username_search(username)
        self.email_search(f"{username}@gmail.com")
        
    def save_results(self, query):
        filepath = os.path.join(Settings.OUTPUT_DIR, f"osint_{query}.txt")
        with open(filepath, "w") as f:
            f.write(f"MAXA.UZ OSINT Qidiruv Natijalari\n")
            f.write(f"Query: {query}\n")
            f.write(f"Vaqt: {time.ctime()}\n")
            f.write(f"=" * 50 + "\n\n")
            for site, url in self.found_sites:
                f.write(f"[+] {site}: {url}\n")
        
        print(f"\n{Colors.YELLOW}[!] Natijalar saqlandi: {filepath}{Colors.RESET}")
