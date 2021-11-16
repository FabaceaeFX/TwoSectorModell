import numpy    as np
import networkx as nx

networkGraph             = nx.complete_graph(6)
candidate                = 1
neighbors                = list(networkGraph.neighbors(candidate))
consumptions             = np.array([0,0,1,0,0,0])
savingsRates             = np.array([7,8,9,10,11,12])
NeighborhoodConsumptions = consumptions[neighbors]
bestNeighbor             = neighbors[np.argmax(NeighborhoodConsumptions)]
  



print("neighborsOfCandidate", neighbors, "consumptions", NeighborhoodConsumptions, "bestNeighbor", bestNeighbor, "savingCandidate", savingsRates[candidate], "savingBestNeigh", savingsRates[bestNeighbor] )
