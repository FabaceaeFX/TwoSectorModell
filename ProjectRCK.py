from scipy.integrate import odeint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import RCK_Integrator   as rck
import RCK_Calculator   as calc
import networkx         as nx
import NetworkCreator   as nc
import NetworkManager   as nh
import ResultsCollector as res
import ParametersRCK    as par



class ProjectRCK:
    
    def __init__(self, _Parameter, _RCKCalculator, _RCKIntegrator, _ResultsCollector, _NetworkCreator, _NetworkManager):
    
        self.calculator          = _RCKCalculator
        self.integrator          = _RCKIntegrator
        self.collector           = _ResultsCollector
        self.creator             = _NetworkCreator
        self.networkManager      = _NetworkManager
    
        self.networkGraph        = 0
        self.neighborhoodMatrix  = None
        
        self.time                = 0
        self.timesteps           = 0
        self.updateTime          = 0
        
        self.candidate           = 0
        self.neighbors           = None
        self.bestNeighbor        = 0
        
        self.production          = None
        self.wages               = None
        self.rent                = None
        
        self.capitals            = par.initCapitals
        self.savingsRates        = par.initSavingsRates
        self.incomes             = par.initIncomes
        self.consumptions        = par.initConsumptions
        self.totalCapital        = 0
       
        self.newCapitals         = None
        self.newTotalLabor       = None
        
        self.timeVector          = None
        self.totalLaborVector    = None
        self.wagesVector         = None
        self.rentVector          = None
        self.productionVector    = None
        self.capitalsMatrix      = None
        self.incomesMatrix       = None
        self.savingsRatesMatrix  = None
        self.consumptionsMatrix  = None
      
    
    def runModel(self):
    
        self.getNetworkGraph()
   
        while self.time < par.maxTime:
            
             self.getVariables()
            # print("wages",self.wages, "rent", self.rent, "incomes", self.incomes, "prod", self.production, "consumptions", self.consumptions)
             self.pickCandidateAndBestNeighbor()
            # print("Candidate", self.candidate, "bestNeighbor", self.bestNeighbor)
             self.getResults()
            # print("NewCapitals", self.newCapitals)
             self.updateFunctionState()
             self.appendResultsToArrays
             
       
        print(self.consumptionsMatrix)
       
 
    def getNetworkGraph(self):
    
        self.networkGraph, self.neighborhoodMatrix = self.creator.createNetwork()
                
        
    def getVariables(self):
    
        self.totalCapital = sum(self.capitals)
        
        self.wages, self.rent, self.incomes, self.production, self.consumptions = \
                self.calculator.getRCKVariables(self.capitals, self.savingsRates, self.totalCapital)
          

    def pickCandidateAndBestNeighbor(self):
        
        self.pickNextUpdateTime()
        self.candidate, self.bestNeighbor = self.networkManager.pickCandidateAndBestNeighbor \
                                              (self.networkGraph, self.consumptions)
                
                
    def pickNextUpdateTime(self):
    
        self.updateTime = self.time + np.random.exponential(scale=par.tau/par.numOfAgents)  
         
    
    def getResults(self):
          
        self.newCapitals, self.newTotalLabor = self.integrator.returnModelSolutions \
                    (self.capitals, self.savingsRates, self.incomes, self.time, self.updateTime)
                    
     
    def updateFunctionState(self):
                             
        self.updateCapitals()
        self.updateTotalLabor()
        self.updateSavingsRates()
        self.updateSystemTime()
        
        
    def updateCapitals(self):
    
        self.capitals = self.newCapitals
        
        
    def updateTotalLabor(self):
    
        self.totalLabor = self.newTotalLabor
        
           
    def updateSavingsRates(self):
    
        if self.consumptions[self.bestNeighbor] > self.consumptions[self.candidate]:
                  
            self.copySavingsRateOfBestNeighor()
            
                    
    def copySavingsRateOfBestNeighor(self):
    
        self.savingsRates[self.candidate] = self.savingsRates[self.bestNeighbor]    
                                       
                    
    def updateSystemTime(self):
   
        self.time = self.updateTime
            
              
    def appendResultsToArrays(self):          
              
        self.timeVector          = np.append(self.timeVector, self.time)
        self.totalLaborVector    = np.append(self.totalLaborVector, self.totalLabor)
        self.wagesVector         = np.append(self.wagesVector, self.wages)
        self.rentVector          = np.append(self.rentVector, self.rent)
        self.productionVector    = np.append(self.productionVector, self.production)
        self.capitalsMatrix      = np.vstack((self.capitalsMatrix, self.capitals))
        self.incomesMatrix       = np.vstack((self.incomesMatrix, self.incomes))
        self.savingsRatesMatrix  = np.vstack((self.savingsMatrix, self.savings))
        self.consumptionsMatrix  = np.vstack((self.consumptionsMatrix, self.consumptions))   
              
            
    
  
        
        
if __name__ == '__main__':


    myParameter        = par
    myRCKCalculator    = calc.RCK_Calculator()
    myRCKIntegrator    = rck.RCK_Integrator()
    myResultsCollector = res.ResultsCollector()
    myNetworkCreator   = nc.NetworkCreator()
    myNetworkManager   = nh.NetworkManager()
    myProjectRCK       = ProjectRCK(myParameter, myRCKCalculator, myRCKIntegrator, myResultsCollector, myNetworkCreator, myNetworkManager)

    
    
    myProjectRCK.runModel()


''' END '''
   
    



