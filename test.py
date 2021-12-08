import numpy    as np
import networkx as nx

networkGraph             = nx.complete_graph(6)
candidate                 = 1
neighbors                 = list(networkGraph.neighbors(candidate))
consumptions              = np.array([0,0,1,0,0,0])
savingsRates              = np.array([7,8,9,10,11,12])
capitalsC                 = np.array([1,0,5,1,1,0])
capitalsF                 = np.array([0,1,0,0,0,1])


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

wagesC=1
wagesF=1

rentC=1
rentF=1

incomes = wagesC * laborsC + wagesF * laborsF + rentC * capitalsC + rentF * capitalsF 



print(incomes)
