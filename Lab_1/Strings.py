__author__ = 'Yonglin'

'''This file Strings.py will help us practice some basic methods of Strings'''
import re

# define parrot
parrot = 'It is dead, that is what is wrong with it'
print('Question_a: define the variable parrot containing the sentence "{}"\n'.format(parrot))

# count the number of the characters of parrot
characters_number = len(parrot)
print('Question_b: The number of characters is {}\n'.format(characters_number))

# count the number if the letters
letters = re.sub(',','',parrot)
letters = re.sub(' ','_',letters)
len_letters = len(re.sub('_','',letters))
print('Question_c: The number of letters is {}\n'.format(len_letters))

# the list of words
ParrotWords = letters.split('_')
print('Question_d: The words list is: ',ParrotWords,'\n')

# merge ParrotWords into a sentence
sentence = ' '.join(ParrotWords)
print('Question_e: Merge ParrotWords into a sentence "{}"\n'.format(sentence))