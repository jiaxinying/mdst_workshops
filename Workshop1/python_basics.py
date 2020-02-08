"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import numpy as np
import random
import base64
def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if num%2==0:
        print('even!')
    else:
        print('odd!')



def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    target=random.randint(1,9)
    value=input('Please guess a number:')
    while value!='exit':
        if int(value)<target:
            print('too low.')
        if int(value)>target:
            print('too high.')
        if int(value)==target:
            print('exactly right.')
        value=input('Please guess a number:')


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    length=len(string)
    for i in range(length//2):
        if string[i]!=string[length-1-i]:
            print("not a palindrome")
            return
    print("palindrome")




def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    encodedBytes_username=base64.b64encode(username.encode("utf-8"))
    encodedStr_username=str(encodedBytes_username,'utf-8')
    encodedBytes_password = base64.b64encode(password.encode("utf-8"))
    encodedStr_password = str(encodedBytes_password, 'utf-8')
    f=open(filename,"a")
    f.write(encodedStr_username)
    f.write('\n')
    f.write(encodedStr_password)



def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    f=open(filename,"r")
    user_de=f.readline()
    password_de=f.readline()
    print(base64.b64decode(user_de))
    print(base64.b64decode(password_de))
    if password!=None:
        f=open(filename,"r")
        lines=f.readlines()
        f=open(filename,"w")
        f.writelines([item for item in lines[:-1]])
        encodedBytes_password = base64.b64encode(password.encode("utf-8"))
        encodedStr_password = str(encodedBytes_password, 'utf-8')
        f.write(encodedStr_password)


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    #part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
