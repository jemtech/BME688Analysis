from data.entry import Entry
import math

class Cluster(object):
    entries = None
    centroid = None
    centroidSqSumm = None
    name = None

    def __init__(self, entries: list[Entry], name: str):
        self.entries = entries
        self.name = name
        self.__calculateCentroid()

    def __calculateCentroid(self):
        self.centroid = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        for entry in self.entries:
            for idx, coordinate in enumerate(entry.data):
                self.centroid[idx] += coordinate
        size = len(self.entries)
        for idx, coordinate in enumerate(self.centroid):
            self.centroid[idx] = coordinate / size
        self.__calculateCentroidSqSumm()
    
    def __calculateCentroidSqSumm(self):
        self.centroidSqSumm = 0.0
        for coordinate in self.centroid:
            self.centroidSqSumm += coordinate * coordinate

    def cosine(self, entry: Entry) -> float:
        sumxx, sumxy = 0.0, 0.0
        for i in range(10):
            x = entry.data[i]
            sumxx += x*x
            sumxy += x*self.centroid[i]
        return sumxy/math.sqrt(sumxx*self.centroidSqSumm)