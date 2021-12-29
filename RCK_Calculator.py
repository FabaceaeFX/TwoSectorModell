import numpy as np
from numba import njit
import pdb

import ParametersRCK as par


class RCK_Calculator:

    def __init__(self):
        
        pass
        
        
 
    def getRCKVariables(self, _capitalsC, _capitalsF, _laborsC, _laborsF, _savingsRates, _sectorIdArray):
        
        totalCapitalC = np.int64(sum(_capitalsC))   
        totalCapitalF = np.int64(sum(_capitalsF))
        totalLaborC   = np.int64(sum(_laborsC))  
        totalLaborF   = np.int64(sum(_laborsF))
        occupNumberC  = np.int64(sum(_sectorIdArray=='c'))
        occupNumberF  = np.int64(sum(_sectorIdArray=='f'))
        
        wagesC        = np.asarray(self.calculateWages(totalCapitalC, totalLaborC))
        wagesF        = np.asarray(self.calculateWages(totalCapitalF, totalLaborF))
        rentC         = np.single(self.calculateRent(totalCapitalC, totalLaborC))
        rentF         = np.single(self.calculateRent(totalCapitalF, totalLaborF))
        incomes       = self.calculateIncomes(_capitalsC, _capitalsF, rentC, rentF, wagesC, wagesF, _laborsC, _laborsF)
        productionC   = self.calculateProduction(totalCapitalC, totalLaborC)
        productionF   = self.calculateProduction(totalCapitalF, totalLaborF)
        consumptions  = self.calculateConsumptions(_savingsRates, incomes)
        avgSavingsC   = self.getAvgSavingsC(occupNumberC, _savingsRates, _sectorIdArray)
        avgSavingsF   = self.getAvgSavingsF(occupNumberF, _savingsRates, _sectorIdArray)
        
        
        return (wagesC, wagesF, rentC, rentF, productionC, productionF, incomes, consumptions,\
                totalCapitalC, totalCapitalF, occupNumberC, occupNumberF, avgSavingsC, avgSavingsF)
                
                
                
        
        

    def calculateWages(self, _totalCapital, _totalLabor):
        
        if _totalLabor != 0:
        
            wages = par.alpha * _totalLabor ** (par.alpha - 1) * _totalCapital ** par.beta
            
        else: 
        
            wages = 0
        
        return wages
        
        
    def calculateRent(self, _totalCapital, _totalLabor):
    
        if _totalCapital != 0:
        
            print(par.beta, _totalLabor, par.alpha, _totalCapital, par.beta)
            rent =  par.beta * (_totalLabor ** par.alpha) * (_totalCapital ** (par.beta - 1))
            print(rent, 'rent after Calculatiom')
            
        else: 
        
            rent = 0
        
        print(rent, 'rent before return')
        return rent
              
                                                
    def calculateIncomes(self, _capitalsC, _capitalsF, _rentC, _rentF, _wagesC,\
                          _wagesF, _laborsC, _laborsF):
        
        
        incomes = _wagesC * _laborsC + _wagesF * _laborsF + _rentC * _capitalsC + _rentF * _capitalsF 
        
        return incomes
           
                         
    def calculateProduction(self, _totalCapital, _totalLabor):
    
        production = _totalCapital ** par.beta * _totalLabor ** par.alpha   
        
        return production
         
    @njit   
    def calculateConsumptions(self, _savingsRates, _incomes):
    
        consumptions = _incomes * (1 - _savingsRates)
        
        return consumptions
        
        
    def getAvgSavingsC(self, _occupNumberC, _savingsRates, _sectorIdArray):
    
        if _occupNumberC != 0:
            avgSavingsC = sum(_savingsRates[_sectorIdArray=='c'])/_occupNumberC
            
        else:
            avgSavingsC = 0
            
        return avgSavingsC
        
        
    def getAvgSavingsF(self, _occupNumberF, _savingsRates, _sectorIdArray):
    
        if _occupNumberF != 0:
            avgSavingsF = sum(_savingsRates[_sectorIdArray=='f'])/_occupNumberF
            
        else:
            avgSavingsF = 0
        
        return avgSavingsF
        
    
    def getImitationError(self):
    
        imitationError    = np.random.uniform(par.startEps, par.endEps, size=1)
        
        return imitationError
        
        
        
