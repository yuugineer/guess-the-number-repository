import random
import sys

def get_valid_number(prompt,min_value=None, max_value=None):
    while True:
        sys.stdout.buffer.write(prompt.encode())
        sys.stdout.flush()
        input_value = sys.stdin.buffer.readline().strip()
        if input_value.isdigit():
            number = int(input_value)
            if(min_value is None or number >= min_value) and (max_value is None or number<= max_value):
                return number
        sys.stdout.buffer.write(b"Invalid input. Please try again. \n")
        sys.stdout.flush() 

n = get_valid_number("Enter the minimum number (n):")

m = get_valid_number(f"Enter the maximum number(m, must be >= {n}):", min_value = n)

secret_number = random.randint(n,m)

sys.stdout.buffer.write(f"I'm thinking of a number between {n} and {m}. Can you guess it? \n".encode())
sys.stdout.flush()

attempts = 0
while True:
    attempts += 1
    guess = get_valid_number(f"Attempt {attempts}. Your guess:", min_value=n,max_value=m)

    if guess < secret_number:
        sys.stdout.buffer.write(b"Too low Try a higher number.\n")
    elif guess > secret_number:
        sys.stdout.buffer.write(b"Too High! Try a lower number \n")
    else:
        sys.stdout.buffer.write(f"Congatulations! You've guessed the number {secret_number} correctly in {attempts} attempts! \n".encode())
        break
    sys.stdout.flush()

sys.stdout.flush()



