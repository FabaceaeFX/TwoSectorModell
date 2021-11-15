import numpy as np

import networkx      as nx
import ParametersRCK as par


class NetworkManager:

    def __init__(self):
    
        self.networkGraph          = 0
        
        self.candidate             = 0
        self.neighborsOfCandidate  = 0
        self.bestNeighbor          = 0
        self.neighborsConsumptions = 0
        
   
    def pickCandidateAndBestNeighbor(self, _networkGraph, _consumptions):
    
        self.networkGraph = _networkGraph
        
        self.pickCandidateToUpdate()
        self.loadNeighborhoodOfCandidate()
        self.getNeighborsConsumptions(_consumptions)
        self.chooseBestNeighborOfCandidate()
        
        
        return self.candidate, self.bestNeighbor
        
        
            
            
    def pickCandidateToUpdate(self):
        
        self.candidate = np.random.randint(par.numOfAgents)
 
        
    def loadNeighborhoodOfCandidate(self):
        
        self.neighborsOfCandidate = list(self.networkGraph.neighbors(self.candidate))
        
        
    def getNeighborsConsumptions(self, _consumptions):
    
        self.neighborsConsumptions = _consumptions[self.neighborsOfCandidate]

    
    def chooseBestNeighborOfCandidate(self):
   
        self.bestNeighbor = self.neighborsOfCandidate[np.argmax(self.neighborsConsumptions)]
       
  
