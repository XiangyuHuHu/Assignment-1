# Xiangyu Hu
# CSC673 A1
# Assignment 1
import sys


def print_helloworld():
    print('Hello World')

def print_multiplication_table(num):
    for num1 in range(1,num+1):
        for num2 in range(1,num+1):
            print(num1,"x",num2,"=",num1*num2)

def is_palindrome(str):
    oldstr = str
    newstr = ""
    for let in oldstr:
        newstr = let + newstr
    if(oldstr==newstr):
        print("it's palindrome")
    else:
        print("not palindrome")

def alternatingly_element(arr1,arr2):
    newarr = []
    for x in range(len(arr1)):
        newarr.append(arr1[x])
        newarr.append(arr2[x])
    return newarr

def fibonacci_num():
        # return fibonacci_num(num-2) + fibonacci_num(num-1)
    first = 0
    second = 1
    x = 99
    while x !=0:
        next = first + second
        first = second
        second = next
        x-=1
    return second

def is_leapyear(year):
    if year%4 == 0:
        return True
    else:
        return False



if __name__ == "__main__":
    # print_helloworld()
    # is_palindrome("hellop")
    # is_palindrome("kook")
    # print_multiplication_table(12)
    # arr1 = ["a", "b", "c"]
    # arr2 = [1,2,3]
    # print(alternatingly_element(arr1,arr2))
    print(fibonacci_num())
    # year = 2023
    # print(is_leapyear(year))
    # year2 = 2024
    # print(is_leapyear(year2))

