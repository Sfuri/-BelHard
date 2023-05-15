import time
from abc import ABC , abstractmethod
# def decorator(func):
#     def wrapper(*args):
#         start_time = time()
#         result = func(*args)
#         end_time = time() - start_time
#         print (end_time)
#
# @decorator
# def timer (sec):
#     time.sleep(sec)
#     return
# timer()

class Transport :
    @abstractmethod
    engine: str
    model:str
    mileage:int
    color:str
    year:int
    maxV:int
    def __init__(self,engine,model,mileage,color,year,maxV):
        self.engine = engine
        self.model = model
        self.mileage = mileage
        self.color = color
        self.year =year
        self.maxV =maxV
    def start(self):
        print('start')
    def stop(self):
        print('stop')


class AirTransport(Transport):
    space: int
    maxH: int
    chassis: int
    wings: int
    def __init__(self,engine,model,mileage,color,year,maxV,space,maxH,chassis,wings):
        super().__init__(engine,model,mileage,color,year,maxV)
        self.space = space
        self.maxH = maxH
        self.chassis = chassis
        self.wings = wings
    def fly :
        print('"Engine sound"')
class GroundTransport(Transport):
    def __init__(self, engine, model, mileage, color, year, maxV):
        super().__init__(engine, model, mileage, color, year, maxV)
        self.Taxi = False
    def Taxi(self):
        self.Taxi = True

class WaterTransport(Transport):
    def __init__(self, engine, model, mileage, color, year, maxV):



