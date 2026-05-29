# MAXA.UZ - Settings
# ==================

import os

class Settings:
    # Loyiha papkasi
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Output papkasi
    OUTPUT_DIR = os.path.join(BASE_DIR, "output")
    
    # Wordlist papkasi
    WORDLIST_DIR = os.path.join(BASE_DIR, "wordlists")
    
    # Asosiy wordlist
    DEFAULT_WORDLIST = os.path.join(WORDLIST_DIR, "default.txt")
    
    # Timeout
    TIMEOUT = 10
    
    # User Agent
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    
    # OSINT saytlari
    OSINT_SITES = [
        "Facebook", "Instagram", "Twitter", "Telegram",
        "GitHub", "GitLab", "Reddit", "Pinterest",
        "TikTok", "YouTube", "Snapchat", "LinkedIn",
        "VK", "OK", "WhatsApp", "Signal",
        "Discord", "Twitch", "Steam", "Spotify",
        "Blogger", "WordPress", "Medium", "Quora",
        "Flickr", "DeviantArt", "Behance", "Dribbble",
        "Patreon", "OnlyFans", "CashApp", "Venmo",
        "PayPal", "Ebay", "Amazon", "Alibaba",
        "Roblox", "Fortnite", "Minecraft", "Origin",
        "Xbox", "PlayStation", "Nintendo", "BattleNet"
    ]
    
    # Portlar
    COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080, 8443]
    
    # Hash turlari
    HASH_MODES = {
        "MD5": 0,
        "SHA1": 100,
        "SHA256": 1400,
        "SHA512": 1700,
        "NTLM": 1000,
        "bcrypt": 3200,
        "WPA2": 2500,
        "MySQL": 300
    }

os.makedirs(Settings.OUTPUT_DIR, exist_ok=True)
os.makedirs(Settings.WORDLIST_DIR, exist_ok=True)
