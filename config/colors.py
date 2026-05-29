# MAXA.UZ - Color Configuration
# =============================

import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

class Colors:
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    BLACK = Fore.BLACK
    
    B_RED = Back.RED
    B_GREEN = Back.GREEN
    B_YELLOW = Back.YELLOW
    B_BLUE = Back.BLUE
    
    BOLD = Style.BRIGHT
    DIM = Style.DIM
    NORMAL = Style.NORMAL
    RESET = Style.RESET_ALL

def banner():
    return f"""
{Fore.RED}{Style.BRIGHT}
    ███╗   ███╗ █████╗ ██╗  ██╗ █████╗   ██╗   ██╗███████╗
    ████╗ ████║██╔══██╗╚██╗██╔╝██╔══██╗  ██║   ██║╚══███╔╝
    ██╔████╔██║███████║ ╚███╔╝ ███████║  ██║   ██║  ███╔╝ 
    ██║╚██╔╝██║██╔══██║ ██╔██╗ ██╔══██║  ██║   ██║ ███╔╝  
    ██║ ╚═╝ ██║██║  ██║██╔╝ ██╗██║  ██║  ╚██████╔╝███████╗
    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═════╝ ╚══════╝
    {Fore.YELLOW}HAQIQIY HAKERLAR UCHUN TERMINAL
{Fore.RESET}"""
