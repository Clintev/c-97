import random 

num = random.randint(1,9)
chances = 0
while chances < 5:
    guess = int(input("Enter a number : "))
    if guess==num:
        print("Congratulations You Won!!")
        break
    elif guess>num:
        print("The number is smaller")
        break
    else:
        print("The number is bigger")
    chances+=1
if chances==5:
    print("You Lost, Try Again")