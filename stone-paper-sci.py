import random,time,os
try: 
    import pyfiglet
except:
    os.system("pip install pyfiglet")
    import pyfiglet
# s-stone
# p-paper
# k-scissor
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
white = "\033[1m\033[37m"

def logo(name):
    banner = pyfiglet.figlet_format(name, font="slant")
    print(f"{green}_______________________________")
    print(f"\033[1m\033[31m{banner}\033[0m") 
    print(f"{yellow}Code Dev: @AnkuCode\n")
    print(f"{yellow}Telegram: @AnkuCode\n")
    print(f"{green}_______________________________")
 


def sps(uchoice: str, name: str):

    rc = ['s', 'k', 'p']  
    cchoice = random.choice(rc) 
    valid_choices = {'s': 'stone', 'p': 'paper', 'k': 'scissor'}

    us_choice = valid_choices[uchoice.lower()] 
    comp_choice = valid_choices[cchoice.lower()]  

    if us_choice == comp_choice:
        print(f'{cyan}You Choose: {yellow}{us_choice}\n{red}Computer choose: {yellow}{comp_choice}{white}\n{green}- So it\'s a Draw!')

    elif (us_choice == 'scissor' and comp_choice == 'paper') or \
         (us_choice == 'stone' and comp_choice == 'scissor') or \
         (us_choice == 'paper' and comp_choice == 'stone'):
        print(f'{cyan}You Choose: {yellow}{us_choice}\n{red}Computer choose: {yellow}{comp_choice}{white}\n{green}- So {name} Wins!')

    else:
        print(f'{cyan}You Choose: {yellow}{us_choice}\n{red}Computer choose: {yellow}{comp_choice}{white}\n{red}- So {name} Loss!')

logo("AnkuCode")
text='Welcome to stone paper scissor Game By @Ankucode\n'
for i in text:
    print(red+i,end='',flush=True)
    time.sleep(0.03)
            
def main():
    name=input(f"{yellow}Enter Your Name: {green}")

    print(f"{white}Welcome {name} Lets start the game,please choose one: ")
    while True:
        

        choice=['p','k','s']

        print(f'{red}s {white}={white}{yellow}Stone {white}')
        print(f'{red}p{white} = {white}{yellow}Paper{white}')
        print(f'{red}k{white} = {white}{yellow}Scissor{white}')
        ch = input(f"{yellow}Enter p/k/s or q to exit >> {white}\n").lower()
        
        if ch == 'q':
            print(f"{yellow}Exiting the game! Goodbye!{white}")
            break 
        
        elif ch in choice:
            sps(ch,name)  
        else:
            print(f'{red}Please choose p/k/s, none other than this{white}')
            continue
        # os.system('cls||clear')


main()

        





