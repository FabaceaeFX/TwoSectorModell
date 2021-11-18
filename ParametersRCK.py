import numpy as np


networkTopology       = 'AllToAll'

maxTime               = 500

tau                   = 20


numOfAgents           = 100
  
initSavingsRates      = np.random.rand(numOfAgents)

initCapitals          = np.ones(numOfAgents)

initLabors            = np.ones(numOfAgents)

initIncomes           = np.zeros(numOfAgents)

initConsumptions      = 1 - initSavingsRates

totalLabor            = sum(initLabors)

depreciation          = 0.5

deltaS                = 0

alpha                 = 0.5

beta                  = 1 - alpha
        
populationGrowthRate  = 0
