import os,random

def clear():
    return os.system("clear")


# let's make a command that checks for system updates why not ;)
def update():
    return os.system("sudo pacman -Sy")

def adder():
    a = int(input("Give me a number to add it with another random number : "))
    return ("the results are: ", a + random.randint(1 , 9))

adder()
input("press enter to clear the screen")
clear()
input("Now checking for updates")
update()
input("system update is done press enter to clear the screen")
clear()
input("Now press enter to exit the program")
