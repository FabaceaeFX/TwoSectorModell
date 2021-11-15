import numpy as np

import ParametersRCK as par


class RCK_Calculator:

    def __init__(self):
    
        self.wages        = 0
        self.rent         = 0
        self.incomes      = 0
        self.production   = 0
        self.consumptions = 0
        
        
        
    def getRCKVariables(self, _capitals, _savingsRates, _totalCapital):
        
        #print(_totalCapital, "capitals", _capitals)
        self.calculateWages(_totalCapital)
        self.calculateRent(_totalCapital)
        self.calculateIncomes(_capitals)
        self.calculateProduction(_totalCapital)
        self.calculateConsumptions(_savingsRates)
        
        return (self.wages, self.rent, self.incomes, self.production, self.consumptions)
        
        
        
    def calculateWages(self, _totalCapital):
    
        self.wages = par.depreciation * par.alpha * par.totalLabor ** (par.alpha - 1) * _totalCapital ** par.beta
        
    def calculateRent(self, _totalCapital):
    
        self.rent = par.depreciation * par.beta * par.totalLabor ** par.alpha * _totalCapital ** (par.beta - 1)
                                                             
    def calculateIncomes(self, _capitals):
    
        self.incomes = self.rent * _capitals + self.wages * par.labors
    
                         
    def calculateProduction(self, _totalCapital):
    
        self.production = par.depreciation * _totalCapital ** par.beta * par.totalLabor ** par.alpha   
         
        
    def calculateConsumptions(self, _savingsRates):
    
        self.consumptions = self.incomes * (1 - _savingsRates)
 
