import random
import math
import threading


def rand_lottery_numbers():
    num1 = random.randint(1,69)
    num2 = random.randint(1,69)
    num3 = random.randint(1,69)
    num4 = random.randint(1,69)
    num5 = random.randint(1,69)
    powerball = random.randint(1,26)
    print ("Your numbers are:",num1,num2,num3,num4,num5,"and your powerball is:",powerball)

def user_lottery_numbers():
    print("Please select numbers between 1 and 69 inclusive for the lottery numbers")
    print("and 1 to 26 inclusive for the powerball number")
    num1 = int(input("Please select your first lottery Number:"))
    num2 = int(input("Please select your second lottery Number:"))
    num3 = int(input("Please select your third lottery Number:"))
    num4 = int(input("Please select your fourth lottery Number:"))
    num5 = int(input("Please select your fifth lottery Number:"))
    powerball = int(input("Please select your powerball Number:"))
    print ("Your numbers are:",num1,num2,num3,num4,num5,"and your powerball is:",powerball)

def powerball():
    num11 = random.randint(1,69)
    num21 = random.randint(1,69)
    num31 = random.randint(1,69)
    num41 = random.randint(1,69)
    num51 = random.randint(1,69)
    powerball1 = random.randint(1,26)

def user_num_check(num1,num2,num3,num4,num5,powerball):
    if num1<=69 and num2<=69 and num3<=69 and num4<=69 and num5<=69 and powerball<=26:
        if num1>=1 and num2>=1 and num3>=1 and num4>=1 and num5>=1 and powerball>=1:
            return True
        else:
            return False
    else:
        return False

user_lottery_numbers()