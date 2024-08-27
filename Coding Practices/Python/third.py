"""Create a program that generates 100 random numbers and find the frequency of each number"""
import random

rand_num = []
frequency = {i: 0 for i in range(1, 11)}
for i in range(100):
    num = random.randint(1, 10)
    rand_num.append(num)
    frequency[num] += 1 

print(frequency)


