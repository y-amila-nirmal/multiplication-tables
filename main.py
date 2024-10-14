YELLOW = '\033[33m' 
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BRIGHT_GREEN = '\033[92m'

RESET = '\033[0m'

while True:
    multiply_number = int(input(YELLOW + "Enter a number: "))
    multiply_range = int(input("Enter a range: "))
    print(" ")
    for i in range(multiply_range):
        print(f"{RESET}{CYAN}{multiply_number} x {i + 1}{MAGENTA} = {BRIGHT_GREEN}{multiply_number * (i + 1)}{RESET}")    
    print(RESET +" ")
print("Bye!")