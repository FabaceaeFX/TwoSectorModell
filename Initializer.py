import numpy as np
import ParametersRCK as par

class Initializer:

    def __init__(self):
        
        pass
        
    def getInitVariables(self):
    
        capitals            = par.initCapitals
        savingsRates        = par.initSavingsRates
        labors              = par.initLabors
        
        return (capitals, savingsRates, labors)
        
