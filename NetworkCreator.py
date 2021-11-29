import numpy as np

import networkx      as nx
import ParametersRCK as par

class NetworkCreator:

    def __init__(self):
        
        pass
        
    def createNetwork(self):
    
        networkGraph           = self.chooseNetworkGraph()
        neighborhoodMatrix     = self.getNeighborhoodMatrix(networkGraph)
            
        return networkGraph, neighborhoodMatrix
        
        
        
        
    def chooseNetworkGraph(self):
    
        if par.networkTopology == "AllToAll":
           
            networkGraph       = nx.complete_graph(par.numOfAgents)
            
        return networkGraph
            
            
    def getNeighborhoodMatrix(self, _networkGraph):
    
        neighborhoodMatrix     = nx.adj_matrix(_networkGraph).toarray()
        
        return neighborhoodMatrix
        
        
        

