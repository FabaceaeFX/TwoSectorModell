import numpy as np

import ParametersRCK as par


class RCK_Calculator:

    def __init__(self):
        
        pass
        
        
        
    def getRCKVariables(self, _capitalsC, _capitalsF, _laborsC, _laborsF, _savingsRates, _sectorIdArray):
        
        totalCapitalC = sum(_capitalsC)   
        totalCapitalF = sum(_capitalsF)
        totalLaborC   = sum(_laborsC)  
        totalLaborF   = sum(_laborsF)
        occupNumberC  = sum(_sectorIdArray=='c')
        occupNumberF  = sum(_sectorIdArray=='f')
        
        wagesC        = self.calculateWages(totalCapitalC, totalLaborC)
        wagesF        = self.calculateWages(totalCapitalF, totalLaborF)
        rentC         = self.calculateRent(totalCapitalC, totalLaborC)
        rentF         = self.calculateRent(totalCapitalF, totalLaborF)
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
        
            rent =  par.beta * _totalLabor ** par.alpha * _totalCapital ** (par.beta - 1)
            
        else: 
        
            rent = 0
        
        return rent
              
                                                             
    def calculateIncomes(self, _capitalsC, _capitalsF, _rentC, _rentF, _wagesC,\
                          _wagesF, _laborsC, _laborsF):
    
        incomes = _wagesC * _laborsC + _wagesF * _laborsF + _rentC * _capitalsC + _rentF * _capitalsF 
        
        return incomes
           
                         
    def calculateProduction(self, _totalCapital, _totalLabor):
    
        production = _totalCapital ** par.beta * _totalLabor ** par.alpha   
        
        return production
         
        
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
