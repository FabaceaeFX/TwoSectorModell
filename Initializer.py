import numpy as np
import ParametersRCK as par

class Initializer:

    def __init__(self):
        
        pass
        
    def getInitVariables(self):
    
        capitals            = par.initCapitals
        savingsRates        = par.initSavingsRates
        incomes             = par.initIncomes
        consumptions        = par.initConsumptions
        totalCapital        = sum(par.initCapitals)
        totalLabor          = par.totalLabor
        
        return (capitals, savingsRates, incomes, consumptions, totalCapital, totalLabor)
        
