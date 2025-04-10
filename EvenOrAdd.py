from operator import truediv
from os import execv

### version  1

# number = int(input("Enter number to check if its even or odd: "))

# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")
    
### version 2

# Beginner (Boshlang‘ich) - Tasklarx`
# 1.  Son juft yoki toq ekanligini aniqlash:


while True:
    user_input = input("Enter number to check if its even or odd or type 'exit' to stop the program: ")
    if user_input.lower() == "exit":
        print("Exiting program...")
        break
    
    try:
        number = int(user_input)
        if number % 2 == 0:
            print(f"{number} is  even")
        else:
            print(f"{number} is odd")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
