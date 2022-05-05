import numpy as np

#General settings

numOfAgents            = 100
networkTopology        = 'AllToAll'
tmax                   = 100000
tau                    = 200


startEps               = -0.01
endEps                 = 0.01

depreciation           = 0.05
alpha                  = 0.5
beta                   = 1 - alpha        
populationGrowthRate   = 0
explorationProb        = 0.001
subvention             = 1
steuer                 = 1

seed                   = 10

#General plot settings

plotSetting            = 'Two'

tmin                   = 0
tend                   = 100000

smin                   = 0
smax                   = 1

fontsize               = 32
ticksize               = 25


#Bifurcation diagramm

bifurcationParameter   = 'subvention'
bifurcParamMin         = 1
bifurcParamMax         = 1.1
deltaBifurcParam       = 0.001
iterationMax           = 4
numOfBins              = 100
vmax                   = 70


