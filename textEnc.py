
# Lets Make a text Encryptor and Decryptor
import os
from colorama import Fore
red=Fore.LIGHTRED_EX
green=Fore.LIGHTGREEN_EX
cyan=Fore.LIGHTCYAN_EX
yellow=Fore.LIGHTYELLOW_EX
a='#'
i="/"
b='A'
c="1"
z="|"
o="_"
w="+"
x=">"
def encryptor():
    #text
    text=input(f'\n\n{red}Enter Text: {yellow} ').lower()
    first=text[::-1]
    first=first.replace('a',a)
    first=first.replace('i',i)
    first=first.replace("b",b)
    first=first.replace('c',c)
    first=first.replace('z',z)
    first=first.replace('x',x)
    first=first.replace('o',o)
    first=first.replace(',',w)
    return first



def decryptor():
    text = input(f'\n\n{red}Enter Encrypted Text: {green}')
    first = text.replace(a, 'a')
    first = first.replace(i, 'i')
    first = first.replace(b, 'b')
    first = first.replace(c, 'c')
    first = first.replace(z, 'z')
    first = first.replace(x, 'x')
    first=first.replace(w,'w')
    first= first.replace(o,'o')
    original = first[::-1]
    return original

while True:

    print(f"{cyan}Welcome to Text Encryptor and Decryptor")
    choice= input("Please select:\n 1 for enc\n 2 for Dec\n===>")
    if choice=='1':
        e=encryptor()
        print(green+'Your Encoded text: '+red,e)
        ch=input(f"{cyan}do you want to continue? y/n \n--->Enter: ")
        if ch.lower()=='n':
            print(f"{green}thanks for using")
            break
        else:
            os.system("cls")
            continue
    elif choice =='2':
        d=decryptor()
        print(f'{green}original text: {yellow}',d)
        ch=input(f"{red}do you want to continue? y/n \n--->Enter: ")
        if ch.lower()=='n':
            print(green+"thanks for using")
            break
        else:
            os.system("cls")
            continue
    else:
        print(red+"not valid")
        break