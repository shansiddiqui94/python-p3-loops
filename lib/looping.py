#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
        print("Happy New Year!")
    
def square_integers(int_list): 
    squared_list = []  # Initialize an empty list to store squared elements
    for num in int_list:
        squared_list.append(num ** 2)  # Square each integer and append to the squared_list
    return squared_list

   

def fizzbuzz():
     for num in range(1, 101):  # Iterate over numbers from 1 to 100
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

   
   
 
