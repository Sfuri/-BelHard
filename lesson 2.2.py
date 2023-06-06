import sympy as sp
import random

# def solver(expression: str,variable):
#     x = sp.symbols(variable)
#     expression = sp.sympify(expression)
#
#     der = str(sp.diff(expression,x))
#     # args = der.args
#     # result = 0
#     # for element in args:
#
#     return der
# print(solver('x**3+2*x*y+3*y*z**2','z'))


a = list(random.randint(0, 90) for i in range(100))
b = tuple(random.randint(0, 90) for i in range(100))
a_average = sum(a) / len(a)
b_average = sum(b) / len(b)
round(a_average)
print(a_average)
