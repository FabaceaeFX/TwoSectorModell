import numpy as np
import matplotlib.pyplot as plt

import ParametersRCK as par
import ProjectRCK    as rck
import HarryPlotter  as plot


class BifurcationSeeker:

    def __init__(self):
        pass
        
        
    def scanRegimes(self):  
        self.initArray()
        self.initBifurcationMatrix()  
        for Index in range(0, len(self.array)):   
            self.initSingleSavingsRates()
            self.iterateForSingleValue(Index)
            self.fillBifurcationMatrix(Index)
        plot.HarryPlotter().plotMultiHeatMap(self.bifurcationMatrixC, self.bifurcationMatrixF, self.array)
        #plot.HarryPlotter().plotHeatMap(self.bifurcationMatrixF, self.array)  
        
        
    def initArray(self):
        numOfTicks = int((par.paramMax-par.paramMin)/par.paramDelta+1)
        self.array = np.linspace(par.paramMin, par.paramMax, numOfTicks )  

        
    def initBifurcationMatrix(self):
        self.bifurcationMatrixC = np.zeros((len(self.array), par.iterationMax*par.numOfAgents))
        self.bifurcationMatrixF = np.zeros((len(self.array), par.iterationMax*par.numOfAgents))        
        
                   
    def initSingleSavingsRates(self):
        self.singleSavingsC = np.zeros(par.iterationMax*par.numOfAgents)
        self.singleSavingsF = np.zeros(par.iterationMax*par.numOfAgents)   
                  
        
    def iterateForSingleValue(self, _Index):
        seed  = 1
        for iterationIndex in range(0, par.iterationMax):
            start     =  iterationIndex*par.numOfAgents
            stop      = (iterationIndex+1)*par.numOfAgents   
            parameter = self.array[_Index]
            print(parameter)
            if par.parameter == 'tau':
                tau = parameter
                subvention = par.subvention    
            if par.parameter == 'subvention':
                subvention = parameter
                tau = par.tau
            self.singleSavingsC[start:stop],\
            self.singleSavingsF[start:stop] = rck.ProjectRCK().runModel(tau, seed, subvention, False)
            seed += 1
                
  
    def fillBifurcationMatrix(self, _Index):
        self.bifurcationMatrixC[_Index,:] = self.singleSavingsC
        self.bifurcationMatrixF[_Index,:] = self.singleSavingsF
            

if __name__ == '__main__':


    myBifurcationSeeker     = BifurcationSeeker()
    myBifurcationSeeker.scanRegimes()


''' END '''            
        
