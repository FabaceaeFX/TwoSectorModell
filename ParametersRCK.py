import numpy as np


networkTopology   = 'AllToAll'

maxTime          = 100

tau              = 20


numOfAgents      = 5

initSavingsRates = np.random.rand(numOfAgents)

initCapitals     = np.ones(numOfAgents)

initIncomes      = 0

initConsumptions = 1 - initSavingsRates

depreciation     = 0.5

deltaS           = 0

alpha            = 0.5

beta             = 1 - alpha

populationGrowthRate = 0

initTotalCapital = initCapitals.sum()

labors = np.ones(numOfAgents)

totalLabor = np.array(sum(labors))

initProduction = 0.0
        
