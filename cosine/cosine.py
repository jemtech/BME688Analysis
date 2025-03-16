import conf.Config as Config
import db.DBConnection as DB
import matplotlib.pyplot as pyplot
from data.entry import Entry

def loadData():
    tableName = Config.getConfig()['DB']['data_table']
    query = "SELECT changeTime, ohm0, ohm1, ohm2, ohm3, ohm4, ohm5, ohm6, ohm7, ohm8, ohm9 FROM " + tableName + " order by changeTime ASC"
    print(query)
    DB.query(query, None, __handleData)

data = []
def __handleData(cursor):
    for changeTime, ohm0, ohm1, ohm2, ohm3, ohm4, ohm5, ohm6, ohm7, ohm8, ohm9 in cursor:
        entry = Entry(ohm0, ohm1, ohm2, ohm3, ohm4, ohm5, ohm6, ohm7, ohm8, ohm9)
        data.append(entry)

def plotCosinesToCenter():
    pyplot.plot(cosinesToCenter(), "r")
    pyplot.plot(cosinesToMin(), "g")
    pyplot.plot(cosinesToMax(), "b")
    pyplot.ylabel('cosine to data r = center g = min b = max')
    pyplot.xlabel('time')
    pyplot.show()

def cosinesToCenter():
    Entry.getCenter() #init center
    cosines = []
    for entry in data:
        cosines.append(entry.cosineToCenter())
    return cosines

def cosinesToMin():
    Entry.getCenter() #init center
    cosines = []
    for entry in data:
        cosines.append(entry.cosineToMin())
    return cosines

def cosinesToMax():
    Entry.getCenter() #init center
    cosines = []
    for entry in data:
        cosines.append(entry.cosineToMax())
    return cosines

def main():
    print("Start")
    Config.configLogger()
    loadData()
    plotCosinesToCenter()


if __name__ == "__main__":
    main()
    
