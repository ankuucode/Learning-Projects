import random as r
import time
import os

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

passw = input(f"{YELLOW}Enter Your 1-6 digit pass: {BLUE}")
if len(passw) <= 6:
    try:
        inn = int(passw)
        print(f"{GREEN}Character in limit proceeding next...{RESET}")
        time.sleep(1)
    except ValueError:
        print(f"{RED}Invalid input! Please enter a numeric password.{RESET}")
        exit()
else:
    print(f"{RED}Only valid till 6 digit{RESET}")
    exit()
os.system("cls||clear")
def Crack(psw):
    lists = [
        (len(psw) == 2, (0, 99)),
        (len(psw) == 3, (99, 999)),
        (len(psw) == 4, (999, 9999)),
        (len(psw) == 5, (9999, 99999)),
        (len(psw) == 6, (99999, 999999))
    ]
    for i, j in lists:
        if i:
            return j
stime = time.time()
i = 0
while True:
    i += 1
    a, b = Crack(passw)
    guess = r.randint(a, b)
    print(f"\r{BLUE}Try: {RED}{guess}{BLUE} for {RED}{i} {BLUE}attempts{RESET}", end='', flush=True)
    if guess == inn:
        ttake = time.time() - stime
        print(f'\n\n{GREEN}Finally cracked the password:\n {RED}Attempt Taken: {YELLOW}{i}.{RESET}')
        print(f"{RED}Password is: {YELLOW}{guess}")
        print(f"{RED}Time taken:{YELLOW} {ttake:.2f} seconds{RESET}")
        break
