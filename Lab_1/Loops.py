__author__ = 'Yonglin'

'''This file Loops.py will help us practice some loop methods and list comprehension'''

import random

# Question_a: write a loop
print('Question_a: write a loop')
for i in range(5, 11):
    print('The next number in the loop is {}'.format(i))
print('\n')

# Question_b: while loop
random_value = 0 # initializing the random value
print('Question_b: while loop')
while random_value < 0.9:
    random_value = random.uniform(0, 1)
    if random_value >= 0.9: # guarantee the first random value is less than 0.9
        break
    print('The next random value less than 0.9 is {}'.format(random_value))

# Question_c: for-loop which iterates over the list
print('\n')
print('Question_c: for-loop which iterates over the list')
names = ['Ludwig', 'Rosa', 'Mona', 'Amadeus']

for name in names:
    print ('The name {} is nice'.format(name))
# we can use this statement as well
#   print('The name %s is nice'%name)


# Question_d: for loop
# I think list comprehension is more Pythonic and elegant
for index, name in enumerate(names):
    names[index] = len(name)
nLetters_1 = names

print('\n')
print('Question_d: using enumerate()\nThe nLetters list is: {} '.format(nLetters_1))

# Question_e: list comprehensions 1

# I think list comprehension is more Pythonic and elegant
names = ['Ludwig', 'Rosa', 'Mona', 'Amadeus']
nLetters_2 = [len(name) for name in names]

print('\n')
print('Question_e: list comprehension 1\nThe nLetters list is: {} '.format(nLetters_2))

# Question_f: list comprehensions 2
print('\n')
shortLong = ['Short' if len(name) <= 4 else 'Long' for name in names]
print('Question_f: list comprehension 2\nThe shortLong list is: {} '.format(shortLong))

# Question_g: Write a loop that simultaneously loops over the lists
print('\n')
print('Question_g: Write a loop that simultaneously loops over the lists\n')
for name, len_name in zip(names, shortLong):
    print('he name {} is a {} name'.format(name, len_name))