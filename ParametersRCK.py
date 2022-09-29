import numpy as np

#General settings

numOfAgents            = 100
networkTopology        = 'AllToAll'
tmax                   = 10000
tau                    = 400
probabilityDist        = 0.5
seed                   = 10  
singleRun              = True
newRun                 = False


startEps               = -0.01
endEps                 = 0.01

depreciation           = 0.01
alpha                  = 0.5
beta                   = 1 - alpha        
populationGrowthRate   = 0
explorationProb        = 0.001
subvention             = 1
steuer                 = 1

    

#General plot settings

plotSetting            = 'Two'
smin                   = 0
smax                   = 1
plotStart              = 0
plotStop               = 100000
fontsize               = 25
ticksize               = 20


#Bifurcation diagramm

parameter              = 'tau'
paramMin               = 100      
paramMax               = 400
paramDelta             = 20
iterationMax           = 100
numOfBins              = 1000

fileName               = r'C:\fabaceae\Desktop\PIK\Plots\Results\tau='+ \
                         "N=" + str(numOfAgents) + ", run = " +\
                          str(iterationMax) + ", tmax =" + str(tmax) + \
                          "Parameter = " + parameter + ", tau =" + str(tau) + \
                          "Subvention =" + str(subvention) + "in range" + \
                          str(paramMin) + str(paramMax) +'depreciation =' + str(depreciation)


#2D Parameter Analysis

param1    = 'gamma'
param1Min = 0.5
param1Max = 1.5
param1Delta = 0.1

param2    = 'tau'
param2Min = 100
param2Max = 400
param2Delta = 20

savingsTreshold = 0.2
counterTreshold = 20

TwofileName = r'C:\fabaceae\Desktop\PIK\Plots\Results\tau='+ \
                         "N=" + str(numOfAgents) + ", run = " +\
                          str(iterationMax) + ", tmax =" + str(tmax) + \
                          "Parameter1 =" + param1 + "in range" + str(param1Min) + str(param1Max)+\
                          "Parameter2 =" + param2 + "in range" + str(param2Min) + str(param2Max)
                          
