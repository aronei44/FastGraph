from colorama import Fore
from datetime import datetime


class Logger:
    
    @staticmethod
    def info(message: str):
        print(Fore.GREEN + f'INFO: {message}')

    @staticmethod
    def error(message: str):
        print(Fore.RED + f'ERROR: {message}')
    
    @staticmethod
    def warning(message: str):
        print(Fore.YELLOW + f'WARNING: {message}')

    @staticmethod
    def debug(message: str):
        print(Fore.BLUE + f'DEBUG: {message}')

    @staticmethod
    def log():
        print(Fore.WHITE + f'================ {datetime.now()} ================')

