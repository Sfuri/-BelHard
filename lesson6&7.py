import numpy as np
import itertools
import random
import pandas as pd
import matplotlib.pyplot as plt
# a = np.random.randint(0,10,(3,3))
# b = a.transpose()
# c = np.dot(a,b)
# print (c)


# lst = ['red','green','blue','white']
# for i in itertools.permutations(lst , 3 ) :
#     print (''.join(i))


# matrix = np.random.randint(0,10, (3,3))
# print (matrix)
# matrix_T = matrix.transpose()
# print (matrix_T)
# st_d = np.std(matrix)
# print(st_d)
# determ = np.linalg.det(matrix)
# print (determ)
#
# matrix_2 = np.random.randint(0, 10, (3, 3))
# print(matrix_2)
# print (f'Сумма:', np.sum(matrix_2))
# print (f'Максимальный элемент:', np.max(matrix_2))
# print (f'Минимальный элемент:,',np.min(matrix_2))
# print (f'Кол-во элементов:',np.size(matrix_2))
# print (f'Дисперсия:' ,np.var(matrix_2))
#
# print (np.dot(matrix , matrix_2))


# df  = pd.read_csv('data - Лист1.csv')
# x = df['X']
# y = df['Y']
# plt.plot(x,y)
# plt.title('График от "data.csv"')
# plt.xlabel('Ось X')
# plt.ylabel('Ось Y')
# plt.savefig('schedule.jpeg' )
# plt.show()
# print(df.std)


# labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']
# july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
# july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]
#
# plt.plot(july16_2007,labels , label='july16_2007' )
# plt.plot(july16_2020 , labels , label='july16_2020')
# plt.legend()
# plt.show()