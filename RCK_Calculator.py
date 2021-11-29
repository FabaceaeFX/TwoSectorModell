import numpy as np

import ParametersRCK as par


class RCK_Calculator:

    def __init__(self):
        
        pass
        
        
        
    def getRCKVariables(self, _capitalsC, _capitalsF, _laborsC, _laborsF, _totalCapitalC, _totalCapitalF, _totalLaborC, _totalLaborF, _savingsRates):
        
        wagesC        = self.calculateWages(_totalCapitalC, _totalLaborC)
        wagesF        = self.calculateWages(_totalCapitalF, _totalLaborF)
        rentC         = self.calculateRent(_totalCapitalC, _totalLaborC)
        rentF         = self.calculateRent(_totalCapitalF, _totalLaborF)
        incomesC      = self.calculateIncomes(_capitalsC, _capitalsF, rentC, rentF, wagesC, _laborsC)
        incomesF      = self.calculateIncomes(_capitalsC, _capitalsF, rentC, rentF, wagesF, _laborsF)
        mergedIncomes = self.mergeIncomes(incomesC, incomesF)
        productionC   = self.calculateProduction(_totalCapitalC, _totalLaborC)
        productionF   = self.calculateProduction(_totalCapitalF, _totalLaborF)
        consumptions  = self.calculateConsumptions(_savingsRates, mergedIncomes)
        
        return (wagesC, wagesF, rentC, rentF, productionC, productionF, mergedIncomes, consumptions)
        
        
        
    def calculateWages(self, _totalCapital, _totalLabor):
    
        wages = par.depreciation * par.alpha * _totalLabor ** (par.alpha - 1) * _totalCapital ** par.beta
        
        return wages
        
    def calculateRent(self, _totalCapital, _totalLabor):
    
        rent = par.depreciation * par.beta * _totalLabor ** par.alpha * _totalCapital ** (par.beta - 1)
        
        return rent
                                                             
    def calculateIncomes(self, _capitalsC, _capitalsF, _rentC, _rentF, _wages, _labors):
    
        incomes = _rentC * _capitalsC + _rentF * _capitalsF + _wages * _labors
        
        return incomes
    
    def mergeIncomes(self, _incomesC, _incomesF):
    
        mergedIncomes = _incomesC + _incomesF
        
        return mergedIncomes
                         
    def calculateProduction(self, _totalCapital, _totalLabor):
    
        production = par.depreciation * _totalCapital ** par.beta * _totalLabor ** par.alpha   
        
        return production
         
        
    def calculateConsumptions(self, _savingsRates, _incomes):
    
        consumptions = _incomes * (1 - _savingsRates)
        
        return consumptions
 
