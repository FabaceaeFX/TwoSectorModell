import numpy    as np
import networkx as nx
import pickle   as pickle
import pandas as pd
import matplotlib.pyplot as plt 
from numba import njit

networkGraph             = nx.complete_graph(6)
candidate                 = 1
neighbors                 = list(networkGraph.neighbors(candidate))
consumptions              = np.array([0,0,1,0,0,0])
savingsRates              = np.array([7,8,9,10,11,12])
capitalsC                 = np.array([1,0,5,1,1,0])
capitalsF                 = np.array([0,1,0,0,0,1])
incomes                   = np.array([0,1,0,0,0,1])
ones                      = np.ones(len(savingsRates))

cleanIndex                = np.where(capitalsC  != 0)
fossilIndex               = np.where(capitalsF != 0)

sectorIdArray             = np.empty(6, np.unicode_)
sectorIdArray[cleanIndex] = ('c'+str(cleanIndex))
sectorIdArray[fossilIndex] = ('f'+str(fossilIndex))




indexC                    = np.where(sectorIdArray =='c')
indexF                    = np.where(sectorIdArray=='f')

NumberInSectorF           = sum(sectorIdArray=='c')
NumberInSectorC           = sum(sectorIdArray=='f')

capitalDotsC              = np.zeros(6)
capitalDotsC[indexC]      = savingsRates[indexC] - capitalsC[indexC]



capitalsC                 = np.array([1,0,1,1,1,0])
capitalsF                 = np.array([0,1,1,0,0,1])
laborsC                   = np.array([1,0,0,1,1,0])
laborsF                   = np.array([0,1,1,0,0,1])
initLaborsC              = np.random.uniform(1/5, 0.01, size=5)
wagesC=3
wagesF=1

rentC=1
rentF=3

t=np.array([1])

incomes = wagesC * laborsC + wagesF * laborsF + rentC * capitalsC + rentF * capitalsF 


microDataFrame = pd.DataFrame({"capitalsC": [capitalsC], "capitalsF": [capitalsF], "laborC": [laborsC]}, index = t)

t=np.array([2]) 


microDataFrame3 = pd.DataFrame({"capitalsC": [capitalsC], "capitalsF": [capitalsF], "laborC": [laborsC]}, index = t)



microDataFrame = microDataFrame.append(microDataFrame3)

mc = list(microDataFrame["capitalsC"])

#plt.plot( mc, microDataFrame.index)
#plt.show()


@njit      
def calculateConsumptions(savingsRates, incomes, ones):
    
    consumptions = incomes + ones - savingsRates
        
    return consumptions









