import os
import string
import random
import logging
import requests
import threading
from colorama import Fore
from slowprint.slowprint import slowprint as sp

loop = True
valid = 0
valid_codes = []
invalid = 0
invalid_codes = []
code = 0
codes = [200, 201, 204]
log = logging.info

os.system('cls')
sp(f'Generator + Checker Made By iku#1400 / 15yrold.\n', 0.2)
amount_of_codes = int(input('Amount Of Codes: '))

logging.basicConfig(
    level = logging.INFO,
    format = f'{Fore.LIGHTBLUE_EX}[{Fore.RESET}%(asctime)s{Fore.LIGHTBLUE_EX}] %(message)s{Fore.RESET}',
    datefmt = '%H:%M:%S'
)

def cls():
    os.system('cls')

def title_change():
    os.system('title Valid: {} - Invalid: {}'.format(valid, invalid))

def close():
    save_invalid_codes = input('Save Invalid Codes? (Y/N): ')
    if save_invalid_codes == 'y' or save_invalid_codes == 'Y' or save_invalid_codes == 'Yes' or save_invalid_codes == 'yes':
        for invalid_code in invalid_codes:
            with open('invalid-codes.txt', 'a', encoding = 'UTF-8') as f:
                f.write('https://discord.gift/' + invalid_code + '\n')
    elif save_invalid_codes == 'n' or save_invalid_codes == 'N' or save_invalid_codes == 'No' or save_invalid_codes == 'no':
        if valid > 1:
            save_valid_codes = input('Save Valid Codes? (Y/N): ')
            if save_valid_codes == 'y' or save_valid_codes == 'Y' or save_valid_codes == 'Yes' or save_valid_codes == 'yes':
                for valid_code in valid_codes:
                    with open('valid-codes.txt', 'a', encoding = 'UTF-8') as f:
                        f.write('https://discord.gift/' + valid_code + '\n')
            elif save_valid_codes == 'n' or save_valid_codes == 'N' or save_valid_codes == 'No' or save_valid_codes == 'no':
                os._exit(1)

def code_gen():
    global valid
    global invalid
    global code
#    while loop:
#        title_change()
#        for i in range(1):
    for i in range(int(amount_of_codes)):
        title_change()
        nitro_code = ''.join(random.choices(string.ascii_letters + string.digits, k = 16))
        code = code + 1
        r = requests.get(f'https://discordapp.com/api/v9/entitlements/gift-codes/{nitro_code}?with_application=false&with_subscription_plan=true')
        if r.status_code in codes:
            valid = valid + 1 
            valid_codes.append(nitro_code)
            log(f'Valid Code Generated: {nitro_code} | {Fore.GREEN}Valid: {Fore.LIGHTGREEN_EX}{valid} / {Fore.RED}Invalid: {Fore.LIGHTRED_EX}{invalid} | Code Number: {code}')
        elif r.status_code not in codes:
            invalid = invalid + 1
            invalid_codes.append(nitro_code)
            log(f'{Fore.RED}Invalid{Fore.LIGHTBLACK_EX}: {Fore.LIGHTBLUE_EX}{nitro_code} {Fore.RESET}| {Fore.GREEN}Valid{Fore.LIGHTBLACK_EX}: {Fore.LIGHTGREEN_EX}{valid} {Fore.RESET}/ {Fore.RED}Invalid{Fore.LIGHTBLACK_EX}: {Fore.LIGHTRED_EX}{invalid} {Fore.RESET}| {Fore.LIGHTYELLOW_EX}Code Number{Fore.LIGHTBLACK_EX}: {Fore.LIGHTYELLOW_EX}{code}')
        if code == amount_of_codes:
            close()
        
#def start_threading():
#    for i in range(10):
#        threading.Thread(target = code_gen).start()

if __name__ == '__main__':
    cls()
    code_gen()
