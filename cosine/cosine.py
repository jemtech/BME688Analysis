import conf.Config as Config
import db.DBConnection as DB
import matplotlib.pyplot as pyplot
from data.entry import Entry
from data.cluster import Cluster

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

def plotCosines():
    fig, ax = pyplot.subplots()
    for cluster in clusters:
        ax.plot(cosinesToCluster(cluster), label=cluster.name)
    legend = ax.legend(loc='best', shadow=True, fontsize='x-large')
    pyplot.ylabel('cosine to data')
    pyplot.xlabel('time')
    pyplot.show()

def cosinesToCluster(cluster: Cluster) -> list[float]:
    cosines = []
    for entry in data:
        cosines.append(cluster.cosine(entry))
    return cosines

clusters = []
def initClusters():
    clusters.append(Cluster(data[865:925] + data[311:324], "fresh air"))
    clusters.append(Cluster(data[332:860], "used air"))
    clusters.append(Cluster(data[940:947], "Isopropanol"))
    clusters.append(Cluster(data[975:992], "Butan"))
    clusters.append(Cluster(data[1006:1023], "Petrol"))

def main():
    print("Start")
    Config.configLogger()
    loadData()
    initClusters()
    plotCosines()


if __name__ == "__main__":
    main()
    
