from scipy.integrate import odeint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import timeit

import Initializer      as init
import RCK_Integrator   as integr
import networkx         as nx
import NetworkCreator   as nc
import HarryPlotter     as plot
import ParametersRCK    as par



class ProjectRCK:
    
    def __init__(self):
        pass
        
    
    def runModel(self, _tau, _seed, _subvention, _isSingleRun):
        self.index               = 0
        self.setRandomSeed(_seed)
        self.getNetworkGraph()
        self.createUpdateArray(_tau)
        self.createUpdateTimeline()
        self.createEmptyArrays()
        self.initializeVariables()
        self.calculateVariables(_subvention)
        self.updateSavingsSector()
        self.pickCandidateAndBestNeighbor()
        self.fillResults()
        self.index+=1
        while self.index < len(self.updateTimeline):
            self.getResults(self.updateTimeline[self.index-1], self.updateTimeline[self.index])
            self.pickCandidateAndBestNeighbor()
            self.copySavingsRateOfBestNeighbor()
            self.updateSavingsSector()     
            self.calculateVariables(_subvention)
            self.fillResults()
            self.index += 1
        if _isSingleRun:
            plot.HarryPlotter().plotVectors(self.updateTimeline,\
                                        self.capitalsCMatrix, self.capitalsFMatrix,\
                                        self.totalCapitalCVector, self.totalCapitalFVector,\
                                        self.avgCapitalCVector, self.avgCapitalFVector,\
                                        self.rentCVector, self.rentFVector,\
                                        self.wagesCVector, self.wagesFVector,\
                                        self.productionCVector, self.productionFVector,\
                                        self.occupNumberCVector, self.occupNumberFVector,\
                                        self.maxConsumCVector, self.maxConsumFVector,\
                                        self.savingsRatesCMatrix, self.savingsRatesFMatrix,\
                                        self.avgSavingsCVector, self.avgSavingsFVector,\
                                        self.incomesCMatrix, self.incomesFMatrix, \
                                        self.incomesMatrix, self.consumptionsMatrix,\
                                        self.sectorIdMatrix, self.bestNeighborMatrix,\
                                        self.eqCapitalCVector, self.eqCapitalFVector)
        return(self.savingsRatesC, self.savingsRatesF)
     
     
    def setRandomSeed(self, _seed):
        np.random.seed(_seed)
           
 
    def getNetworkGraph(self): 
        self.networkGraph, self.neighborhoodMatrix  = nc.NetworkCreator().createNetwork()
        

    def createUpdateArray(self, _tau):
        self.updateArray = np.random.exponential(scale=_tau/par.numOfAgents, size=int((par.numOfAgents/_tau)*par.tmax))
        
        
    def createUpdateTimeline(self):
        self.updateTimeline                           = np.zeros(len(self.updateArray)+1)
        self.updateTimeline[0]                        = 0
        self.updateTimeline[1:]                       = np.cumsum(self.updateArray)
        
        
    def initializeVariables(self):  
        self.capitalsC, self.capitalsF,\
        self.laborsC, self.laborsF,\
        self.sectorIdArray, self.savingsRates,\
        self.bestNeighborVector                  = init.Initializer().getInitVariables() 
    
        
    def calculateVariables(self,  _subvention):
        self.totalCapitalC       = sum(self.capitalsC)
        self.totalCapitalF       = sum(self.capitalsF)
        self.totalLaborC         = sum(self.laborsC)
        self.totalLaborF         = sum(self.laborsF)
        self.occupNumberC        = sum(self.sectorIdArray=='c')
        self.occupNumberF        = sum(self.sectorIdArray=='f')
        savingsSumC              = sum(self.savingsRates[self.sectorIdArray=='c'])
        savingsSumF              = sum(self.savingsRates[self.sectorIdArray=='f'])

        self.wagesC              = self.calculateWages(self.totalCapitalC, self.totalLaborC)
        self.wagesF              = self.calculateWages(self.totalCapitalF, self.totalLaborF)
        self.rentC               = _subvention*self.calculateRents(self.totalCapitalC, self.totalLaborC)
        self.rentF               = self.calculateRents(self.totalCapitalF, self.totalLaborF)
        self.productionC         = self.totalCapitalC ** par.beta * self.totalLaborF ** par.alpha  
        self.productionF         = self.totalCapitalF ** par.beta * self.totalLaborF ** par.alpha 
        self.avgCapitalC         = self.totalCapitalC/par.numOfAgents
        self.avgCapitalF         = self.totalCapitalF/par.numOfAgents 
        self.avgSavingsC         = self.calculateAvgSavings(self.occupNumberC, self.savingsRates, savingsSumC)
        self.avgSavingsF         = self.calculateAvgSavings(self.occupNumberF, self.savingsRates, savingsSumF)
        self.incomes             = self.wagesC * self.laborsC + self.wagesF * self.laborsF + self.rentC * self.capitalsC + self.rentF * self.capitalsF 
        self.incomesC            = self.sortIncomes('c')
        self.incomesF            = self.sortIncomes('f')
        self.consumptions        = self.incomes * (np.ones(len(self.savingsRates)) - self.savingsRates)
        self.maxConsumC          = self.getMaxConsumption('c', self.occupNumberC)
        self.maxConsumF          = self.getMaxConsumption('f', self.occupNumberF)
        self.binarySectorId      = self.transcriptSectorIdArray()
        self.eqCapitalC          = self.calculateEqCapitals(self.wagesC, self.rentC, self.occupNumberC, 'c')
        self.eqCapitalF          = self.calculateEqCapitals(self.wagesF, self.rentF, self.occupNumberF, 'f') 
        
       
    def calculateWages(self, _totalCapital, _totalLabor):
        if _totalLabor != 0:
            wages = par.alpha * _totalLabor ** (par.alpha - 1) * _totalCapital ** par.beta    
        else: 
            wages = 0
        return wages
    
   
    def calculateRents(self, _totalCapital, _totalLabor):
        if _totalCapital != 0:
            rent =  par.beta * _totalLabor ** par.alpha * _totalCapital ** (par.beta - 1)  
        else: 
            rent = 0
        return rent
            
    
    def calculateAvgSavings(self, _occupNumber, _savingsRates, _savingsSum):
        if _occupNumber != 0:
            avgSavings = _savingsSum/_occupNumber
        else:
            avgSavings = None
        return avgSavings


    def getMaxConsumption(self, _sectorId, _occupNumber):
        if _occupNumber == 0:
            return None
        maxConsumption = max(self.consumptions[np.where(self.sectorIdArray==_sectorId)])
        return maxConsumption  


    def calculateEqCapitals(self, _wages, _rent, _occupNumber, _sector):
        eqCapitals = sum((self.savingsRates[self.sectorIdArray==_sector]*_wages)/(par.depreciation-self.savingsRates[self.sectorIdArray==_sector]*_rent))/_occupNumber
        if eqCapitals < 0:
            eqCapitals = 0
        return eqCapitals
      
           
    def transcriptSectorIdArray(self):
        binarySectorId = np.zeros(par.numOfAgents)
        binarySectorId[np.where(self.sectorIdArray=='c')] = 1
        binarySectorId[np.where(self.sectorIdArray=='f')] = 2
        return(binarySectorId)
        
    
    def getResults(self, _currentUpdate, _nextUpdate):
        self.capitalsC, self.capitalsF,\
        self.totalLaborC, self.totalLaborF               = integr.RCK_Integrator().returnModelSolutions\
                                                         (self.capitalsC, self.capitalsF,\
                                                          self.totalLaborC, self.totalLaborF,\
                                                          self.sectorIdArray, self.incomes, self.savingsRates,\
                                                          _currentUpdate, _nextUpdate)  
    
     
    def pickCandidateAndBestNeighbor(self):
        self.candidate                                   = np.random.randint(par.numOfAgents)
        neighborsOfCandidate                             = np.where(self.neighborhoodMatrix[self.candidate] == 1)[0]
        self.neighborsConsumptions                       = self.consumptions[neighborsOfCandidate]
        self.bestNeighbor                                = neighborsOfCandidate[np.argmax(self.neighborsConsumptions)] 
        
        self.bestNeighborVector                          = np.zeros(par.numOfAgents)
        if self.sectorIdArray[self.bestNeighbor] == 'c':
            self.bestNeighborVector[self.bestNeighbor]   = 1
        else:
            self.bestNeighborVector[self.bestNeighbor]   = 2   
          
                    
    def copySavingsRateOfBestNeighbor(self):
       if np.random.rand() < par.explorationProb:
            self.savingsRates[self.candidate]            = np.random.rand()
            if self.sectorIdArray[self.candidate] == 'c':
                self.sectorIdArray[self.candidate]       = 'f'
            else:
                self.sectorIdArray[self.candidate]       = 'c'
            return 0
            
       if self.consumptions[self.bestNeighbor] > self.consumptions[self.candidate]:
            self.savingsRates[self.candidate]            = self.savingsRates[self.bestNeighbor] + np.random.uniform(par.startEps, par.endEps, size=1)
            if self.sectorIdArray[self.candidate]       != self.sectorIdArray[self.bestNeighbor]:
                self.sectorCrossCounter[self.index,\
                                        self.candidate]  = 1      
            self.sectorIdArray[self.candidate]           = self.sectorIdArray[self.bestNeighbor]
            while (self.savingsRates[self.candidate] > 1) or (self.savingsRates[self.candidate] < 0):
                self.savingsRates[self.candidate]        = self.savingsRates[self.bestNeighbor] + np.random.uniform(par.startEps, par.endEps, size=1)
                self.sectorIdArray[self.candidate]       = self.sectorIdArray[self.bestNeighbor]
                
        
    def updateSavingsSector(self):
        savingsRatesC                                    = np.zeros(len(self.savingsRates))
        savingsRatesC[np.where(self.sectorIdArray=='c')] = self.savingsRates[self.sectorIdArray=='c']
        savingsRatesC[np.where(self.sectorIdArray=='f')] = None
        savingsRatesF                                    = np.zeros(len(self.savingsRates))
        savingsRatesF[np.where(self.sectorIdArray=='f')] = self.savingsRates[self.sectorIdArray=='f']
        savingsRatesF[np.where(self.sectorIdArray=='c')] = None
        self.savingsRatesC                               = savingsRatesC
        self.savingsRatesF                               = savingsRatesF  
                                     
                     
    def sortIncomes(self, _sector):
        if _sector == 'c':
            sector2 = 'f'
        else:
            sector2 = 'c'   
        incomes                                          = np.zeros(len(self.incomes))
        incomes[np.where(self.sectorIdArray==_sector)]   = self.incomes[self.sectorIdArray==_sector]
        incomes[np.where(self.sectorIdArray==sector2)]   = None
        return incomes
  
    
    def createEmptyArrays(self):
        self.totalLaborCVector    = np.zeros(len(self.updateTimeline))
        self.totalLaborFVector    = np.zeros(len(self.updateTimeline))
        self.wagesCVector         = np.zeros(len(self.updateTimeline))
        self.wagesFVector         = np.zeros(len(self.updateTimeline))
        self.rentCVector          = np.zeros(len(self.updateTimeline))
        self.rentFVector          = np.zeros(len(self.updateTimeline))
        self.productionCVector    = np.zeros(len(self.updateTimeline))
        self.productionFVector    = np.zeros(len(self.updateTimeline))
        self.totalCapitalCVector  = np.zeros(len(self.updateTimeline))
        self.totalCapitalFVector  = np.zeros(len(self.updateTimeline))
        self.occupNumberCVector   = np.zeros(len(self.updateTimeline))
        self.occupNumberFVector   = np.zeros(len(self.updateTimeline))
        self.avgCapitalCVector    = np.zeros(len(self.updateTimeline))
        self.avgCapitalFVector    = np.zeros(len(self.updateTimeline))
        self.avgSavingsCVector    = np.zeros(len(self.updateTimeline))
        self.avgSavingsFVector    = np.zeros(len(self.updateTimeline))
        self.maxConsumCVector     = np.zeros(len(self.updateTimeline))
        self.maxConsumFVector     = np.zeros(len(self.updateTimeline))
        self.eqCapitalCVector     = np.zeros(len(self.updateTimeline))
        self.eqCapitalFVector     = np.zeros(len(self.updateTimeline))
               
        self.savingsRatesCMatrix  = np.zeros((len(self.updateTimeline), par.numOfAgents))
        self.savingsRatesFMatrix  = np.zeros((len(self.updateTimeline), par.numOfAgents))
        self.capitalsCMatrix      = np.zeros((len(self.updateTimeline), par.numOfAgents))
        self.capitalsFMatrix      = np.zeros((len(self.updateTimeline), par.numOfAgents))
        self.incomesMatrix        = np.zeros((len(self.updateTimeline), par.numOfAgents))
        self.incomesCMatrix       = np.zeros((len(self.updateTimeline), par.numOfAgents))
        self.incomesFMatrix       = np.zeros((len(self.updateTimeline), par.numOfAgents))
        self.savingsRatesMatrix   = np.zeros((len(self.updateTimeline), par.numOfAgents))
        self.consumptionsMatrix   = np.zeros((len(self.updateTimeline), par.numOfAgents))
        self.sectorIdMatrix       = np.zeros((len(self.updateTimeline), par.numOfAgents))
        self.sectorCrossCounter   = np.zeros((len(self.updateTimeline), par.numOfAgents))
        self.bestNeighborMatrix   = np.zeros((len(self.updateTimeline), par.numOfAgents))  

        
    def fillResults(self):          
        self.totalLaborCVector[self.index]    = self.totalLaborC
        self.totalLaborFVector[self.index]    = self.totalLaborF
        self.wagesCVector[self.index]         = self.wagesC
        self.wagesFVector[self.index]         = self.wagesF
        self.rentCVector[self.index]          = self.rentC
        self.rentFVector[self.index]          = self.rentF
        self.productionCVector[self.index]    = self.productionC
        self.productionFVector[self.index]    = self.productionF
        self.totalCapitalCVector[self.index]  = self.totalCapitalC
        self.totalCapitalFVector[self.index]  = self.totalCapitalF
        self.avgCapitalCVector[self.index]    = self.avgCapitalC
        self.avgCapitalFVector[self.index]    = self.avgCapitalF
        self.avgSavingsCVector[self.index]    = self.avgSavingsC
        self.avgSavingsFVector[self.index]    = self.avgSavingsF
        self.occupNumberCVector[self.index]   = self.occupNumberC
        self.occupNumberFVector[self.index]   = self.occupNumberF
        self.maxConsumCVector[self.index]     = self.maxConsumC
        self.maxConsumFVector[self.index]     = self.maxConsumF
        self.eqCapitalCVector[self.index]     = self.eqCapitalC
        self.eqCapitalFVector[self.index]     = self.eqCapitalF
        
        self.capitalsCMatrix[self.index]      = self.capitalsC
        self.capitalsFMatrix[self.index]      = self.capitalsF
        self.incomesMatrix[self.index]        = self.incomes
        self.incomesCMatrix[self.index]       = self.incomesC
        self.incomesFMatrix[self.index]       = self.incomesF
        self.savingsRatesMatrix[self.index]   = self.savingsRates
        self.consumptionsMatrix[self.index]   = self.consumptions
        self.savingsRatesCMatrix[self.index]  = self.savingsRatesC
        self.savingsRatesFMatrix[self.index]  = self.savingsRatesF  
        self.sectorIdMatrix[self.index]       = self.binarySectorId
        self.bestNeighborMatrix[self.index]   = self.bestNeighborVector
               
               
if __name__ == '__main__':
    myProjectRCK       = ProjectRCK()
    myProjectRCK.runModel(par.tau, par.seed, par.subvention, True)
    #import timeit
    #print(timeit.timeit(myProjectRCK.runModel(tau), number=10))

''' END '''
   
    



