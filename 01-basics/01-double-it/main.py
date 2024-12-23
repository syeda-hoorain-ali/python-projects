from colorama import Fore, Style

def main():
    user_input: int = int(input(Fore.CYAN + Style.BRIGHT + "Enter a number: " + Style.RESET_ALL))
    curr_value: int = user_input

    while curr_value < 100:
        curr_value = curr_value * 2
        print(Fore.MAGENTA + str(curr_value))

    print(Style.RESET_ALL)

if __name__ == '__main__':
    main()
