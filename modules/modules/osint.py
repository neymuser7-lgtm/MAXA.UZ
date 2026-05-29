cat > ~/MAXA.UZ/modules/osint.py << 'EOF'
import sys, os, subprocess
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from config.colors import Colors
except:
    class Colors:
        RED = '\033[0;31m'
        GREEN = '\033[0;32m'
        YELLOW = '\033[1;33m'
        CYAN = '\033[0;36m'
        BLUE = '\033[0;34m'
        BOLD = '\033[1m'
        RESET = '\033[0m'
        DIM = '\033[2m'

def username_search(username):
    print(f"\n{Colors.CYAN}[*] Username qidirilmoqda: {Colors.BOLD}{username}{Colors.RESET}\n")
    
    sites = [
        ("Instagram", f"https://www.instagram.com/{username}"),
        ("GitHub", f"https://github.com/{username}"),
        ("Reddit", f"https://www.reddit.com/user/{username}"),
        ("YouTube", f"https://www.youtube.com/@{username}"),
        ("TikTok", f"https://www.tiktok.com/@{username}"),
        ("Telegram", f"https://t.me/{username}"),
        ("Twitter", f"https://twitter.com/{username}"),
        ("Facebook", f"https://www.facebook.com/{username}"),
        ("Pinterest", f"https://www.pinterest.com/{username}"),
        ("Snapchat", f"https://www.snapchat.com/add/{username}"),
        ("LinkedIn", f"https://www.linkedin.com/in/{username}"),
        ("VK", f"https://vk.com/{username}"),
        ("Twitch", f"https://www.twitch.tv/{username}"),
        ("Steam", f"https://steamcommunity.com/id/{username}"),
        ("Spotify", f"https://open.spotify.com/user/{username}"),
        ("Medium", f"https://medium.com/@{username}"),
        ("Flickr", f"https://www.flickr.com/people/{username}"),
        ("Dribbble", f"https://dribbble.com/{username}"),
        ("Behance", f"https://www.behance.net/{username}"),
        ("Patreon", f"https://www.patreon.com/{username}"),
    ]
    
    found = []
    
    for site_name, url in sites:
        try:
            cmd = f"curl -s -o /dev/null -w '%{{http_code}}' --max-time 5 '{url}'"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            code = result.stdout.strip()
            
            if code == "200":
                found.append((site_name, url))
                print(f"{Colors.GREEN}[+] {site_name}: {url}{Colors.RESET}")
            else:
                print(f"{Colors.RED}[-] {site_name}: Topilmadi{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.DIM}[-] {site_name}: Xatolik{Colors.RESET}")
    
    print(f"\n{Colors.YELLOW}[!] Jami topildi: {len(found)} ta sayt{Colors.RESET}")
    return found

def name_search(name):
    print(f"\n{Colors.CYAN}[*] Ism qidirilmoqda: {name}{Colors.RESET}\n")
    google_url = f"https://www.google.com/search?q={name.replace(' ', '+')}"
    print(f"{Colors.GREEN}Google: {google_url}{Colors.RESET}")
    linkedin_url = f"https://www.linkedin.com/search/results/people/?keywords={name.replace(' ', '%20')}"
    print(f"{Colors.GREEN}LinkedIn: {linkedin_url}{Colors.RESET}")

def email_search(email):
    print(f"\n{Colors.CYAN}[*] Email tekshirilmoqda: {email}{Colors.RESET}\n")
    print(f"{Colors.YELLOW}[*] HaveIBeenPwned, DeHashed, Intelx.io saytlarida tekshiring{Colors.RESET}")
    print(f"{Colors.GREEN}[+] Email: {email}{Colors.RESET}")

def phone_search(phone):
    print(f"\n{Colors.CYAN}[*] Telefon qidirilmoqda: {phone}{Colors.RESET}\n")
    print(f"{Colors.YELLOW}[*] Truecaller, GetContact, PhoneInfoga orqali tekshiring{Colors.RESET}")
    print(f"{Colors.GREEN}[+] Telefon: {phone}{Colors.RESET}")

def domain_search(domain):
    print(f"\n{Colors.CYAN}[*] Domen qidirilmoqda: {domain}{Colors.RESET}\n")
    subdomains = ["www", "mail", "admin", "api", "dev", "test", "ftp", "cdn", "blog", "shop", "webmail", "portal"]
    
    for sub in subdomains:
        full = f"{sub}.{domain}"
        cmd = f"ping -c 1 -W 2 {full} > /dev/null 2>&1"
        result = subprocess.run(cmd, shell=True)
        if result.returncode == 0:
            print(f"{Colors.GREEN}[+] {full} - Topildi{Colors.RESET}")
        else:
            print(f"{Colors.RED}[-] {full}{Colors.RESET}")

def all_search(username):
    print(f"\n{Colors.YELLOW}{'='*50}{Colors.RESET}")
    print(f"{Colors.BOLD}TO'LIQ QIDIRUV: {username}{Colors.RESET}")
    print(f"{Colors.YELLOW}{'='*50}{Colors.RESET}")
    username_search(username)
    email_search(f"{username}@gmail.com")

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        cmd = sys.argv[1]
        val = sys.argv[2]
        if cmd == "username":
            username_search(val)
        elif cmd == "name":
            name_search(val)
        elif cmd == "email":
            email_search(val)
        elif cmd == "phone":
            phone_search(val)
        elif cmd == "domain":
            domain_search(val)
        elif cmd == "all":
            all_search(val)
        else:
            print(f"Noto'g'ri komanda: {cmd}")
    else:
        print("Ishlatish: python3 osint.py <komanda> <qiymat>")
        print("Komandalar: username, name, email, phone, domain, all")
EOF
