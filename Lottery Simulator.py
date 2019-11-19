import random
import math
import threading
import pynput


def rand_lottery_numbers():
    num1 = random.randint(1,69)
    num2 = random.randint(1,69)
    num3 = random.randint(1,69)
    num4 = random.randint(1,69)
    num5 = random.randint(1,69)
    powerball = random.randint(1,26)
    print ("Your numbers are:",num1,num2,num3,num4,num5,"and your powerball is:",powerball)

def user_lottery_numbers():
    num1 = int(input("Please select your first lottery Number:"))
    num2 = int(input("Please select your second lottery Number:"))
    num3 = int(input("Please select your third lottery Number:"))
    num4 = int(input("Please select your fourth lottery Number:"))
    num5 = int(input("Please select your fifth lottery Number:"))
    powerball = int(input("Please select your powerball Number:"))
    print ("Your numbers are:",num1,num2,num3,num4,num5,"and your powerball is:",powerball)


user_lottery_numbers()


