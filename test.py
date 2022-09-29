import numpy    as np
import networkx as nx
import matplotlib.pyplot as plt 
import matplotlib.cm as cm

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





    
c = np.array([[1,1,1],[2,2,2],[3,3,3]])

print(c[:,:2])
