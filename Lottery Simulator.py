import random
import math
import threading
import pynput


def lottery_numbers():
    while True:
        num1 = random.randint(1,63)
        num2 = random.randint(1,63)
        num3 = random.randint(1,63)
        num4 = random.randint(1,63)
        num5 = random.randint(1,63)
        powerball = random.randint(1,26)
        print (num1,num2,num3,num4,num5,powerball)


lottery_numbers()


