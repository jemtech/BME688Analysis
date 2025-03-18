import sys
import math

class Entry(object):
    min = [sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max,
           sys.float_info.max]
    max = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    center = None
    centerSqSumm = 0.0
    maxSqSumm = 0.0
    minSqSumm = 0.0
    
    def __init__(self, ohm0, ohm1, ohm2, ohm3, ohm4, ohm5, ohm6, ohm7, ohm8, ohm9):
        self.data = []
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
        self.__minMax()
        self.cosineToCenterTemp = None

    def __minMax(self):
        for idx, ohm in enumerate(self.data):
            if ohm < Entry.min[idx]:
                Entry.min[idx] = ohm
            if ohm > Entry.max[idx]:
                Entry.max[idx] = ohm

    def cosineToCenter(self):
        if self.cosineToCenterTemp is None:
            # init center if not done
            Entry.getCenter()
            sumxx, sumxy = 0.0, 0.0
            for i in range(10):
                x = self.data[i]
                sumxx += x*x
                sumxy += x*Entry.center[i]
            self.cosineToCenterTemp = sumxy/math.sqrt(sumxx*Entry.centerSqSumm)
        return self.cosineToCenterTemp

    def cosineToMin(self):
        sumxx, sumxy = 0.0, 0.0
        for i in range(10):
            x = self.data[i]
            sumxx += x*x
            sumxy += x*Entry.min[i]
        return sumxy/math.sqrt(sumxx*Entry.minSqSumm)

    def cosineToMax(self):
        sumxx, sumxy = 0.0, 0.0
        for i in range(10):
            x = self.data[i]
            sumxx += x*x
            sumxy += x*Entry.max[i]
        return sumxy/math.sqrt(sumxx*Entry.maxSqSumm)
    
    @staticmethod
    def getCenter():
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
