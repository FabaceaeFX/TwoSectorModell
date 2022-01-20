from scipy.integrate import odeint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

import NumbaCalculator  as numCalc
import NumbaAppender    as numPend
import Initializer      as init
import RCK_Integrator   as rck
import RCK_IntegratorTest as test
import RCK_Calculator   as calc
import networkx         as nx
import NetworkCreator   as nc
import NetworkManager   as nm
import HarryPlotter     as plot
import ParametersRCK    as par



class ProjectRCK:
    
    def __init__(self):
    
        self.Parameter           = par
        self.manager             = nm.NetworkManager()
        self.integrator          = test.RCK_IntegratorTest()
        self.numPend             = numPend
        self.numCalc             = numCalc
        
    
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
        self.occupNumberCVector  = 0
        self.occupNumberFVector  = 0
        
        self.incomes             = 0
        self.incomesMatrix       = 0
      
        self.savingsRates        = 0
        self.savingsRatesMatrix  = 0
        self.savingsRatesC       = 0       
        self.savingsRatesF       = 0
        self.savingsRatesCMatrix = 0
        self.savingsRatesFMatrix = 0
                
        self.avgSavingsC         = 0
        self.avgSavingsF         = 0
        self.avgSavingsCVector   = 0
        self.avgSavingsFVector   = 0

        
        self.consumptions        = 0
        self.consumptionsMatrix  = 0
        
      
    
    def runModel(self, _tau):
    
        tic = time.perf_counter()


   

        self.getNetworkGraph()
        self.initializeVariables()
        self.calculateVariables()
        self.updateSavingsSector()
        self.wrightInitArrayEntries()
    
      
        while self.time < (_tau/par.numOfAgents)*par.maxTime:
                
            self.pickNextUpdateTime(_tau)
            self.pickCandidateAndBestNeighbor()
            self.getResults()
            self.copySavingsRateOfBestNeighbor()
            self.copySectorOfBestNeighbor()
            self.updateSavingsSector()
            self.updateSystemTime()           
            self.calculateVariables()
            self.appendResultsToArrays()

        
        toc = time.perf_counter()

        print(f"RunModel{toc - tic:0.4f} seconds")    
        
        plot.HarryPlotter().plotVectors(self.capitalsCMatrix, self.capitalsFMatrix,\
                              self.totalCapitalCVector, self.totalCapitalFVector,\
                              self.rentCVector, self.rentFVector,\
                              self.wagesCVector, self.wagesFVector,\
                              self.productionCVector, self.productionFVector,\
                              self.occupNumberCVector, self.occupNumberFVector,\
                              self.savingsRatesCMatrix, self.savingsRatesFMatrix,\
                              self.avgSavingsCVector, self.avgSavingsFVector,\
                              self.incomesMatrix, self.consumptionsMatrix)
     
        
     
     
       
 
    def getNetworkGraph(self):
        
        tic = time.perf_counter()
        self.networkGraph, self.neighborhoodMatrix = nc.NetworkCreator().createNetwork()
        toc = time.perf_counter()

        print(f"getNetworkGraph{toc - tic:0.4f} seconds")  
        
    def initializeVariables(self):
        
        tic = time.perf_counter()
        self.capitalsC, self.capitalsF,\
        self.laborsC, self.laborsF,\
        self.sectorIdArray, self.savingsRates      = init.Initializer().getInitVariables()
        toc = time.perf_counter()

        print(f"InitializeVariables{toc - tic:0.4f} seconds")   
    
        
    def calculateVariables(self):

        tic = time.perf_counter()
        self.totalCapitalC       = sum(self.capitalsC)
        self.totalCapitalF       = sum(self.capitalsF)
        self.totalLaborC         = sum(self.laborsC)
        self.totalLaborF         = sum(self.laborsF)
        self.occupNumberC        = sum(self.sectorIdArray=='c')
        self.occupNumberF        = sum(self.sectorIdArray=='f')
        savingsSumC              = sum(self.savingsRates[self.sectorIdArray=='c'])
        savingsSumF              = sum(self.savingsRates[self.sectorIdArray=='c'])
        
        self.wagesC              = numCalc.calculateWages(self.totalCapitalC, self.totalLaborC)
        self.wagesF              = numCalc.calculateWages(self.totalCapitalF, self.totalLaborF)
        self.rentC               = numCalc.calculateRents(self.totalCapitalC, self.totalLaborC)
        self.rentF               = numCalc.calculateRents(self.totalCapitalF, self.totalLaborF)
        self.productionC         = numCalc.calculateProduction(self.totalCapitalC, self.totalLaborC)
        self.productionF         = numCalc.calculateProduction(self.totalCapitalF, self.totalLaborF)
        self.consumptions        = numCalc.calculateConsumptions(self.savingsRates, self.incomes)
        self.avgSavingsC         = numCalc.calculateAvgSavingsC(self.occupNumberC, self.savingsRates, self.sectorIdArray, savingsSumC)
        self.avgSavingsF         = numCalc.calculateAvgSavingsF(self.occupNumberF, self.savingsRates, self.sectorIdArray, savingsSumF)
        self.incomes             = numCalc.calculateIncomes(self.capitalsC, self.capitalsF, self.rentC, self.rentF,\
                                                    self.wagesC, self.wagesF, self.laborsC, self.laborsF)
        toc = time.perf_counter()

        print(f"CalculateVariables{toc - tic:0.4f} seconds")   
          

    def pickCandidateAndBestNeighbor(self):
        
        self.candidate, self.bestNeighbor          = self.manager.pickCandidateAndBestNeighbor\
                                                         (self.networkGraph, self.consumptions)         

              
    def pickNextUpdateTime(self, _tau):
        
        self.updateTime                            = self.time +\
                                                     np.random.exponential(scale=_tau/par.numOfAgents) 
    
    def getResults(self):
        
        tic = time.perf_counter() 
        self.capitalsC, self.capitalsF,\
        self.totalLaborC, self.totalLaborF         = self.integrator.returnModelSolutions\
                                                    (self.capitalsC, self.capitalsF,\
                                                     self.totalLaborC, self.totalLaborF,\
                                                     self.sectorIdArray, self.incomes, self.savingsRates,\
                                                     self.time, self.updateTime)  
        toc = time.perf_counter()

        #print(f"RunIntegrator{toc - tic:0.4f} seconds")          
            
                    
    def copySavingsRateOfBestNeighbor(self):

        if self.consumptions[self.bestNeighbor] > self.consumptions[self.candidate]:
    
            self.savingsRates[self.candidate]      = self.savingsRates[self.bestNeighbor] + np.random.uniform(par.startEps, par.endEps, size=1)
            
            while (self.savingsRates[self.candidate] > 1) or (self.savingsRates[self.candidate] < 0):
            
                self.savingsRates[self.candidate]  = self.savingsRates[self.bestNeighbor] + np.random.uniform(par.startEps, par.endEps, size=1)

        
        
    def copySectorOfBestNeighbor(self):
    
        self.sectorIdArray[self.candidate]         = self.sectorIdArray[self.bestNeighbor]  

    def updateSavingsSector(self):

        savingsRatesC      = np.zeros(len(self.savingsRates))
        savingsRatesC[np.where(self.sectorIdArray=='c')] = self.savingsRates[self.sectorIdArray=='c']
        savingsRatesC[np.where(self.sectorIdArray=='f')] = None
        
        savingsRatesF      = np.zeros(len(self.savingsRates))
        savingsRatesF[np.where(self.sectorIdArray=='f')] = self.savingsRates[self.sectorIdArray=='f']
        savingsRatesF[np.where(self.sectorIdArray=='c')] = None
        
        
        self.savingsRatesC = savingsRatesC
        self.savingsRatesF = savingsRatesF  
                     
    def updateSystemTime(self):
   
        self.time                                  = self.updateTime
        
        
     
    def wrightInitArrayEntries(self):
        
        tic = time.perf_counter()
        self.timeVector           = self.time

        self.totalLaborCVector    = self.totalLaborC
        self.totalLaborFVector    = self.totalLaborF

        self.wagesCVector         = self.wagesC
        self.wagesFVector         = self.wagesF

        self.rentCVector          = self.rentC
        self.rentFVector          = self.rentF

        self.productionCVector    = self.productionC
        self.productionFVector    = self.productionF

        self.totalCapitalCVector  = self.totalCapitalC
        self.totalCapitalFVector  = self.totalCapitalF

        self.capitalsCMatrix      = self.capitalsC
        self.capitalsFMatrix      = self.capitalsF

        self.incomesMatrix        = self.incomes
        self.savingsRatesMatrix   = self.savingsRates
        self.consumptionsMatrix   = self.consumptions  

        self.occupNumberCVector   = self.occupNumberC
        self.occupNumberFVector   = self.occupNumberF

        self.avgSavingsCVector    = self.avgSavingsC
        self.avgSavingsFVector    = self.avgSavingsF

        self.savingsRatesCMatrix  = self.savingsRatesC 
        self.savingsRatesFMatrix  = self.savingsRatesF   
        toc = time.perf_counter()

        #print(f"Wrightfirst{toc - tic:0.4f} seconds")   
    
                 
    def appendResultsToArrays(self):          
        
        tic = time.perf_counter()
            
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
        
        self.avgSavingsCVector    = np.append(self.avgSavingsCVector, self.avgSavingsC)
        self.avgSavingsFVector    = np.append(self.avgSavingsFVector, self.avgSavingsF)
        
        self.occupNumberCVector   = np.append(self.occupNumberCVector, self.occupNumberC)
        self.occupNumberFVector   = np.append(self.occupNumberFVector, self.occupNumberF)
        
        self.capitalsCMatrix      = np.vstack((self.capitalsCMatrix, self.capitalsC))
        self.capitalsFMatrix      = np.vstack((self.capitalsFMatrix, self.capitalsF))
        
        self.incomesMatrix        = np.vstack((self.incomesMatrix, self.incomes))
        self.savingsRatesMatrix   = np.vstack((self.savingsRatesMatrix, self.savingsRates))
        self.consumptionsMatrix   = np.vstack((self.consumptionsMatrix, self.consumptions)) 
        
        self.savingsRatesCMatrix  = np.vstack((self.savingsRatesCMatrix, self.savingsRatesC))
        self.savingsRatesFMatrix  = np.vstack((self.savingsRatesFMatrix, self.savingsRatesF))    
        toc = time.perf_counter()

        print(f"appendResults{toc - tic:0.4f} seconds")    



    def appendResults(self):    
        
        tic = time.perf_counter()
        self.timeVector,\
        self.totalLaborCVector, self.totalLaborFVector,\
        self.wagesCVector, self.wagesFVector,\
        self.rentCVector, self.rentFVector,\
        self.productionCVector, self.productionFVector,\
        self.totalCapitalCVector,self.totalCapitalFVector,\
        self.avgSavingsCVector, self.avgSavingsFVector,\
        self.occupNumberCVector, self.occupNumberFVector,\
                                    = numPend.appendResultsToVectors(self.timeVector, self.time,\
                                                                          self.totalLaborCVector, self.totalLaborC,\
                                                                          self.totalLaborFVector, self.totalLaborF,\
                                                                          self.wagesCVector, self.wagesC,\
                                                                          self.wagesFVector, self.wagesF,\
                                                                          self.rentCVector, self.rentC,\
                                                                          self.rentFVector, self.rentF,\
                                                                          self.productionCVector, self.productionC,\
                                                                          self.productionFVector, self.productionF,\
                                                                          self.totalCapitalCVector, self.totalCapitalC,\
                                                                          self.totalCapitalFVector, self.totalCapitalF,\
                                                                          self.avgSavingsCVector, self.avgSavingsC,\
                                                                          self.avgSavingsFVector, self.avgSavingsF,\
                                                                          self.occupNumberCVector, self.occupNumberC,\
                                                                          self.occupNumberFVector, self.occupNumberF)
        
        
        self.capitalsCMatrix, self.capitalsFMatrix,\
        self.incomesMatrix, self.savingsRatesMatrix,\
        self.consumptionsMatrix, self.savingsRatesCMatrix,\
        self.savingsRatesFMatrix  =  self.numPend.appendResultsToMatrices(self.capitalsCMatrix, self.capitalsC,\
                                                                          self.capitalsFMatrix, self.capitalsF,\
                                                                          self.incomesMatrix, self.incomes,\
                                                                          self.savingsRatesMatrix, self.savingsRates,\
                                                                          self.consumptionsMatrix, self.consumptions,\
                                                                          self.savingsRatesCMatrix, self.savingsRatesC,\
                                                                          self.savingsRatesFMatrix, self.savingsRatesF)
        
        
        
        
        toc = time.perf_counter()

        print(f"appendResults{toc - tic:0.4f} seconds")  
        
if __name__ == '__main__':


    myProjectRCK       = ProjectRCK()
    tau=400
    
    myProjectRCK.runModel(tau)


''' END '''
   
    



