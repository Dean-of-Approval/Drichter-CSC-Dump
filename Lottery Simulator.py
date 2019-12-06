import random
import math
import threading
from os import system, name
rand_correct = False
"""
list of functions
    user_lottery_numbers()
    powerball()
    user_num_check(num1,num2,num3,num4,num5,powerball)
    rand_lottery_numbers(rand_correct)
"""

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def user_lottery_numbers():
    while user_num_test != True:
        print("\033[1;37;40m Please select numbers between 1 and 69 inclusive for the lottery numbers")
        print("and 1 to 26 inclusive for the powerball number")
        num1 = int(input("Please select your first lottery Number:"))
        num2 = int(input("Please select your second lottery Number:"))
        num3 = int(input("Please select your third lottery Number:"))
        num4 = int(input("Please select your fourth lottery Number:"))
        num5 = int(input("Please select your fifth lottery Number:"))
        powerball = int(input("Please select your powerball Number:"))
        if num1<=69 and num2<=69 and num3<=69 and num4<=69 and num5<=69 and powerball<=26:
            if num1>=1 and num2>=1 and num3>=1 and num4>=1 and num5>=1 and powerball>=1:
                user_num_test = True
            else:
                clear()
                print("\033[1;31;40m Please select numbers greater than 0")
        else:
            clear()
            print("\033[1;31;40m Please select numbers less than 70 for the first 5 numbers and 27 for the powerball.")
    
    

   

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
            clear()
            print("\033[1;31;40m Please select numbers greater than 0")
            user_lottery_numbers()
    else:
        clear()
        print("\033[1;31;40m Please select numbers less than 70 for the first 5 numbers and 27 for the powerball.")
        user_lottery_numbers()

def rand_lottery_numbers(rand_correct):
    while rand_correct == False:
        num1 = random.randint(1,69)
        num2 = random.randint(1,69)
        num3 = random.randint(1,69)
        num4 = random.randint(1,69)
        num5 = random.randint(1,69)
        powerball = random.randint(1,26)
        if num1<num2 and num2<num3 and num3<num4 and num4<num5:
            rand_correct = True
        else:
            rand_correct = False
    print ("Your numbers are:",num1,num2,num3,num4,num5,"and your powerball is:",powerball)

userinput = input("Do you want random numbers? Y or N: ")

if userinput.capitalize() == "Y":
    rand_lottery_numbers(rand_correct)
else:
    user_lottery_numbers()






print ("Your numbers are:",num1,num2,num3,num4,num5,"and your powerball is:",powerball)
    user_satisified = input("Are you satisified with you number selections? Y or N")
    return user_satisified