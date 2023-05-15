import math


# def is_cat_here(*args):
#     for elem in args:
#         if isinstance(elem,str):
#             if 'cat' in elem.lower():
#                 return (True)
#     return (False)
# print(is_cat_here('c','CaT'))


# def is_item_here(item,*args)
#     return item in args


# def your_favourite_color(my_color, **kwargs):
#     color = kwargs.get('color')
#     if  color is None:
#         print (f"My favourite color is {my_color}, what is your favourite color ?")
#     else : print (f'My fovourite color is {my_color} but {color} is also pretty good')
# your_favourite_color('blue' , **{'color':'white'})


def equation (a,b,c):
    Dis = (b**2 - 4*a*c)
    if Dis < 0:
        return ('Нет корней')
    if Dis > 0:
        x1 = (-b + Dis**0.5) / 2*a
        x2 = (-b + Dis ** 0.5) / 2*a
        return (x1,x2)
    if Dis == 0:
        return -b/2*a
print (equation(1,2,1))