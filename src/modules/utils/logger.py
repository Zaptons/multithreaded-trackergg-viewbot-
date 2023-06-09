import os, platform
from os import system, name
from datetime import datetime
from colorama import Fore, Style
from src.modules.helper.config import Config
from pystyle import Colors, Colorate, Center

# Logo
logo = """
████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗     ██████╗  ██████╗ 
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗   ██╔════╝ ██╔════╝ 
   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝   ██║  ███╗██║  ███╗
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗   ██║   ██║██║   ██║
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║██╗╚██████╔╝╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝  ╚═════╝"""

class Logger:

    def __init__(self):
        
        # Set the colors for the logs
        self.log_types = {
            "INFO": Fore.CYAN,
            "SUCCESS": Fore.GREEN,
            "OK": Fore.GREEN,
            "WARNING": Fore.YELLOW,
            "SLEEP": Fore.YELLOW,
            "ERROR": Fore.RED,
            "BAD": Fore.RED,
            "INPUT": Fore.BLUE,
        }
        self.config = Config()

    # Clear console function
    def clear(self):
        system("cls" if name in ("nt", "dos") else "clear")

    # Function to print the logo when the gen starts
    def print_logo(self):
        self.clear()
        print(Center.XCenter(Colorate.Vertical(Colors.white_to_blue, logo, 1)))
        print(Center.XCenter(Colorate.Vertical(Colors.white_to_blue, "────────────────────────────────────────────\n", 1)))
        print(Center.XCenter(Colorate.Vertical(Colors.white_to_blue, f"Welcome!\n\n", 1)))
        os.system(f"title Tracker.gg View Bot {self.config.build_version} • I'm ready!")

    # Function to log messages to the console
    def log(self, type, message):
        color = self.log_types[type]
        now = datetime.now()
        current_time = now.strftime("%d/%m/%Y • %H:%M:%S")
        print(f"{Style.DIM}{current_time} • {Style.RESET_ALL}{Style.BRIGHT}{color}[{Style.RESET_ALL}{type}{Style.BRIGHT}{color}] {Style.RESET_ALL}{Style.BRIGHT}{Fore.WHITE}{message}")

    def change_title(self, title):
        if platform.system() == 'Windows':
            os.system(f'title {title}')
        elif platform.system() == 'Linux':
            os.system(f'echo -ne "\033]0;{title}\007"')