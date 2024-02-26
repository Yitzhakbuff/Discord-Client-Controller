import requests
import os
from datetime import datetime

# Para imprimir de forma colorida
def debug(response):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y - %H:%M:%S")
    print(f"\033[0;32m{date_time}\033[0m \033[1;34m| DEBUG   |\033[0m \033[1;32mstatus-code:{response.status_code}\033[0m - \033[1;33m{response.elapsed}\033[0m - Request to: \033[1;36m{response.url}\033[0m")

def inputx(prompt):
    print(f"\033[1;32m{prompt}\033[0m", end="")
    user_input = input()
    print(f"\033[1;36m{user_input}\033[0m")
    return user_input

def info(texto):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y - %H:%M:%S")
    print(f"\033[0;32m{date_time}\033[0m \033[1;35m| INFO    |\033[0m \033[1;37m{texto}\033[0m")

def error(texto):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y - %H:%M:%S")
    print(f"\033[0;32m{date_time}\033[0m \033[1;31m| ERROR   |\033[0m \033[1;37m{texto}\033[0m")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
