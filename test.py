import numpy    as np
import networkx as nx

networkGraph             = nx.complete_graph(6)
candidate                = 1
neighbors                = list(networkGraph.neighbors(candidate))
consumptions             = np.array([0,0,1,0,0,0])
savingsRates             = np.array([7,8,9,10,11,12])
capitalsC                = np.array([1,0,1,1,1,0])
capitalsF                = np.array([0,1,0,0,0,1])


cleanInvestorIndex       = np.where(capitalsC == 1)
fossilInvestorIndex      = np.where(capitalsF == 1)

sectorIdentityArray      = np.empty(6, np.unicode_)
sectorIdentityArray[cleanInvestorIndex]=('c'+str(cleanInvestorIndex))
sectorIdentityArray[fossilInvestorIndex]=('f'+str(fossilInvestorIndex))




indexC = np.where(sectorIdentityArray=='c')
indexF = np.where(sectorIdentityArray=='f')

capitalDotsC         = np.zeros(6)
capitalDotsC[indexC] = savingsRates[indexC] - capitalsC[indexC]



capitalsC                = np.array([1,0,1,1,1,0])
capitalsF                = np.array([0,1,0,0,0,1])

capitals = capitalsC + capitalsF



print(capitals)
