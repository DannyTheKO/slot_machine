# Write code below 💖
import random

symbols = ['🍒',' 🍇', '🍉', '7']
def play():
    result = random.choices(symbols, k = 3)
    # result = ['7','7','7']

    display_result = '|'.join(result)
    print(display_result)

    if result[0] == result[1] == result[2] == '7':
        print("Jackpot!!!")
    elif result[0] == result[1] == result[2]:
        print("You Win!!!")
    else:
        print("Try Again!")

def input_func():
    user_input = input("Do you want to play again? (Y or N): ")
    return user_input


input_result = "Y"
while input_result != "N":
    play()
    input_result = input_func()


print("Thanks for playing!")