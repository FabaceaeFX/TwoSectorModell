from scipy.integrate import odeint
import numpy as np

import ParametersRCK as par
import NumbaCalculator as num


class RCK_IntegratorTest:

    def __init__(self): 
          
        self.capitalDotsC          = 0
        self.capitalDotsF          = 0
        
        self.totalLaborDotC        = 0 
        self.totalLaborDotF        = 0
        
    
    def returnModelSolutions(self, _capitalsC, _capitalsF, _totalLaborC,\
                             _totalLaborF, _sectorIdArray, _incomes, _savingsRates,\
                             _time, _updateTime):
        
        
        
        concatenatedInitsC, concatenatedInitsF           = num.concatenateCapitalsAndTotalLabor(_capitalsC, _capitalsF, _totalLaborC, _totalLaborF)    
        indexC                                           = np.where(_sectorIdArray=='c')
        indexF                                           = np.where(_sectorIdArray=='f')
        self.capitalDotsC, self.capitalDotsF             = num.calculateCapitalDots(_capitalsC, _capitalsF, _savingsRates, _incomes, _sectorIdArray, indexC, indexF)
        self.totalLaborDotC, self.totalLaborDotF         = num.calculateTotalLaborDot(_totalLaborC, _totalLaborF)
        
        capitalResultsC, totalLaborResultC   = self.solveCapitalDEQC(_time, _updateTime, concatenatedInitsC)
        capitalResultsF, totalLaborResultF   = self.solveCapitalDEQF(_time, _updateTime, concatenatedInitsF)

        return capitalResultsC, capitalResultsF, totalLaborResultC,\
               totalLaborResultF
       
   
   

        
    
    def solveCapitalDEQC(self, _time, _updateTime, _concatenatedInits):
    
        integrationInterval        = [_time, _updateTime]

        DEQResults                 = odeint(self.getConcatenatedDotsC, _concatenatedInits, 
                                     integrationInterval)[1]      
        DEQResults                 = self.filterOutNegativeResults(DEQResults) 
           
        capitalResults             = DEQResults[: par.numOfAgents]
        totalLaborResult           = DEQResults[par.numOfAgents : ]
        
        return capitalResults, totalLaborResult
        
        
    
    def solveCapitalDEQF(self, _time, _updateTime, _concatenatedInits):
    
        integrationInterval        = [_time, _updateTime]

        DEQResults                 = odeint(self.getConcatenatedDotsF, _concatenatedInits, 
                                     integrationInterval)[1]      
        DEQResults                 = self.filterOutNegativeResults(DEQResults) 
           
        capitalResults             = DEQResults[: par.numOfAgents]
        totalLaborResult           = DEQResults[par.numOfAgents : ]
        
        return capitalResults, totalLaborResult    
        
        
        
        
    def getConcatenatedDotsC(self, _concatenatedInits, _integrationTime):
    
        concatenatedDotsC = num.RCKderiv(self.capitalDotsC, self.totalLaborDotC)
        
        return concatenatedDotsC
        
    
    
    def getConcatenatedDotsF(self, _concatenatedInits, _integrationTime):
    
        concatenatedDotsF = num.RCKderiv(self.capitalDotsF, self.totalLaborDotF)
        
        return concatenatedDotsF
        
      
        
        
    def filterOutNegativeResults(self, _DEQResults):
   
        filteredResults            = np.where(_DEQResults > 0,\
                                     _DEQResults, \
                                     np.zeros(par.numOfAgents+1))
                               
        return filteredResults
