__author__ = 'Yonglin'
'''This file Dictionaries.py will help us practice some Dictionary methods'''

import random

# Question_a: Make a dictionary named Amadeus
print('Question_a: Make a dictionary named Amadeus')
Amadeus = {'Sex': 'M', 'Algebra': 8, 'History': 13}
print(Amadeus)
print('\n')

# Question_b: Make three more dictionaries
print('Question_b: Make three more dictionaries')
Rosa = {'Sex': 'F', 'Algebra': 19, 'History': 22}
Mona = {'Sex': 'F', 'Algebra': 6, 'History': 27}
Ludwig = {'Sex': 'M', 'Algebra': 9, 'History': 5}

print(Rosa, Mona, Ludwig)
print('\n')

# Question_c: Combine the four students in a dictionary named students
students = {'Amadeus': Amadeus, 'Rosa': Rosa, 'Mona': Mona, 'Ludwig': Ludwig}
print('Question_c: Combine the four students in a dictionary named students')
print ('Amadeus got {} scores of History'.format(students['Amadeus']['History']))

# Question_d: Add the new student Karl to the dictionary students
print('\n')
Karl = {'Sex': 'M', 'Algebra': 14, 'History': 10}
students['Karl'] = Karl
print('Question_d: Add the new student Karl to the dictionary students')
for item in students.items():
    print('%7s %s %2d %2d' %(item[0], item[1]['Sex'], item[1]['Algebra'], item[1]['History']))

# Question_e: Use for-loop to print out the names and scores of all students on the screen.
print('\n')
print('print out the names and scores of all students: ')
for item in students.items():
    print('Student %7s socred %2d on the Algebra exam and %2d on the History exam' % (item[0], item[1]['Algebra'], item[1]['History']))