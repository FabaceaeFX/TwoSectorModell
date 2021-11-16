from scipy.integrate import odeint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import Initializer      as init
import RCK_Integrator   as rck
import RCK_Calculator   as calc
import networkx         as nx
import NetworkCreator   as nc
import NetworkManager   as nh
import HarryPlotter     as plot
import ParametersRCK    as par



class ProjectRCK:
    
    def __init__(self, _Parameter, _Initializer, _RCKCalculator, _RCKIntegrator, \
                                       _NetworkCreator, _NetworkManager, _Plotter):
    
        self.init                = _Initializer
        self.calculator          = _RCKCalculator
        self.integrator          = _RCKIntegrator
        self.creator             = _NetworkCreator
        self.networkManager      = _NetworkManager
        self.plot                = _Plotter
    
        self.networkGraph        = 0
        self.neighborhoodMatrix  = 0
        
        self.time                = 0
        self.timesteps           = 0
        self.updateTime          = 0
        
        self.candidate           = 0
        self.neighbors           = 0
        self.bestNeighbor        = 0
        
        self.production          = 0
        self.wages               = 0
        self.rent                = 0
        
        self.capitals            = 0
        self.savingsRates        = 0
        self.incomes             = 0
        self.consumptions        = 0
        self.totalCapital        = 0
        self.totalLabor          = 0
       
        self.newCapitals         = 0
        self.newTotalLabor       = 0
        
        self.timeVector          = 0
        self.totalCapitalVector  = 0
        self.totalLaborVector    = 0
        self.wagesVector         = 0
        self.rentVector          = 0
        self.productionVector    = 0
        
        self.capitalsMatrix      = 0
        self.incomesMatrix       = 0
        self.savingsRatesMatrix  = 0
        self.consumptionsMatrix  = 0
      
    
    def runModel(self):
    
        self.getNetworkGraph()
        self.initializeVariables()
        self.getVariables()
        self.wrightInitArrayEntries()
   
        while self.time < par.maxTime:
            
             self.getVariables()
             self.pickNextUpdateTime()
             self.pickCandidateAndBestNeighbor()
             self.getResults()
             self.updateFunctionState()
             self.appendResultsToArrays()
             
        self.plot.plotVector(self.savingsRatesMatrix)
        self.plot.plotVector(self.capitalsMatrix)
     
       
 
    def getNetworkGraph(self):
    
        self.networkGraph, self.neighborhoodMatrix = self.creator.createNetwork()
                
      
    def initializeVariables(self):
    
        self.capitals, self.savingsRates, \
        self.incomes, self.consumptions, \
        self.totalCapital, self.totalLabor         = self.init.getInitVariables()
    
        
    def getVariables(self):
    
        self.totalCapital = sum(self.capitals)     
        self.wages, self.rent, self.incomes,\
        self.production, self.consumptions = self.calculator.getRCKVariables(self.capitals,\
                                                       self.savingsRates, self.totalCapital)
          

    def pickCandidateAndBestNeighbor(self):
        
        self.candidate, self.bestNeighbor = self.networkManager.pickCandidateAndBestNeighbor \
                                              (self.networkGraph, self.consumptions)
                
                
    def pickNextUpdateTime(self):
    
        self.updateTime = self.time + np.random.exponential(scale=par.tau/par.numOfAgents)  
         
    
    def getResults(self):
          
        self.newCapitals, self.newTotalLabor = self.integrator.returnModelSolutions \
                                               (self.capitals, self.savingsRates, \
                                                self.incomes, self.time, self.updateTime)
                    
     
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
        print(self.time)
            
     
    def wrightInitArrayEntries(self):
    
        self.timeVector          = self.time
        self.totalLaborVector    = self.totalLabor
        self.wagesVector         = self.wages
        self.rentVector          = self.rent
        self.productionVector    = self.production
        self.totalCapitalVector  = self.totalCapital
        self.capitalsMatrix      = self.capitals
        self.incomesMatrix       = self.incomes
        self.savingsRatesMatrix  = self.savingsRates
        self.consumptionsMatrix  = self.consumptions  
    
                 
    def appendResultsToArrays(self):          
              
        self.timeVector          = np.append(self.timeVector, self.time)
        self.totalLaborVector    = np.append(self.totalLaborVector, self.totalLabor)
        self.wagesVector         = np.append(self.wagesVector, self.wages)
        self.rentVector          = np.append(self.rentVector, self.rent)
        self.productionVector    = np.append(self.productionVector, self.production)
        self.totalCapitalVector  = np.append(self.totalCapitalVector, self.totalCapital)
        self.capitalsMatrix      = np.vstack((self.capitalsMatrix, self.capitals))
        self.incomesMatrix       = np.vstack((self.incomesMatrix, self.incomes))
        self.savingsRatesMatrix  = np.vstack((self.savingsRatesMatrix, self.savingsRates))
        self.consumptionsMatrix  = np.vstack((self.consumptionsMatrix, self.consumptions))   
              
            
    
  
        
        
if __name__ == '__main__':


    myParameter        = par
    myInitializer      = init.Initializer()
    myRCKCalculator    = calc.RCK_Calculator()
    myRCKIntegrator    = rck.RCK_Integrator()
    myNetworkCreator   = nc.NetworkCreator()
    myNetworkManager   = nh.NetworkManager()
    myHarryPlotter     = plot.HarryPlotter()
    myProjectRCK       = ProjectRCK(myParameter, myInitializer, myRCKCalculator, \
                         myRCKIntegrator, myNetworkCreator, myNetworkManager, \
                         myHarryPlotter)

    
    
    myProjectRCK.runModel()


''' END '''
   
    



