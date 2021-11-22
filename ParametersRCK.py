import numpy as np


networkTopology       = 'AllToAll'

maxTime               = 501

tau                   = 20


numOfAgents           = 100
  
initSavingsRates      = np.random.rand(numOfAgents)

initCapitals          = np.ones(numOfAgents)

initLabors            = np.ones(numOfAgents)

depreciation          = 0.5

deltaS                = 0

alpha                 = 0.5

beta                  = 1 - alpha
        
populationGrowthRate  = 0
