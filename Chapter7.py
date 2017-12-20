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
        
