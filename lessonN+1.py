from sqlalchemy.orm import DeclarativeBase


# class car:
#     color:str
#     type:str
#     year:int
#     def __init__(self,color,type,year):
#         self.color = color
#         self._type = type
#         self.__year = year
#     def eng_start(self):
#         print ('Engine is on')
#     def eng_stop(self):
#         print ('Engine is off')
#     def set_color(self,newV):
#         self.color = newV
#     def set_type(self,newV):
#         self._type = newV
#     @property
#     def year(self):
#         return self.__year
#
#     @year.setter
#     def set_year(self,newV):
#         self.__year = newV


# class Math:
#     a:int
#     b:int
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def multiply(self):
#         print(self.a * self.b)
#
#     def div(self):
#         try:
#             print(self.a / self.b)
#         except ZeroDivisionError:
#             b=0

class Base(DeclarativeBase):
    pass


class person(Base):
    name = str
    sex = str
    age = int
    position = str
    status = str
