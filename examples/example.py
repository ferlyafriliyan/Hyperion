import os, sys

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

def hello():
    myname = ", I am Ferly Afriliyan ! "
    project = "and I just finished creating a python project to Obfuscate Python3 files which is quite difficult to Reverse"
    print("Hello world", myname)
    print(project)
    
if __name__ == '__main__':
    clear();hello()
    