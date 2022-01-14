from scipy.integrate import odeint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import NumbaCalculator  as num
import Initializer      as init
import RCK_Integrator   as rck
import RCK_IntegratorTest as test
import RCK_Calculator   as calc
import networkx         as nx
import NetworkCreator   as nc
import NetworkManager   as nh
import HarryPlotter     as plot
import ParametersRCK    as par



class ProjectRCK:
    
    def __init__(self):
    
        self.Parameter           = par
    
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
        self.savingsRatesC       = 0       
        self.savingsRatesF       = 0
        self.savingsRatesMatrixC = 0
        self.savingsRatesMatrixF = 0
                
        self.avgSavingsC         = 0
        self.avgSavingsF         = 0
        self.avgSavingsVectorC   = 0
        self.avgSavingsVectorF   = 0

        
        self.consumptions        = 0
        self.consumptionsMatrix  = 0
        
        self.microDataFrame      = 0
        self.macroDataFrame      = 0
      
      
      
    
    def runModel(self, _tau):
    
        self.getNetworkGraph()
        self.initializeVariables()
        self.calculateVariables()
        self.wrightInitArrayEntries()
        self.initializeMicroDataFrame()
        self.initializeMacroDataFrame()
      
        while self.time < par.maxTime:
                
            self.pickNextUpdateTime(_tau)
            self.pickCandidateAndBestNeighbor()
            self.getResults()
            self.copySavingsRateOfBestNeighbor()
            self.copySectorOfBestNeighbor()
            self.updateSavingsSector()
            self.updateSystemTime()
            self.calculateVariables()
            self.appendResultsToArrays()

         
       # return self.savingsRatesC, self.savingsRatesF
        
            
        plot.HarryPlotter().plotVectors(self.capitalsCMatrix, self.capitalsFMatrix,\
                              self.totalCapitalCVector, self.totalCapitalFVector,\
                              self.rentCVector, self.rentFVector,\
                              self.wagesCVector, self.wagesFVector,\
                              self.productionCVector, self.productionFVector,\
                              self.occupNumberVectorC, self.occupNumberVectorF,\
                              self.savingsRatesMatrixC, self.savingsRatesMatrixF,\
                              self.avgSavingsVectorC, self.avgSavingsVectorF,\
                              self.incomesMatrix, self.consumptionsMatrix)
     
        
     
     
       
 
    def getNetworkGraph(self):
    
        self.networkGraph, self.neighborhoodMatrix = nc.NetworkCreator().createNetwork()
        print(self.networkGraph, self.neighborhoodMatrix)
      
    def initializeVariables(self):
    
        self.capitalsC, self.capitalsF,\
        self.laborsC, self.laborsF,\
        self.sectorIdArray, self.savingsRates      = init.Initializer().getInitVariables()
        print( "capitalsC", self.capitalsC, "capitalsF",  self.capitalsF, "laborsC", self.laborsC, "laborsF", self.laborsF, "sectorIdArray", self.sectorIdArray, "savingsRates", self.savingsRates)
    
        
    def calculateVariables(self):

        self.totalCapitalC       = sum(self.capitalsC)
        self.totalCapitalF       = sum(self.capitalsF)
        self.totalLaborC         = sum(self.laborsC)
        self.totalLaborF         = sum(self.laborsF)
        self.occupNumberC        = sum(self.sectorIdArray=='c')
        self.occupNumberF        = sum(self.sectorIdArray=='f')
        savingsSumC              = sum(self.savingsRates[self.sectorIdArray=='c'])
        savingsSumF              = sum(self.savingsRates[self.sectorIdArray=='c'])
        
        self.wagesC       = num.calculateWages(self.totalCapitalC, self.totalLaborC)
        self.wagesF       = num.calculateWages(self.totalCapitalF, self.totalLaborF)
        self.rentC        = num.calculateRents(self.totalCapitalC, self.totalLaborC)
        self.rentF        = num.calculateRents(self.totalCapitalF, self.totalLaborF)
        self.productionC  = num.calculateProduction(self.totalCapitalC, self.totalLaborC)
        self.productionF  = num.calculateProduction(self.totalCapitalF, self.totalLaborF)
        self.consumptions = num.calculateConsumptions(self.savingsRates, self.incomes)
        self.avgSavingsC  = num.calculateAvgSavingsC(self.occupNumberC, self.savingsRates, self.sectorIdArray, savingsSumC)
        self.avgSavingsF  = num.calculateAvgSavingsF(self.occupNumberF, self.savingsRates, self.sectorIdArray, savingsSumF)
        self.incomes      = num.calculateIncomes(self.capitalsC, self.capitalsF, self.rentC, self.rentF,\
                                                    self.wagesC, self.wagesF, self.laborsC, self.laborsF)
          

    def pickCandidateAndBestNeighbor(self):
        
        self.candidate, self.bestNeighbor          = nh.NetworkManager().pickCandidateAndBestNeighbor\
                                                    (self.networkGraph, self.consumptions)
                
                
                
              
    def pickNextUpdateTime(self, _tau):
    
        self.updateTime                            = self.time +\
                                                     np.random.exponential(scale=_tau/par.numOfAgents)  
         
    
    def getResults(self):
          
        self.capitalsC, self.capitalsF,\
        self.totalLaborC, self.totalLaborF         = test.RCK_IntegratorTest().returnModelSolutions\
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

    def updateSavingsSector(self):
    
        self.savingsRatesC = self.savingsRates[self.sectorIdArray=='c']  
        self.savingsRatesF = self.savingsRates[self.sectorIdArray=='f']
                     
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
        
        self.savingsRatesMatrixC                   = self.savingsRatesC 
        self.savingsRatesMatrixF                   = self.savingsRatesF   
    
                 
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
        
        self.savingsRatesMatrixC  = np.append(self.savingsRatesMatrixC, self.savingsRatesC)
        self.savingsRatesMatrixF  = np.append(self.savingsRatesMatrixF, self.savingsRatesF)     
              
         
    def initializeMicroDataFrame(self):
    
        self.microDataFrame = pd.DataFrame(columns=["capitalsC", 
                                                    "capitalsF",
                                                    "savingsRates",
                                                    "incomes",
                                                    "consumptions"])
                                                    
    def initializeMacroDataFrame(self):
    
        self.macroDataFrame = pd.DataFrame(columns=["totalCapitalC", 
                                                    "totalCapitalF",
                                                    "totalLaborC",
                                                    "totalLaborF",
                                                    "wagesC",
                                                    "wagesF",
                                                    "rentC",
                                                    "rentF",
                                                    "productionC",
                                                    "productionF",
                                                    "avgSavingsC",
                                                    "avgSavingsF",
                                                    "occupNumberC",
                                                    "occupNumberF"])
                                                    
    def updateMicroDataFrame(self):
    
        microDataFrame = pd.DataFrame({"capitalsC": [self.capitalsC], 
                                        "capitalsF": [self.capitalsF],
                                        "savingsRates": [self.savingsRates],
                                        "incomes":[self.incomes],
                                        "consumptions":[self.consumptions]}, 
                                        index = np.array([self.time]))
                                    
        self.microDataFrame = self.microDataFrame.append(microDataFrame)
        
        
        
                                                    
    def updateMacroDataFrame(self):
    
        macroDataFrame = pd.DataFrame({"totalCapitalC": self.totalCapitalC, 
                                    "totalCapitalF": self.totalCapitalF,
                                    "totalLaborC": self.totalLaborC,
                                    "totalLaborF": self.totalLaborF,
                                    "wagesC": self.wagesC,
                                    "wagesF": self.wagesF,
                                    "rentC": self.rentC,
                                    "rentF": self.rentF,
                                    "productionC": self.productionC,
                                    "productionF": self.productionF,
                                    "avgSavingsC": self.avgSavingsC,
                                    "avgSavingsF": self.avgSavingsF,
                                    "occupNumberC": self.occupNumberC,
                                    "occupNumberF": self.occupNumberF},
                                    index = np.array([self.time]))
                                    
        self.macroDataFrame = self.macroDataFrame.append(macroDataFrame)

 
        
            
    
  
        
        
if __name__ == '__main__':


    myProjectRCK       = ProjectRCK()
    tau=100
    
    myProjectRCK.runModel(tau)


''' END '''
   
    



