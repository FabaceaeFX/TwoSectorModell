import numpy as np


networkTopology       = 'AllToAll'

maxTime               = 10000

tau                   = 500

startEps              = -0.01
endEps                = 0.01
numOfAgents           = 100
  
initSavingsRates      = np.random.rand(numOfAgents)

initCapitalsC         = np.ones(numOfAgents)
#initCapitalsC         = np.random.binomial(n=1, p=0.5, size=[numOfAgents])
initCapitalsF         = np.zeros(numOfAgents)
#initCapitalsF         = np.ones(numOfAgents)-initCapitalsC

cleanInvestorIndex    = np.where(initCapitalsC == 1)
fossilInvestorIndex   = np.where(initCapitalsF == 1)
sectorIdentityArray   = np.empty(numOfAgents, np.unicode_)

sectorIdentityArray[cleanInvestorIndex]  = ('c'+str(cleanInvestorIndex))
sectorIdentityArray[fossilInvestorIndex] = ('f'+str(fossilInvestorIndex))

initLaborsC           = np.random.uniform(1/numOfAgents, 0.01, size=numOfAgents)
initLaborsF           = np.zeros(numOfAgents)

depreciation          = 0.05

deltaS                = 0

alpha                 = 0.5

beta                  = 1 - alpha
        
populationGrowthRate  = 0





plotSetting           = 'Single'
