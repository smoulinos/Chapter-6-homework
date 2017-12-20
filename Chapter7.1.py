#Question 1 

numberlist = [0,7,15,8,9,56,2,3,13]

def count_odd(numlist):
    count = 0
    for i in numlist:
        if i%2 == 1:
            count +=1
    return count
print(count_odd(numberlist))

#Question 2

def sum_even(numlist):
    sum = 0
    for i in numlist:
        if i%2 == 0:
            sum+=i
    return sum
    
print(sum_even(numberlist))

#Question 3

negativenumberlist = [1,-3,9,-2,-9,6]

def sum_neg(numlist):
    sum = 0
    for i in numlist:
        if i < 0:
            sum +=i
    return sum
print(sum_neg(negativenumberlist))

#Question 4

wordlist = ["cat", "apple", "laptop", "magic"]

def fivewords(list):
    words = 0
    for i in list:
        if 5 == len(i):
            words += 1
    return words
print(fivewords(wordlist))

#Question 5

numberlist = [7,15,8,2,3,13]

def evenfirst(numlist):
    sum=0
    for i in numlist:
        if i % 2 == 0:
            break
        else:
            sum +=i
    return sum

print(evenfirst(numberlist))


#Question 6

samwords = ["name1","name2", "name3", "sam"]
def samfxn(name):
    count =0
    for i in name:
        if i == "sam":
            count += 1
            break
        count +=1
    return count
        
print(samfxn(samwords))
        
#Question 7
n = 25
approx = n/2
while True:
    better = (approx + n/approx)/2.0
    print(better)
    if abs(better - approx) < 0.0000001:
        break
    approx = better     #approx changes every time, not always n/2
    print(better)



#Question 10
    
def is_prime(n):              
    for i in range(2,n):          #prime is only divisible by 1 and itself
        if n % i == 0:
            return False
        return True
    

#Question 11

import turtle
wn = turtle.Screen()
stef = turtle.Turtle()

steps = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (angle, moves) in steps:
    stef.right(angle)
    stef.forward(moves)
    
#Question 12

import turtle
wn = turtle.Screen()
stef = turtle.Turtle()
stef.pensize(10)
house = [(270,50), (30, 50), (120,50), (120,50), (225,70.1), (225,50), (225,70.1), (225,50) ]

for (angle,moves) in house:
    stef.right(angle)
    stef.forward(moves)