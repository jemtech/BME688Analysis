from data.entry import Entry
import math
from typing import List

class Cluster(object):
    entries:List[Entry] = None
    centroid:List[float] = None
    centroidSqSumm:float = None
    name:str = None
    clusterDimesion:int = None

    def __init__(self, entries: List[Entry], name: str):
        self.entries = entries
        self.name = name
        self.__calculateCentroid()

    def __calculateCentroid(self):
        size:int = len(self.entries)
        if size == 0:
            self.centroid = None
            return
        self.centroid = []
        # init zero with dimension of first entry
        self.clusterDimesion = len(self.entries[0].data)
        for i in range(self.clusterDimesion):
            self.centroid.append(0.0)
        # summ data in each dimension
        for entry in self.entries:
            for idx, coordinate in enumerate(entry.data):
                self.centroid[idx] += coordinate
        # divide by entry count
        for idx, coordinate in enumerate(self.centroid):
            self.centroid[idx] = coordinate / size
        self.__calculateCentroidSqSumm()
    
    def __calculateCentroidSqSumm(self):
        self.centroidSqSumm = 0.0
        for coordinate in self.centroid:
            self.centroidSqSumm += coordinate * coordinate

    def cosine(self, entry: Entry) -> float:
        sumxy:float = 0.0
        for i in range(self.clusterDimesion):
            x:float = entry.data[i]
            sumxy += x*self.centroid[i]
        return sumxy/math.sqrt(entry.sqSum()*self.centroidSqSumm)