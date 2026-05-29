# MAXA.UZ - Password Cracking Module
# =================================

import hashlib
import itertools
import string
import time
from config.colors import Colors

class Cracker:
    def __init__(self):
        pass
    
    def identify_hash(self, hash_str):
        print(f"\n{Colors.CYAN}[*] Hash aniqlanmoqda...{Colors.RESET}\n")
        
        length = len(hash_str)
        
        hash_types = {
            32: "MD5",
            40: "SHA1",
            56: "SHA224",
            64: "SHA256",
            96: "SHA384",
            128: "SHA512"
        }
        
        if length in hash_types:
            hash_type = hash_types[length]
            print(f"{Colors.GREEN}[+] Hash turi: {hash_type}{Colors.RESET}")
            return hash_type
        else:
            print(f"{Colors.YELLOW}[!] Hash turi aniqlanmadi. Uzunligi: {length}{Colors.RESET}")
            return "Noma'lum"
    
    def crack_md5(self, target_hash, max_length=6):
        print(f"\n{Colors.CYAN}[*] MD5 hash sindirilmoqda: {target_hash}{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Maksimal uzunlik: {max_length}{Colors.RESET}\n")
        
        chars = string.ascii_lowercase + string.digits
        
        for length in range(1, max_length + 1):
            print(f"{Colors.CYAN}[*] Uzunlik tekshirilmoqda: {length}{Colors.RESET}")
            
            for combo in itertools.product(chars, repeat=length):
                word = "".join(combo)
                hash_word = hashlib.md5(word.encode()).hexdigest()
                
                if hash_word == target_hash:
                    print(f"\n{Colors.GREEN}[+] SINDIRILDI!{Colors.RESET}")
                    print(f"{Colors.GREEN}[+] Hash: {target_hash}{Colors.RESET}")
                    print(f"{Colors.GREEN}[+] Parol: {word}{Colors.RESET}")
                    return word
        
        print(f"{Colors.RED}[-] SINDIRILMADI{Colors.RESET}")
        return None
    
    def generate_wordlist(self, min_len, max_len, charset="1234567890", output="wordlist.txt"):
        print(f"\n{Colors.CYAN}[*] Wordlist yaratilmoqda...{Colors.RESET}")
        print(f"{Colors.YELLOW}[*] Min: {min_len}, Max: {max_len}{Colors.RESET}")
        
        count = 0
        with open(output, "w") as f:
            for length in range(min_len, max_len + 1):
                for combo in itertools.product(charset, repeat=length):
                    f.write("".join(combo) + "\n")
                    count += 1
                    if count % 1000000 == 0:
                        print(f"{Colors.DIM}[*] {count} parol yaratildi...{Colors.RESET}")
        
        print(f"{Colors.GREEN}[+] Wordlist yaratildi: {output} ({count} parol){Colors.RESET}")
        return output
