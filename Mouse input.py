from time import sleep 
from pynput.mouse import Listener
from os import system, name 

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
  

def on_move(x,y):
    clear()
    print(x,y)
    

def on_click(x,y,button,pressed):
    clear()
    print(x,y,button,pressed)
    

def on_scroll(x,y,dx,dy):
    clear()
    print((x,y,dx,dy))
    

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()