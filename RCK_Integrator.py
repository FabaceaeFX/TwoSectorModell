from scipy.integrate import odeint
import numpy as np

import ParametersRCK as par


class RCK_Integrator:

    def __init__(self):   
       
        self.capitalDots        = 0
        self.totalLaborDot      = 0
        self.capitalResults     = 0
        self.totalLaborResult   = 0
        
    
    def returnModelSolutions(self, _capitals, _savingsRates, _incomes, _time, _updateTime):
        
        self.concatenateCapitalsAndTotalLabor(_capitals)
        self.getCapitalDots(_capitals, _savingsRates, _incomes)
        self.getTotalLaborDot()
        self.solveCapitalDEQ(_time, _updateTime)
        

        return self.capitalResults, self.totalLaborResult
        
        
   
   
   
   
    def concatenateCapitalsAndTotalLabor(self, _capitals):
    
        self.concatenatedInits = np.append(_capitals, par.totalLabor)
        
        
    def getCapitalDots(self, _capitals, _savingsRates, _incomes):
    
        self.capitalDots = _savingsRates * _incomes - _capitals * par.depreciation
    
    
    def getTotalLaborDot(self):

        self.totalLaborDot = par.populationGrowthRate * par.totalLabor
        
    
    def solveCapitalDEQ(self, _time, _updateTime):
    
        integrationInterval   = [_time, _updateTime]

        DEQResults            = odeint(self.RCKderiv, self.concatenatedInits, 
                                integrationInterval)[1]      
        DEQResults            = self.filterOutNegativeResults(DEQResults) 
        print(DEQResults)   
                   
        self.capitalResults   = DEQResults[: par.numOfAgents]
        self.totalLaborResult = DEQResults[par.numOfAgents : ]
        
        
    def RCKderiv(self, _concatenatedInits, _integrationTime):

        self.concatenatedDots = np.append(self.capitalDots, self.totalLaborDot)
        
        return self.concatenatedDots
        
        
    def filterOutNegativeResults(self, _DEQResults):
   
        filteredResults  = np.where(_DEQResults[0 : par.numOfAgents] > 0,\
                               _DEQResults[0 : par.numOfAgents], \
                               np.zeros(par.numOfAgents))
                               
        return filteredResults
        
        


            
            

