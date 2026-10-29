
# Create a simple umber guessing game using while loop.The program should make use ofsatements such as else,break,continue


import random

secret_number = random.randint(1,10)
attempts = 3

while attempts >0:
    guess = int(input("Guess a number between 1 and 10:"))

    if guess < 1 or guess > 10:
        print("Invalid guess! Enter a number between 1 and 10.")
        continue
    if guess == secret_number:
        print("Congratulatios! You guessed the correct number!")
        break
    elif guess > secret_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")

    attempts -=1
    print("Attempts remaining:", attempts)

else:
    print("Better luck next time!")
    print("The correct number was:", secret_number)



#Create a multiplication table(from 1 to 10) for given number using a for loop and range function

number = int(input("Enter the number:"))
for i in range(1,11):
    result = number * i
    print(number,"x",i,"=",result)

#Create a python function that calculates the Body Mass Index(BMI)

def calculate_bmi(weight,height):
    bmi = weight/(height **2)
    return bmi
weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))
bmi = calculate_bmi(weight,height)
print("Your BMI is:",round(bmi,2))
