import webbrowser
import sys
import os  
LINK = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
ERROR_COUNT = 0

def input_math():
    global ERROR_COUNT
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == 1: 
                open_video()
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                open_video()
                ERROR_COUNT += 1 
    except:
        ERROR_COUNT -= 1
        pass 

def open_video():
    webbrowser.open(LINK)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")
    os.remove("fakefile.txt") 
    return  
input_math()
