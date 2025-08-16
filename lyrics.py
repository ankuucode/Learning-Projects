from colorama import Fore
import time,os
g=Fore.LIGHTGREEN_EX
m = Fore.LIGHTMAGENTA_EX
b=Fore.LIGHTBLUE_EX
ye=Fore.LIGHTYELLOW_EX
r=Fore.LIGHTRED_EX
c=Fore.LIGHTCYAN_EX
w=Fore.LIGHTWHITE_EX

def ShowLyrics():
    os.system('cls')
    print(f"{r}Wanna Be Your".center(80))
    lyrics={f'{m}Secrets I have held in my heart ❤️\n':1.3,
        f'{c}Are harder to hide than I thought\n':1.25,
        f'{ye}Maybe I just wanna be yours\n':1.2,
        f"{w}I wanna be yours, I wanna be yours\n{w}":1005
    }

    for x,y in lyrics.items():
        for i in x:
            print(i,end='',flush=True)
            time.sleep(0.06)
        time.sleep(y)

ShowLyrics()
