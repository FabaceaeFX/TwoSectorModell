import numpy as np
import matplotlib.pyplot as plt

import ParametersRCK as par
import ProjectRCK    as rck
import HarryPlotter  as plot
import pickle


class TwoDPickleReader:

    def __init__(self):
        numOfParam1 = int((par.param1Max-par.param1Min)/par.param1Delta+1)
        numOfParam2 = int((par.param2Max-par.param2Min)/par.param2Delta+1)
        self.paramArray1 = np.linspace(par.param1Min, par.param1Max, numOfParam1 ) 
        self.paramArray2 = np.linspace(par.param2Min, par.param2Max, numOfParam2 ) 
        self.savingsBlockC = np.zeros(par.iterationMax*par.numOfAgents)
        self.savingsBlockF = np.zeros(par.iterationMax*par.numOfAgents)
        self.LowSaversSumMatrixC = np.zeros((len(self.paramArray1), len(self.paramArray2)))
        self.LowSaversSumMatrixF = np.zeros((len(self.paramArray1), len(self.paramArray2)))
        self.unpickleToList()
    
    
    def getResultsFromPickle(self):
        for k in range(0, len(self.paramArray1)):     
          
            for i in range(0, len(self.paramArray2)): 
                self.LowSaversCounterC = 0
                self.LowSaversCounterF = 0
                
                for j in range(0, par.iterationMax):
                    self.wrightToBlock(k, i,j)
                    if np.sum(self.LowSaversC)>par.counterTreshold:
                        self.LowSaversSumC = 1
                    else:
                        self.LowSaversSumC = 0
                    if np.sum(self.LowSaversF)>par.counterTreshold:
                        self.LowSaversSumF = 1
                    else:
                        self.LowSaversSumF = 0
                    self.LowSaversCounterC += self.LowSaversSumC
                    self.LowSaversCounterF += self.LowSaversSumF
             
                    
                self.wrightToMatrix(k,i) 
        self.LowSaversSumMatrixC = np.flip(self.LowSaversSumMatrixC, 0)
        self.LowSaversSumMatrixF = np.flip(self.LowSaversSumMatrixF, 0)
        print( self.paramArray1, self.paramArray2)
        plot.HarryPlotter().plot2DParameterHeatmap(self.LowSaversSumMatrixC, self.LowSaversSumMatrixF, self.paramArray1, self.paramArray2)
        
        
    def unpickleToList(self):
        self.resultsList = []
        with open(par.TwofileName, 'rb') as dataStorage:
            try:
                while True:
                    self.resultsList.append(pickle.load(dataStorage))
            except EOFError:
                pass
    
    
           
    def wrightToBlock(self, _k, _i, _j):
        self.savingsBlockC[_j*par.numOfAgents:(_j+1)*par.numOfAgents] = self.resultsList[_k*(len(self.paramArray2)*par.iterationMax)+(_i*par.iterationMax)+_j][0]
        self.savingsBlockF[_j*par.numOfAgents:(_j+1)*par.numOfAgents] = self.resultsList[_k*(len(self.paramArray2)*par.iterationMax)+(_i*par.iterationMax)+_j][1]
        self.LowSaversC = np.zeros(par.numOfAgents)
        self.LowSaversF = np.zeros(par.numOfAgents)
        self.LowSaversC[np.where(self.savingsBlockC[_j*par.numOfAgents:(_j+1)*par.numOfAgents]<par.savingsTreshold)] = 1 
        self.LowSaversF[np.where(self.savingsBlockF[_j*par.numOfAgents:(_j+1)*par.numOfAgents]<par.savingsTreshold)] = 1
        
  
    
    def wrightToMatrix(self, _k, _i):
        self.LowSaversSumMatrixC[_k,_i] = self.LowSaversCounterC
        self.LowSaversSumMatrixF[_k,_i] = self.LowSaversCounterF  
        
        

        
        
        
if __name__ == '__main__':


    myPickleReader     = TwoDPickleReader()
    myPickleReader.getResultsFromPickle()


''' END '''            
        
