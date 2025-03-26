import sys
import math
from typing import List

class Entry(object):
    min:List[float] = [sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max]
    max:List[float] = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    center:List[float] = None
    centerSqSumm:float = 0.0
    maxSqSumm:float = 0.0
    minSqSumm:float = 0.0
    
    def __init__(self, ohm0:float, ohm1:float, ohm2:float, ohm3:float, ohm4:float, ohm5:float, ohm6:float, ohm7:float, ohm8:float, ohm9:float):
        self.data:List[float] = []
        self.data.append(ohm0)
        self.data.append(ohm1)
        self.data.append(ohm2)
        self.data.append(ohm3)
        self.data.append(ohm4)
        self.data.append(ohm5)
        self.data.append(ohm6)
        self.data.append(ohm7)
        self.data.append(ohm8)
        self.data.append(ohm9)
        self.dimension: int = len(self.data)
        self.__minMax()
        self.cosineToCenterTemp:float = None
        self.sqSumMem:float = None

    def __minMax(self):
        for idx, ohm in enumerate(self.data):
            if ohm < Entry.min[idx]:
                Entry.min[idx] = ohm
            if ohm > Entry.max[idx]:
                Entry.max[idx] = ohm

    def sqSum(self) -> float:
        if self.sqSumMem is None:
            self.sqSumMem = 0.0
            for i in range(self.dimension):
                x:float = self.data[i]
                self.sqSumMem += x*x
        return self.sqSumMem

    def cosineToCenter(self) -> float:
        if self.cosineToCenterTemp is None:
            # init center if not done
            Entry.getCenter()
            sumxy = 0.0
            for i in range(self.dimension):
                sumxy += self.data[i]*Entry.center[i]
            self.cosineToCenterTemp = sumxy/math.sqrt(self.sqSum()*Entry.centerSqSumm)
        return self.cosineToCenterTemp

    def cosineToMin(self) -> float:
        sumxy = 0.0
        for i in range(self.dimension):
            sumxy += self.data[i]*Entry.min[i]
        return sumxy/math.sqrt(self.sqSum()*Entry.minSqSumm)

    def cosineToMax(self) -> float:
        sumxy = 0.0
        for i in range(self.dimension):
            sumxy += self.data[i]*Entry.max[i]
        return sumxy/math.sqrt(self.sqSum()*Entry.maxSqSumm)
    
    @staticmethod
    def getCenter() -> List[float]:
        if Entry.center is None:
            Entry.center = []
            Entry.centerSqSumm = 0.0
            for i in range(10):
                center = ((Entry.max[i] - Entry.min[i]) / 2) + Entry.min[i]
                Entry.center.append(center)
                Entry.centerSqSumm += center * center
                Entry.minSqSumm += Entry.min[i] * Entry.min[i]
                Entry.maxSqSumm += Entry.max[i] * Entry.max[i]
        return Entry.center
