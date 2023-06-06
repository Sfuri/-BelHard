import itertools
import random
import numpy as np

# colors = ('red','green','blue','white')
# print (list(itertools.combinations(colors,3)))

# def flavor (n,t):
#     chance = 1-(((n-1)/n) ** t)
#     return chance

# ls = ('girl','boy')
# both = 0
# neither = 0
# either = 0
# for i in range(10000):
#     older = random.choice(ls)
#     younger = random.choice(ls)
#     if older =='girl'  and younger == 'girl':
#         both +=1
#     elif older or younger == 'girl':
#         either +=1
#     else: neither +=1
#
# print(both)

# class vector:
#     ls : list
#     def __init__(self,ls):
#         self.ls = ls
#     def __add__(self, other):
#         new_ls = []
#         for i, j in zip(self.ls, other.ls):
#             new_ls.append(i + j)
#         return new_ls
#
# vector1 = vector([1,2,3])
# vector2 = vector([5,6,7])
# print (vector1 + vector2)

# A = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# def matrix_magick(n):
#     B = np.transpose(n)
#     C = n * B
#     return C
# print(matrix_magick(A))


array1 = np.random.randint(10, size=(3, 3))
t_array = np.transpose(array1)
std_deviation = np.std(array1)
determinant = np.linalg.det(array1)

array2 = np.random.randint(10, size=(3, 3))
array2_sum = np.sum(array2)
array2_min = np.min(array2)
array2_max = np.max(array2)
array2_len = np.size(array2)
array2_variance = np.var(array2)

product = array1 * array2
