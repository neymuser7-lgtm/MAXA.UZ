# MAXA.UZ - Network Module
# =======================

import subprocess
import socket
import requests
from config.colors import Colors

class Network:
    def __init__(self):
        self.target = None
    
    def port_scan(self, target, ports=None):
        print(f"\n{Colors.CYAN}[*] Port skanerlanmoqda: {target}{Colors.RESET}\n")
        
        if ports is None:
            ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389, 8080]
        
        open_ports = []
        
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            
            if result == 0:
                service = self.get_service(port)
                open_ports.append((port, service))
                print(f"{Colors.GREEN}[+] Port {port} OCHIQ - {service}{Colors.RESET}")
            else:
                print(f"{Colors.DIM}[-] Port {port} Yopiq{Colors.RESET}")
            
            sock.close()
        
        return open_ports
    
    def get_service(self, port):
        services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
            53: "DNS", 80: "HTTP", 110: "POP3", 135: "RPC",
            139: "NetBIOS", 143: "IMAP", 443: "HTTPS", 445: "SMB",
            3306: "MySQL", 3389: "RDP", 5900: "VNC", 8080: "HTTP-Proxy"
        }
        return services.get(port, "Noma'lum")
    
    def vuln_scan(self, target, port=80):
        print(f"\n{Colors.CYAN}[*] Zaiflik skanerlanmoqda: {target}:{port}{Colors.RESET}\n")
        
        tests = [
            ("SQL Injection", f"{target}?id=1'"),
            ("XSS", f"{target}?search=<script>alert(1)</script>"),
            ("Directory Listing", f"{target}/admin/"),
            ("PHP Info", f"{target}/phpinfo.php"),
            ("Config File", f"{target}/.env"),
            ("Git", f"{target}/.git/HEAD"),
            ("Backup", f"{target}/backup.zip"),
            ("Admin Panel", f"{target}/admin/login.php"),
        ]
        
        headers = {"User-Agent": "MAXA.UZ-Scanner"}
        
        for vuln_name, url in tests:
            try:
                response = requests.get(f"http://{url}" if not url.startswith("http") else url, 
                                       headers=headers, timeout=5, allow_redirects=False)
                if response.status_code == 200:
                    print(f"{Colors.GREEN}[+] {vuln_name}: Topildi! - {url}{Colors.RESET}")
                else:
                    print(f"{Colors.RED}[-] {vuln_name}: Topilmadi{Colors.RESET}")
            except:
                print(f"{Colors.DIM}[-] {vuln_name}: Xatolik{Colors.RESET}")
    
    def dns_enum(self, domain):
        print(f"\n{Colors.CYAN}[*] DNS qazilmoqda: {domain}{Colors.RESET}\n")
        
        try:
            import dns.resolver
            
            record_types = ["A", "AAAA", "MX", "NS", "TXT", "SOA", "CNAME"]
            
            for rtype in record_types:
                try:
                    answers = dns.resolver.resolve(domain, rtype)
                    for answer in answers:
                        print(f"{Colors.GREEN}[+] {rtype}: {answer}{Colors.RESET}")
                except:
                    print(f"{Colors.DIM}[-] {rtype}: Yozuv topilmadi{Colors.RESET}")
        except:
            print(f"{Colors.RED}[!] dns moduli o'rnatilmagan: pip install dnspython{Colors.RESET}")
    
    def dos_attack(self, target, port=80):
        print(f"{Colors.RED}[!] DoS hujum uchun qo'shimcha tool kerak:{Colors.RESET}")
        print(f"{Colors.YELLOW}    hping3 -S --flood -p {port} {target}{Colors.RESET}")
        print(f"{Colors.YELLOW}    slowloris {target} -p {port}{Colors.RESET}")
