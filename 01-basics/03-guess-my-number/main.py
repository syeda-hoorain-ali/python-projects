from colorama import Fore, Style, Back
import random

def main():
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT + "            Guess My Number            ")
    print(Style.RESET_ALL + Fore.MAGENTA + "I am thinking of a number between 0 and 99...")
    
    number: int = random.randint(0, 99)
    user_guess = int(input(Fore.CYAN + Style.BRIGHT + "\nEnter a guess: " + Style.RESET_ALL))

    while user_guess != number:
        if user_guess > number:
            print(Fore.YELLOW + "Your guess is too high")
        else:
            print(Fore.RED + "Your guess is too low")
        user_guess = int(input(Fore.CYAN + Style.BRIGHT + "\nEnter a new number: " + Style.RESET_ALL))
    print(Fore.GREEN + f"Congrats! The number was: {user_guess}", Style.RESET_ALL)


if __name__ == '__main__':
    main()
