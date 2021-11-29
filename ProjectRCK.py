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
        self.updateTime          = 0
        self.timeVector          = 0
        
        self.candidate           = 0
        self.neighbors           = 0
        self.bestNeighbor        = 0
        
        self.sectorIdArray       = 0
        
        self.capitalsC           = 0
        self.capitalsF           = 0
        self.capitalsCMatrix     = 0
        self.capitalsFMatrix     = 0
        
        self.laborsC             = 0
        self.laborsF             = 0
        self.laborsCMatrix       = 0
        self.laborsFMatrix       = 0
        
        self.totalCapitalC       = 0
        self.totalCapitalF       = 0
        self.totalCapitalCVector = 0
        self.totalCapitalFVector = 0
        
        self.totalLaborC         = 0
        self.totalLaborF         = 0
        self.totalLaborCVector   = 0
        self.totalLaborFVector   = 0
        
        self.wagesC              = 0
        self.wagesF              = 0
        self.wagesCVector        = 0
        self.wagesFVector        = 0
        
        self.rentC               = 0
        self.rentF               = 0
        self.rentCVector         = 0
        self.rentFVector         = 0
        
        self.productionC         = 0
        self.productionF         = 0
        self.productionCVector   = 0
        self.productionFVector   = 0
        
        self.incomes             = 0
        self.incomesMatrix       = 0
      
        self.savingsRates        = 0
        self.savingsRatesMatrix  = 0
        
        self.consumptions        = 0
        self.consumptionsMatrix  = 0
      
    
    def runModel(self):
    
        self.getNetworkGraph()
        self.initialize()
        self.getVariables()
        self.wrightInitArrayEntries()
   
        while self.time < par.maxTime:
                
            self.pickNextUpdateTime()
            self.pickCandidateAndBestNeighbor()
            self.getResults()
            self.updateFunctionState()
            self.getVariables()
            self.appendResultsToArrays()
             
        self.plot.plotVectors(self.capitalsCMatrix, self.capitalsFMatrix,\
                              self.totalCapitalCVector, self.totalCapitalFVector)
     
       
 
    def getNetworkGraph(self):
    
        self.networkGraph, self.neighborhoodMatrix = self.creator.createNetwork()
                
      
    def initialize(self):
    
        self.capitalsC, self.capitalsF,\
        self.laborsC, self.laborsF,\
        self.sectorIdArray, self.savingsRates      = self.init.getInitVariables()
    
        
    def getVariables(self):
    
        self.totalCapitalC                         = sum(self.capitalsC)   
        self.totalCapitalF                         = sum(self.capitalsF)
        
        self.totalLaborC                           = sum(self.laborsC)  
        self.totalLaborF                           = sum(self.laborsF)
        

        self.wagesC, self.wagesF,\
        self.rentC, self.rentF,\
        self.productionC, self.productionF,\
        self.incomes, self.consumptions            = self.calculator.getRCKVariables\
                                                    (self.capitalsC, self.capitalsF,\
                                                     self.laborsC, self.laborsF,\
                                                     self.totalCapitalC,self.totalCapitalF,\
                                                     self.totalLaborC, self.totalLaborF,\
                                                     self.savingsRates)
          

    def pickCandidateAndBestNeighbor(self):
        
        self.candidate, self.bestNeighbor          = self.networkManager.pickCandidateAndBestNeighbor\
                                                    (self.networkGraph, self.consumptions)
                
                
    def pickNextUpdateTime(self):
    
        self.updateTime                            = self.time +\
                                                     np.random.exponential(scale=par.tau/par.numOfAgents)  
         
    
    def getResults(self):
          
        self.capitalsC, self.capitalsF,\
        self.totalLaborC, self.totalLaborF         = self.integrator.returnModelSolutions\
                                                     (self.capitalsC, self.capitalsF,\
                                                      self.totalLaborC, self.totalLaborF,\
                                                      self.sectorIdArray, self.incomes, self.savingsRates,\
                                                      self.time, self.updateTime)
                    
     
    def updateFunctionState(self):
                             
        self.updateSavingsRates()
        self.updateSystemTime()
        
           
    def updateSavingsRates(self):
    
        if self.consumptions[self.bestNeighbor] > self.consumptions[self.candidate]:
                  
            self.copySavingsRateOfBestNeighbor()
            self.copySectorOfBestNeighbor()
            
                    
    def copySavingsRateOfBestNeighbor(self):
    
        self.savingsRates[self.candidate]         = self.savingsRates[self.bestNeighbor]
        
        
    def copySectorOfBestNeighbor(self):
    
        self.sectorIdArray[self.candidate]        = self.sectorIdArray[self.bestNeighbor]  
        print(self.sectorIdArray)  
                                       
                    
    def updateSystemTime(self):
   
        self.time                                 = self.updateTime
            
     
    def wrightInitArrayEntries(self):
    
        self.timeVector                           = self.time
        
        self.totalLaborCVector                    = self.totalLaborC
        self.totalLaborFVector                    = self.totalLaborF
        
        self.wagesCVector                         = self.wagesC
        self.wagesFVector                         = self.wagesF
        
        self.rentCVector                          = self.rentC
        self.rentFVector                          = self.rentF
        
        self.productionCVector                    = self.productionC
        self.productionFVector                    = self.productionF
        
        self.totalCapitalCVector                  = self.totalCapitalC
        self.totalCapitalFVector                  = self.totalCapitalF
        
        self.capitalsCMatrix                      = self.capitalsC
        self.capitalsFMatrix                      = self.capitalsF
        
        self.incomesMatrix                        = self.incomes
        self.savingsRatesMatrix                   = self.savingsRates
        self.consumptionsMatrix                   = self.consumptions  
    
                 
    def appendResultsToArrays(self):          
              
        self.timeVector           = np.append(self.timeVector, self.time)
        
        self.totalLaborCVector    = np.append(self.totalLaborCVector, self.totalLaborC)
        self.totalLaborFVector    = np.append(self.totalLaborFVector, self.totalLaborF)
        
        self.wagesCVector         = np.append(self.wagesCVector, self.wagesC)
        self.wagesFVector         = np.append(self.wagesFVector, self.wagesF)
        
        self.rentCVector          = np.append(self.rentCVector, self.rentC)
        self.rentFVector          = np.append(self.rentFVector, self.rentF)
        
        self.productionCVector    = np.append(self.productionCVector, self.productionC)
        self.productionFVector    = np.append(self.productionFVector, self.productionF)
        
        self.totalCapitalCVector  = np.append(self.totalCapitalCVector, self.totalCapitalC)
        self.totalCapitalFVector  = np.append(self.totalCapitalFVector, self.totalCapitalF)
        
        self.capitalsCMatrix      = np.vstack((self.capitalsCMatrix, self.capitalsC))
        self.capitalsFMatrix      = np.vstack((self.capitalsFMatrix, self.capitalsF))
        
        self.incomesMatrix        = np.vstack((self.incomesMatrix, self.incomes))
        self.savingsRatesMatrix   = np.vstack((self.savingsRatesMatrix, self.savingsRates))
        self.consumptionsMatrix   = np.vstack((self.consumptionsMatrix, self.consumptions))   
              
            
    
  
        
        
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
   
    



