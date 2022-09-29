import numpy as np
import matplotlib.pyplot as plt

import ParametersRCK as par
import ProjectRCK    as rck
import HarryPlotter  as plot
import pickle


class PickleReader:

    def __init__(self):
        numOfTicks = int((par.paramMax-par.paramMin)/par.paramDelta+1)
        self.array = np.linspace(par.paramMin, par.paramMax, numOfTicks ) 
        self.savingsBlockC = np.zeros(par.iterationMax*par.numOfAgents)
        self.savingsBlockF = np.zeros(par.iterationMax*par.numOfAgents)
        self.bifurcationMatrixC = np.zeros((len(self.array), par.iterationMax*par.numOfAgents))
        self.bifurcationMatrixF = np.zeros((len(self.array), par.iterationMax*par.numOfAgents))   
        self.averageOccupC = np.zeros(len(self.array))
        self.averageOccupF = np.zeros(len(self.array))      
        self.occupNumberC = np.zeros(par.iterationMax)
        self.occupNumberF = np.zeros(par.iterationMax)
        self.varianzOccupC = np.zeros(len(self.array))
        self.varianzOccupF = np.zeros(len(self.array))
        self.unpickleToList()
    
    
    def getResultsFromPickle(self):          
        for i in range(0, len(self.array)): 
            for j in range(0, par.iterationMax):
                self.wrightToBlock(i,j)
            self.wrightToMatrix(i)
            self.calcAverageOccupNumber(i) 
            self.calcVarianzOccupNumber(i) 
        plot.HarryPlotter().plotMultiHeatMap(self.bifurcationMatrixC, self.bifurcationMatrixF, self.averageOccupC, self.averageOccupF, self.varianzOccupC, self.varianzOccupF, self.array)
        
        
    def unpickleToList(self):
        self.resultsList = []
        with open(par.fileName, 'rb') as dataStorage:
            try:
                while True:
                    self.resultsList.append(pickle.load(dataStorage))
            except EOFError:
                pass
                
        
    def wrightToBlock(self, _i, _j):
        self.savingsBlockC[_j*par.numOfAgents:(_j+1)*par.numOfAgents] = self.resultsList[(_i*par.iterationMax)+_j][0]
        self.savingsBlockF[_j*par.numOfAgents:(_j+1)*par.numOfAgents] = self.resultsList[(_i*par.iterationMax)+_j][1]
        self.occupNumberC[_j] = self.resultsList[(_i*par.iterationMax)+_j][2]
        self.occupNumberF[_j] = self.resultsList[(_i*par.iterationMax)+_j][3]
        
    
    def wrightToMatrix(self, _i):
        self.bifurcationMatrixC[_i,:] = self.savingsBlockC
        self.bifurcationMatrixF[_i,:] = self.savingsBlockF   
        
        
    def calcAverageOccupNumber(self, _i):
        self.averageOccupC[_i] = sum(self.occupNumberC)/len(self.occupNumberC)
        self.averageOccupF[_i] = sum(self.occupNumberF)/len(self.occupNumberF)
        
     
    def calcVarianzOccupNumber(self, _i):
        distFromMeanC        = np.square(self.occupNumberC-self.averageOccupC[_i])
        distFromMeanF        = np.square(self.occupNumberF-self.averageOccupF[_i])
        self.varianzOccupC[_i] = np.sqrt(1/len(self.occupNumberC)*sum(distFromMeanC))
        self.varianzOccupF[_i] = np.sqrt(1/len(self.occupNumberF)*sum(distFromMeanF))
        
        
        
if __name__ == '__main__':


    myPickleReader     = PickleReader()
    myPickleReader.getResultsFromPickle()


''' END '''            
        
