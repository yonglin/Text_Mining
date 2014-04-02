__author__ = 'Yonglin'
'''This file Vectors.py will help us practice some array methods in numpy'''

# Question_a: Define two lists
list1 = [1, 3, 4]
list2 = [5, 6, 9]
print('Question_a: We use "try-except statement" to test whether it is possible to multiply two number lists directly\n')
try:
    list1 * list2
except:
    print('We cannot multiply two number lists directly!\n')

# Question_b: Convert list1 and list2 into arrays
from numpy import array
array1 = array(list1)
array2 = array(list2)

print('Question_b: array1*array2 is: {}'.format(array1 * array2))
print('Now we know that it is element-wise multiplication\n')

# Question_c: Matrix
from numpy import diag
matrix1 = array([array1, array2])
matrix2 = diag(array([1, 2, 3]), k = 0)
print('matrix1 is:')
print(matrix1)
print('\n')
print('matrix2 is:')
print(matrix2)

print('Question_c: We use "try-except statement" to test whether it is possible to multiply matrix1 with matrix2\n')
try:
    matrix1 * matrix2
except:
    print('We cannot multiply matrix1 with matrix2 directly! Because array multiplication is element-wise!\n')

# Question_d: Compute the usual matrix product

print('Question_d: We use "dot" from numpy to do the product of matrix1 and matrix2\n')
from numpy import dot
print('The product of matrix1 and matrix2 is: ')
print(dot(matrix1, matrix2))