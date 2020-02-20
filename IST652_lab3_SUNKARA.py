# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:58:33 2019

@author: KARTHEEK
"""
#( 1a ) Show the expression that fetches the value of the stock dictionary at the key orange 
stock = {"banana": 6,"apple": 0,"orange":32,"pear": 15,"avacado": 3,"mango": 5}
prices={"banana":4,"apple":2,"orange":1.5,"pear":3,"avacado":10,"mango":1}

stock["orange"]

#( 1b ) Show a statement that adds an item to the stock dictionary called \"cherry\" with some integer value AND that adds <i><u>cherry</u></i> to the prices dictionary with a numeric value. \n",
#"- <i>Or pick your own fruit name.</

#Adding new item cherry to both the dictionaries with values
stock["cherry"]=12
prices["cherry"]=6

#( 2 ) Write the code for a loop that iterates over the stock dictionary and prints each key and value. 
#unpacking keys and corresponding values of stock dictionary into variables key and value respectively
for key,value in stock.items():
    print(key,value)

#( 3 ) Write the code that will sum the total number in stock for all the items in the groceries list and prints this value to console
groceries = ['apple', 'banana', 'pear']
sum=0
for x in groceries:
    sum+=stock[x] #sum = sum + stock[x]
print('The total number in stock for all the items in the list is'+' '+str(sum))

#( 4 ) Write the code that can print out the total value of in-stock items. 
a=[]
for key,value in stock.items():
    a.append(prices[key]*value)
    
#( 5)
guessesTaken=0
import random
number=random.randint(1,20)
print('I am thinking of a number between 1 and 20.')
while guessesTaken < 6:
    print('Take a guess')
    try:
        guess=int(input())
    except ValueError:
        print("Sorry this is not a number. Try Again")
        continue
    guessesTaken=guessesTaken+1
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.') 
    if guess == number:
        break
    

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job - You guessed my number in ' + guessesTaken + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)


# The input is taken in the try block. As integer is expected as input, if a string is given then ValueError is 
    #thrownwhich is handled in except
#Continue takes to the start of while loop if the except statement is executed
    
    
