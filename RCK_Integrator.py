from scipy.integrate import odeint
import numpy as np

import ParametersRCK as par


class RCK_Integrator:

    def __init__(self): 
    
        self.capitalsC           = 0
        self.capitalsF           = 0
        self.totalLaborC         = 0
        self.totalLaborF         = 0  
        self.sectorIdArray       = 0
        self.incomes             = 0
        self.savingsRates        = 0
      
        self.capitalDotsC        = 0
        self.capitalDotsF        = 0
        
        self.totalLaborDotC      = 0
        self.totalLaborDotF      = 0
        
        self.capitalResultsC     = 0
        self.capitalResultsF     = 0
        
        self.totalLaborResultC   = 0
        self.totalLaborResultF   = 0
        
        self.concatenatedInitsC  = 0
        self.concatenatedInitsF  = 0
        
    
    def returnModelSolutions(self, _capitalsC, _capitalsF, _totalLaborC,\
                             _totalLaborF, _sectorIdArray, _incomes, _savingsRates,\
                             _time, _updateTime):
        
        self.capitalsC           = _capitalsC
        self.capitalsF           = _capitalsF
        self.incomes             = _incomes
        self.totalLaborC         = _totalLaborC
        self.totalLaborF         = _totalLaborF
        self.sectorIdArray       = _sectorIdArray
        self.savingsRates        = _savingsRates
        
        
        self.concatenateCapitalsAndTotalLabor()
        self.getCapitalDots()
        self.getTotalLaborDot()
        self.solveCapitalDEQC(_time, _updateTime)
        self.solveCapitalDEQF(_time, _updateTime)
        

        return self.capitalResultsC, self.capitalResultsF, self.totalLaborResultC,\
               self.totalLaborResultF
       
   
   
   
    def concatenateCapitalsAndTotalLabor(self):
    
        self.concatenatedInitsC   = np.append(self.capitalsC, self.totalLaborC)
        self.concatenatedInitsF   = np.append(self.capitalsF, self.totalLaborF)
        
        
    def getCapitalDots(self):
    
        indexC                    = np.where(self.sectorIdArray=='c')
        indexF                    = np.where(self.sectorIdArray=='f')
        depreciationTermC         = -par.depreciation * self.capitalsC
        depreciationTermF         = -par.depreciation * self.capitalsF

        self.capitalDotsC         = np.ones(par.numOfAgents) * depreciationTermC
        self.capitalDotsF         = np.ones(par.numOfAgents) * depreciationTermF
        
        self.capitalDotsC[indexC] += self.savingsRates[indexC]*self.incomes[indexC]                             
        self.capitalDotsF[indexF] += self.savingsRates[indexF]*self.incomes[indexF]
        
    
    
    def getTotalLaborDot(self):

        self.totalLaborDotC        = par.populationGrowthRate * self.totalLaborC
        self.totalLaborDotF        = par.populationGrowthRate * self.totalLaborF
        
    
    def solveCapitalDEQC(self, _time, _updateTime):
    
        integrationInterval        = [_time, _updateTime]

        DEQResults                 = odeint(self.RCKderivC, self.concatenatedInitsC, 
                                     integrationInterval)[1]      
        DEQResults                 = self.filterOutNegativeResults(DEQResults) 
                   
        self.capitalResultsC       = DEQResults[: par.numOfAgents]
        self.totalLaborResultC     = DEQResults[par.numOfAgents : ]
        
        
    def solveCapitalDEQF(self, _time, _updateTime):
    
        integrationInterval        = [_time, _updateTime]

        DEQResults                 = odeint(self.RCKderivF, self.concatenatedInitsF, 
                                     integrationInterval)[1]      
        DEQResults                 = self.filterOutNegativeResults(DEQResults) 
                   
        self.capitalResultsF       = DEQResults[: par.numOfAgents]
        self.totalLaborResultF     = DEQResults[par.numOfAgents : ]
        
        
    def RCKderivC(self, _concatenatedInits, _integrationTime):

        self.concatenatedDotsC     = np.append(self.capitalDotsC, self.totalLaborDotC)
        
        return self.concatenatedDotsC
        
        
    def RCKderivF(self, _concatenatedInits, _integrationTime):

        self.concatenatedDotsF     = np.append(self.capitalDotsF, self.totalLaborDotF)
        
        return self.concatenatedDotsF
        
        
    def filterOutNegativeResults(self, _DEQResults):
   
        filteredResults            = np.where(_DEQResults[0 : par.numOfAgents] > 0,\
                                     _DEQResults[0 : par.numOfAgents], \
                                     np.zeros(par.numOfAgents))
                               
        return filteredResults
        
        


            
            

