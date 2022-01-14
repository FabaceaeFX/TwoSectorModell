import numpy as np
import matplotlib.pyplot as plt

import ParametersRCK as par
import ProjectRCK    as rck


class BifurcationSeeker:

    def __init__(self):
        
        self.bifurcationMatrixC = 0
        self.bifurcationMatrixF = 0
        self.singleTauSavingsC  = 0
        self.singleTauSavingsF  = 0
        
        
    def scanTauRegimes(self):
        
        self.iterateForSingleTauValue(par.tauMin)
        self.wrightInitBifurcationEntry()
       
        
        for tau in range(par.tauMin + par.deltaTau, par.tauMax):
            
            self.resetSingleTauSavings()
            self.iterateForSingleTauValue(tau)
            self.appendSingleTauSavingsToBifurcationMatrix()
            
                 
            
                  
        
    def iterateForSingleTauValue(self, _tau):
    
        for iteration in range(0, par.iterationMax):
            
                runner  = rck.ProjectRCK()
                lastSavingsRatesC, lastSavingsRatesF = runner.runModel(_tau)
                
                self.singleTauSavingsC = np.append(self.singleTauSavingsC, lastSavingsRatesC)
                self.singleTauSavingsF = np.append(self.singleTauSavingsF, lastSavingsRatesF)
                
                
    def resetSingleTauSavings(self):
    
        self.singleTauSavingsC = 0
        self.singleTauSavingsF = 0
                  
       
    def wrightInitBifurcationEntry(self):
        
        self.bifurcationMatrixC = self.singleTauSavingsC
        self.bifurcationMatrixF = self.singleTauSavingsF
        
    def appendSingleTauSavingsToBifurcationMatrix(self):
    
        self.bifurcationMatrixC = np.vstack((self.bifurcationMatrixC, self.singleTauSavingsC))
        self.bifurcationMatrixF = np.vstack((self.bifurcationMatrixF, self.singleTauSavingsF))
            
        

if __name__ == '__main__':


    myBifurcationSeeker     = BifurcationSeeker()

    
    
    myBifurcationSeeker.scanTauRegimes()


''' END '''            
        
