from colorama import Fore, Style
from time import sleep

def main():    
    for i in range(10, 6, -1):
        print(Fore.CYAN + Style.BRIGHT + str(i))
        sleep(0.5)
    
    for i in range(6, 3, -1):
        print(Fore.YELLOW + str(i))
        sleep(0.5)

    for i in range(3, 0, -1):
        print(Fore.RED + str(i))
        sleep(0.5)

    print(Fore.GREEN + "Liftoff!" + Style.RESET_ALL)

if __name__ == '__main__':
    main()
