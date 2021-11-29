import numpy as np
import ParametersRCK as par

class Initializer:

    def __init__(self):
        
        pass
        
    def getInitVariables(self):
    
        capitalsC            = par.initCapitalsC
        capitalsF            = par.initCapitalsF
        
        laborsC              = par.initLaborsC
        laborsF              = par.initLaborsF
        
        savingsRates         = par.initSavingsRates
        
        sectorIdArray        = self.createSectorIdentityArray(capitalsC, capitalsF)
        
        return (capitalsC, capitalsF, laborsC, laborsF, sectorIdArray, savingsRates)
    
        
    def createSectorIdentityArray(self, _capitalsC, _capitalsF):   
     
        cleanInvestorIndex                       = np.where(_capitalsC == 1)
        fossilInvestorIndex                      = np.where(_capitalsF == 1)
        sectorIdArray                            = np.empty(par.numOfAgents, np.unicode_)
        sectorIdArray[cleanInvestorIndex]        = ('c'+str(cleanInvestorIndex))
        sectorIdArray[fossilInvestorIndex]       = ('f'+str(fossilInvestorIndex)) 
        
        return sectorIdArray
        
        
        
