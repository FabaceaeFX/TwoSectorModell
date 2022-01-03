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
    
    def __init__(self):
    
        self.Parameter        = par
        self.init             = init.Initializer()
        self.calculator       = calc.RCK_Calculator()
        self.integrator       = rck.RCK_Integrator()
        self.creator          = nc.NetworkCreator()
        self.networkManager   = nh.NetworkManager()
        self.plot             = plot.HarryPlotter()
    
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
        
        self.occupNumberC        = 0
        self.occupNumberF        = 0
        self.occupNumberVectorC  = 0
        self.occupNumberVectorF  = 0
        
        self.incomes             = 0
        self.incomesMatrix       = 0
      
        self.savingsRates        = 0
        self.savingsRatesMatrix  = 0
                
        self.avgSavingsC         = 0
        self.avgSavingsF         = 0
        self.avgSavingsVectorC   = 0
        self.avgSavingsVectorF   = 0

        
        self.consumptions        = 0
        self.consumptionsMatrix  = 0
      
      
      
    
    def runModel(self):
    
        self.getNetworkGraph()
        self.initializeVariables()
        self.calculateVariables()
        self.wrightInitArrayEntries()
   
        while self.time < par.maxTime:
                
            self.pickNextUpdateTime()
            self.pickCandidateAndBestNeighbor()
            self.getResults()
            self.copySavingsRateOfBestNeighbor()
            self.copySectorOfBestNeighbor()
            self.updateSystemTime()
            self.calculateVariables()
            self.appendResultsToArrays()

             
        self.plot.plotVectors(self.capitalsCMatrix, self.capitalsFMatrix,\
                              self.totalCapitalCVector, self.totalCapitalFVector,\
                              self.rentCVector, self.rentFVector,\
                              self.wagesCVector, self.wagesFVector,\
                              self.productionCVector, self.productionFVector,\
                              self.occupNumberVectorC, self.occupNumberVectorF,\
                              self.incomesMatrix, self.savingsRatesMatrix,\
                              self.avgSavingsVectorC, self.avgSavingsVectorF,\
                              self.consumptionsMatrix)
     
     
     
     
       
 
    def getNetworkGraph(self):
    
        self.networkGraph, self.neighborhoodMatrix = self.creator.createNetwork()
                
      
    def initializeVariables(self):
    
        self.capitalsC, self.capitalsF,\
        self.laborsC, self.laborsF,\
        self.sectorIdArray, self.savingsRates      = self.init.getInitVariables()
    
        
    def calculateVariables(self):

        self.wagesC, self.wagesF,\
        self.rentC, self.rentF,\
        self.productionC, self.productionF,\
        self.incomes, self.consumptions,\
        self.totalCapitalC, self.totalCapitalF,\
        self.occupNumberC, self.occupNumberF,\
        self.avgSavingsC, self.avgSavingsF         = self.calculator.getRCKVariables\
                                                    (self.capitalsC, self.capitalsF,\
                                                     self.laborsC, self.laborsF,\
                                                     self.savingsRates, self.sectorIdArray)
          

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
            
                    
    def copySavingsRateOfBestNeighbor(self):
    
        if self.consumptions[self.bestNeighbor] > self.consumptions[self.candidate]:
    
            self.savingsRates[self.candidate]      = self.savingsRates[self.bestNeighbor] + np.random.uniform(par.startEps, par.endEps, size=1)
            
            while (self.savingsRates[self.candidate] > 1) or (self.savingsRates[self.candidate] < 0):
            
                self.savingsRates[self.candidate]  = self.savingsRates[self.bestNeighbor] + np.random.uniform(par.startEps, par.endEps, size=1)
        
        
    def copySectorOfBestNeighbor(self):
    
        self.sectorIdArray[self.candidate]         = self.sectorIdArray[self.bestNeighbor]  

                    
    def updateSystemTime(self):
   
        self.time                                  = self.updateTime
        
        
     
    def wrightInitArrayEntries(self):
    
        self.timeVector                            = self.time
        
        self.totalLaborCVector                     = self.totalLaborC
        self.totalLaborFVector                     = self.totalLaborF
        
        self.wagesCVector                          = self.wagesC
        self.wagesFVector                          = self.wagesF
        
        self.rentCVector                           = self.rentC
        self.rentFVector                           = self.rentF
        
        self.productionCVector                     = self.productionC
        self.productionFVector                     = self.productionF
        
        self.totalCapitalCVector                   = self.totalCapitalC
        self.totalCapitalFVector                   = self.totalCapitalF
        
        self.capitalsCMatrix                       = self.capitalsC
        self.capitalsFMatrix                       = self.capitalsF
        
        self.incomesMatrix                         = self.incomes
        self.savingsRatesMatrix                    = self.savingsRates
        self.consumptionsMatrix                    = self.consumptions  
        
        self.occupNumberVectorC                    = self.occupNumberC
        self.occupNumberVectorF                    = self.occupNumberF
        
        self.avgSavingsVectorC                     = self.avgSavingsC
        self.avgSavingsVectorF                     = self.avgSavingsF
    
                 
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
        
        self.avgSavingsVectorC    = np.append(self.avgSavingsVectorC, self.avgSavingsC)
        self.avgSavingsVectorF    = np.append(self.avgSavingsVectorF, self.avgSavingsF)
        
        self.occupNumberVectorC   = np.append(self.occupNumberVectorC, self.occupNumberC)
        self.occupNumberVectorF   = np.append(self.occupNumberVectorF, self.occupNumberF)
        
        self.capitalsCMatrix      = np.vstack((self.capitalsCMatrix, self.capitalsC))
        self.capitalsFMatrix      = np.vstack((self.capitalsFMatrix, self.capitalsF))
        
        self.incomesMatrix        = np.vstack((self.incomesMatrix, self.incomes))
        self.savingsRatesMatrix   = np.vstack((self.savingsRatesMatrix, self.savingsRates))
        self.consumptionsMatrix   = np.vstack((self.consumptionsMatrix, self.consumptions))   
              
         
            
    
  
        
        
if __name__ == '__main__':


    myProjectRCK       = ProjectRCK()

    
    
    myProjectRCK.runModel()


''' END '''
   
    



