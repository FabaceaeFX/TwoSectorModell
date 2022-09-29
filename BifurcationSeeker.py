import numpy as np
import matplotlib.pyplot as plt

import ParametersRCK as par
import ProjectRCK    as rck
import HarryPlotter  as plot
import Pickler as pp


class BifurcationSeeker:

    def __init__(self):
        pass
        
        
    def scanRegimes(self):  
        self.initArray()
        self.initBifurcationMatrix()
        self.initAverageOccupVector()  
        for Index in range(0, len(self.array)):  
            print(Index, 'lenArray=', len(self.array)) 
            self.initSingleSavingsRates()
            self.initOccupNumber()
            self.iterateForSingleValue(Index)
            self.fillBifurcationMatrix(Index)
            self.calcAverageOccupNumber(Index)
        plot.HarryPlotter().plotMultiHeatMap(self.bifurcationMatrixC, self.bifurcationMatrixF, self.averageOccupC, self.averageOccupF, self.array)
        
        
    def initArray(self):
        numOfTicks = int((par.paramMax-par.paramMin)/par.paramDelta+1)
        self.array = np.linspace(par.paramMin, par.paramMax, numOfTicks )  

        
    def initBifurcationMatrix(self):
        self.bifurcationMatrixC = np.zeros((len(self.array), par.iterationMax*par.numOfAgents))
        self.bifurcationMatrixF = np.zeros((len(self.array), par.iterationMax*par.numOfAgents))   
        
    
    def initAverageOccupVector(self):
        self.averageOccupC = np.zeros(len(self.array))
        self.averageOccupF = np.zeros(len(self.array))     
        
                   
    def initSingleSavingsRates(self):
        self.singleSavingsC = np.zeros(par.iterationMax*par.numOfAgents)
        self.singleSavingsF = np.zeros(par.iterationMax*par.numOfAgents) 
        
    
    def initOccupNumber(self):
        self.occupNumberC = np.zeros(par.iterationMax)
        self.occupNumberF = np.zeros(par.iterationMax)
                  
        
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
            self.singleSavingsF[start:stop],\
            self.occupNumberC[iterationIndex],\
            self.occupNumberF[iterationIndex] = rck.ProjectRCK().runModel(tau, seed, subvention, False)
            seed += 1
                
  
    def fillBifurcationMatrix(self, _Index):
        self.bifurcationMatrixC[_Index,:] = self.singleSavingsC
        self.bifurcationMatrixF[_Index,:] = self.singleSavingsF
            
    
    def calcAverageOccupNumber(self, _Index):
        self.averageOccupC[_Index] = sum(self.occupNumberC)/len(self.occupNumberC)
        self.averageOccupF[_Index] = sum(self.occupNumberF)/len(self.occupNumberF)
        
        

if __name__ == '__main__':


    myBifurcationSeeker     = BifurcationSeeker()
    myBifurcationSeeker.scanRegimes()


''' END '''            
        
