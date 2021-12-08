from scipy.integrate import odeint
import numpy as np

import ParametersRCK as par


class RCK_Integrator:

    def __init__(self): 
          
        self.capitalDotsC          = 0
        self.capitalDotsF          = 0
        
        self.totalLaborDotC        = 0
        self.totalLaborDotF        = 0
        
        self.capitalResultsC       = 0
        self.capitalResultsF       = 0
        
        self.totalLaborResultC     = 0
        self.totalLaborResultF     = 0
        
        self.concatenatedInitsC    = 0
        self.concatenatedInitsF    = 0
        
    
    def returnModelSolutions(self, _capitalsC, _capitalsF, _totalLaborC,\
                             _totalLaborF, _sectorIdArray, _incomes, _savingsRates,\
                             _time, _updateTime):
        
        
        
        self.concatenateCapitalsAndTotalLabor(_capitalsC, _capitalsF, _totalLaborC, _totalLaborF)
        self.getCapitalDots(_capitalsC, _capitalsF, _savingsRates, _incomes, _sectorIdArray)
        self.getTotalLaborDot(_totalLaborC, _totalLaborF)
        self.solveCapitalDEQC(_time, _updateTime)
        self.solveCapitalDEQF(_time, _updateTime)

        return self.capitalResultsC, self.capitalResultsF, self.totalLaborResultC,\
               self.totalLaborResultF
       
   
   
   
    def concatenateCapitalsAndTotalLabor(self, _capitalsC, _capitalsF, _totalLaborC, _totalLaborF):
    
        self.concatenatedInitsC    = np.append(_capitalsC, _totalLaborC)
        self.concatenatedInitsF    = np.append(_capitalsF, _totalLaborF)
        
        
    def getCapitalDots(self, _capitalsC, _capitalsF, _savingsRates, _incomes, _sectorIdArray):
        
        indexC                     = np.where(_sectorIdArray=='c')
        indexF                     = np.where(_sectorIdArray=='f')
        depreciationTermC          = -par.depreciation * _capitalsC
        depreciationTermF          = -par.depreciation * _capitalsF

        self.capitalDotsC          = np.ones(par.numOfAgents) * depreciationTermC
        self.capitalDotsF          = np.ones(par.numOfAgents) * depreciationTermF
        
        self.capitalDotsC[indexC] += _savingsRates[indexC]*_incomes[indexC]                             
        self.capitalDotsF[indexF] += _savingsRates[indexF]*_incomes[indexF]
        
    
    
    def getTotalLaborDot(self, _totalLaborC, _totalLaborF):

        self.totalLaborDotC        = par.populationGrowthRate * _totalLaborC
        self.totalLaborDotF        = par.populationGrowthRate * _totalLaborF
        
    
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
   
        filteredResults            = np.where(_DEQResults > 0,\
                                     _DEQResults, \
                                     np.zeros(par.numOfAgents+1))
                               
        return filteredResults
        
        


            
            

