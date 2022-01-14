import numpy as np
import ParametersRCK as par

class Initializer:

    def __init__(self):
        
        pass
        
    def getInitVariables(self):
    
        capitalsC, capitalsF = self.createInitCapitals()
        laborsC, laborsF     = self.createInitLabors()
        savingsRates         = self.createInitSavingsRates()
        sectorIdArray        = self.createSectorIdentityArray(capitalsC, capitalsF)
        
        return (capitalsC, capitalsF, laborsC, laborsF, sectorIdArray, savingsRates)
    
    
    def createInitCapitals(self):
    
        capitalsC            = np.random.binomial(n=1, p=0.5, size=[par.numOfAgents])
        capitalsF            = np.ones(par.numOfAgents)-capitalsC
        
        return capitalsC, capitalsF
        
    def createInitLabors(self):
    
        laborIndexes         = np.random.binomial(n=1, p=0.5, size=[par.numOfAgents])
        laborsC              = laborIndexes*np.random.uniform(1/par.numOfAgents, 0.01, size=par.numOfAgents)
        laborsF              = (np.ones(par.numOfAgents)-laborIndexes)*np.random.uniform(1/par.numOfAgents, 0.01, size=par.numOfAgents)
        
        return laborsC, laborsF
    
    def createInitSavingsRates(self):
    
        savingsRates         = np.random.rand(par.numOfAgents)
        
        return savingsRates    
       
    def createSectorIdentityArray(self, _capitalsC, _capitalsF):   
     
        c                    = np.where(_capitalsC == 1)
        f                    = np.where(_capitalsF == 1)
        sectorIdArray        = np.empty(par.numOfAgents, np.unicode_)
        sectorIdArray[c]     = ('c'+str(c))
        sectorIdArray[f]     = ('f'+str(f)) 
        
        return sectorIdArray
        
        
        
