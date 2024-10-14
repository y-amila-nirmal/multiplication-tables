YELLOW = '\033[33m' # orange on some systems
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BRIGHT_GREEN = '\033[92m'

RESET = '\033[0m' # called to return to standard terminal text color

print(YELLOW + "yellow" + RESET)
print(MAGENTA + "magenta" + RESET)
print(CYAN + "cyan" + RESET)
print(BRIGHT_GREEN + "bright green" + RESET)

while True:
    multiply_number = int(input(YELLOW + "Enter a number: "))
    multiply_range = int(input("Enter a range: "))
    print(" ")
    for i in range(multiply_range):
        print(f"{RESET}{CYAN}{multiply_number} x {i + 1}{MAGENTA} = {BRIGHT_GREEN}{multiply_number * (i + 1)}{RESET}")    
    print(RESET +" ")
print("Bye!")