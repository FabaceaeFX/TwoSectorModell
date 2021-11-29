import numpy as np


networkTopology       = 'AllToAll'

maxTime               = 500

tau                   = 20


numOfAgents           = 500
  
initSavingsRates      = np.random.rand(numOfAgents)

initCapitalsC         = np.random.binomial(n=1, p=0.5, size=[numOfAgents])
initCapitalsF         = np.ones(numOfAgents)-initCapitalsC

cleanInvestorIndex    = np.where(initCapitalsC == 1)
fossilInvestorIndex   = np.where(initCapitalsF == 1)
sectorIdentityArray   = np.empty(numOfAgents, np.unicode_)
sectorIdentityArray[cleanInvestorIndex]=('c'+str(cleanInvestorIndex))
sectorIdentityArray[fossilInvestorIndex]=('f'+str(fossilInvestorIndex))

initLaborsC           = initCapitalsC
initLaborsF           = initCapitalsF

depreciation          = 0.5

deltaS                = 0

alpha                 = 0.5

beta                  = 1 - alpha
        
populationGrowthRate  = 0
