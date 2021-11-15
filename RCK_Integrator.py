from scipy.integrate import odeint
import numpy as np

import ParametersRCK as par


class RCK_Integrator:

    def __init__(self):   
       
        self.inputCapitals      = 0
        self.capitalDots        = 0
        self.totalLaborDot      = 0
        self.capitalResults     = 0
        self.totalLaborResult   = 0
        
    
    def returnModelSolutions(self, _capitals, _savingsRates, _incomes, _time, _updateTime):
        
        #print("inputCapitals", _capitals)
        self.inputCapitals = _capitals
        self.filterOutNegativeResults()
        self.concatenateCapitalsAndTotalLabor()
        self.getCapitalDots(_savingsRates, _incomes)
        self.getTotalLaborDot()
        self.solveCapitalDEQ(_time, _updateTime)
        
       # print("Results", self.capitalResults)

        return self.capitalResults, self.totalLaborResult
        
        
   
   
   
   
    def concatenateCapitalsAndTotalLabor(self):
    
        self.concatenatedInits = np.append(self.inputCapitals, par.totalLabor)
        
        
    def getCapitalDots(self, _savingsRates, _incomes):
    
        self.capitalDots = _savingsRates * _incomes - self.inputCapitals * par.depreciation
    
    
    def getTotalLaborDot(self):

        self.totalLaborDot = par.populationGrowthRate * par.totalLabor
        
    
    def solveCapitalDEQ(self, _time, _updateTime):
    
        integrationInterval   = [_time, _updateTime]

        DEQResults            = odeint(self.RCKderiv, self.concatenatedInits, 
                                integrationInterval, mxhnil=1, mxstep=5000000)[1]  
        print("Results", DEQResults)                     
        self.capitalResults   = DEQResults[: par.numOfAgents]
        self.totalLaborResult = DEQResults[par.numOfAgents : ]
        
        
    def RCKderiv(self, _concatenatedInits, _integrationTime):

        print("Inits", _concatenatedInits)
        initCapitals          = _concatenatedInits[:par.numOfAgents]
        initTotalLabor        = _concatenatedInits[par.numOfAgents:]
       
        self.concatenatedDots = np.append(self.capitalDots, self.totalLaborDot)
        
        return self.concatenatedDots
        
        
    def filterOutNegativeResults(self):
   
        self.inputCapitals  = np.where(self.inputCapitals[0 : par.numOfAgents] > 0,\
                               self.inputCapitals[0 : par.numOfAgents], \
                               np.zeros(par.numOfAgents))
        
        


            
            

