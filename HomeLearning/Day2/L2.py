#while loop
#Loop over a list without using for loop
def printwwhileloop(l):
    i = 0
    while i != len(l):
        print(l[i])
        i += 1

print(printwwhileloop([1,2,3,4,5,6,7]))

#Given a number k, write a function calculate consecutive sum and stop when the sum is larger than k
def consum(k):
    total = 0
    addedvalue = 1
    while total < k:
        total += addedvalue
        addedvalue += 1
    return total

print(consum(11))
print(consum(100))

#Given a list of string, loop through the list and add ! to each string and stop when an element in string is empty
def strlist(input_list,char):
    i = 0
    while i != len(input_list) and input_list[i] != '':
        input_list[i] += char
        i += 1
    return input_list
    
print(strlist(['hello','world','a','b','c'],'!'))
print(strlist(['hello','world','a','','c'],'!'))

#Write a program calculating factorial of a number n
def factorial(n):
    product = 1
    num = 1
    while num <= n:
        product = product * num
        num += 1
    return product

print(factorial(3))

#Given a k number which is the times 3 dices are thrown, write a program calculating the probability of all 3 dices having 6
import random

def simulation_dice(k):
    times = 0
    all_get_six = 0
    while times <= k:
        a = (random.randint(1,6))
        b = (random.randint(1,6))
        c = (random.randint(1,6))
        if a == b == c == 6:
            all_get_six += 1
        times += 1
    prob = all_get_six/k
    return prob

print(simulation_dice(1000000))

#Given a k number of times running though a simulation, each simulation will stop when 3 dices have 6
def simulation2(k):
    simu_times = 0
    prob = 0
    while simu_times <= k:
        a = 0
        b = 0
        c = 0
        throw_times = 0
        while a != 6 or b != 6 or c != 6:
            a = random.randint(1,6)
            b = random.randint(1,6)
            c = random.randint(1,6)
            throw_times += 1
        prob += 1/throw_times
        simu_times += 1
    avg = prob/k
    return avg

print(simulation2(1000000))