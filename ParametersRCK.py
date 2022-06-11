import numpy as np

#General settings

numOfAgents            = 100
networkTopology        = 'AllToAll'
tmax                   = 10000
tau                    = 280


startEps               = -0.01
endEps                 = 0.01

depreciation           = 0.05
alpha                  = 0.5
beta                   = 1 - alpha        
populationGrowthRate   = 0
explorationProb        = 0.001
subvention             = 1.1
steuer                 = 1

seed                   = 2      

#General plot settings

plotSetting            = 'Two'
singleRun              = False

tmin                   = 0
tend                   = 100000

smin                   = 0
smax                   = 1

fontsize               = 32
ticksize               = 25


#Bifurcation diagramm

parameter              = 'tau'
paramMin               = 100
paramMax               = 300
paramDelta             = 1
iterationMax           = 1
numOfBins              = 1000



