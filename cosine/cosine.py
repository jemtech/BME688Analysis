import conf.Config as Config
import db.DBConnection as DB
import matplotlib.pyplot as pyplot
from data.entry import Entry
from data.cluster import Cluster
import json

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
    trainingData = json.loads(Config.getConfig()['Cluster']['training_data'])
    for clusterConfig in trainingData:
        clusterData = []
        for dataIndex in clusterConfig['index']:
            clusterData += data[dataIndex['start']:dataIndex['end']]
        clusters.append(Cluster(clusterData, clusterConfig['name']))

def main():
    print("Start")
    Config.configLogger()
    loadData()
    initClusters()
    plotCosines()


if __name__ == "__main__":
    main()
    
