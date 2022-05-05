import numpy as np
import matplotlib.pyplot as plt

import ParametersRCK as par
import ProjectRCK    as rck
import HarryPlotter  as plot


class BifurcationSeeker:

    def __init__(self):
        
        pass
        
        
    def scanBifurcParamRegimes(self):
        
        self.initBifurcParamArray()
        self.initBifurcationMatrix()
       
        
        for bifurcParamIndex in range(0, len(self.bifurcParamArray)):
            
            self.initSingleBifurcParamSavingsRates()
            self.iterateForSingleBifurcParamValue(bifurcParamIndex)
            self.fillBifurcationMatrix(bifurcParamIndex)
            
        plot.HarryPlotter().plotHeatMap(self.bifurcationMatrixC, self.bifurcParamArray)
        plot.HarryPlotter().plotHeatMap(self.bifurcationMatrixF, self.bifurcParamArray)
        
        
        
    def initBifurcParamArray(self):
        
        self.bifurcParamArray = np.linspace(par.bifurcParamMin, par.bifurcParamMax, int((par.bifurcParamMax-par.bifurcParamMin)/par.deltaBifurcParam+1))  

        
    def initBifurcationMatrix(self):
    
        self.bifurcationMatrixC = np.zeros((len(self.bifurcParamArray), par.iterationMax*par.numOfAgents))
        self.bifurcationMatrixF = np.zeros((len(self.bifurcParamArray), par.iterationMax*par.numOfAgents))
        
        
                   
    def initSingleBifurcParamSavingsRates(self):
    
        self.singleBifurcParamSavingsC = np.zeros(par.iterationMax*par.numOfAgents)
        self.singleBifurcParamSavingsF = np.zeros(par.iterationMax*par.numOfAgents)   
                  
        
    def iterateForSingleBifurcParamValue(self, _bifurcParamIndex):
    
 
        seed  = 1
        subvention = 1
        
        for iterationIndex in range(0, par.iterationMax):
             
            start    =  iterationIndex*par.numOfAgents
            stop     = (iterationIndex+1)*par.numOfAgents   
            bifurcParamValue = self.bifurcParamArray[_bifurcParamIndex]
            
            if par.bifurcationParameter == 'tau':
                tau = bifurcParamValue
                subvention = par.subvention
                
            if par.bifurcationParameter == 'subvention':
                subvention = bifurcParamValue
                tau = par.tau
            
            
            self.singleBifurcParamSavingsC[start:stop],\
            self.singleBifurcParamSavingsF[start:stop] = rck.ProjectRCK().runModel(tau, seed, subvention)
            
            seed += 1
                
        
        
        
    def fillBifurcationMatrix(self, _bifurcParamIndex):
    
        self.bifurcationMatrixC[_bifurcParamIndex,:] = self.singleBifurcParamSavingsC
        self.bifurcationMatrixF[_bifurcParamIndex,:] = self.singleBifurcParamSavingsF
            

if __name__ == '__main__':


    myBifurcationSeeker     = BifurcationSeeker()

    
    
    myBifurcationSeeker.scanBifurcParamRegimes()


''' END '''            
        
