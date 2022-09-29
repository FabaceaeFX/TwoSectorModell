import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp

import ParametersRCK as par
import ProjectRCK    as rck
import HarryPlotter  as plot
import pickle
from random import random


class TwoDParallelProcessor:

    def __init__(self):
        numOfParam1 = int((par.param1Max-par.param1Min)/par.param1Delta+1)
        numOfParam2 = int((par.param2Max-par.param2Min)/par.param2Delta+1)
        self.paramArray1 = np.linspace(par.param1Min, par.param1Max, numOfParam1) 
        self.paramArray2 = np.linspace(par.param2Min, par.param2Max, numOfParam2) 
        with open(par.TwofileName, 'wb') as dataStorage:
            pass
        
        
    def solveAndSaveMultipleRuns(self):
        
        for k in range(0, len(self.paramArray1)):
            print(k)
            for i in range(0, len(self.paramArray2)): 
                print(i)
                pool = mp.Pool(mp.cpu_count()-1)
                for j in range(0, par.iterationMax):
                    parameter1 = self.paramArray1[k]
                    parameter2 = self.paramArray2[i]
                    self.subvention = parameter1
                    self.tau = parameter2
                    self.probabilityDist = par.probabilityDist
                    pool.apply_async(self.solveRCK, args = (j, ), callback=self.pickleResults)
                pool.close()
                pool.join()

    def solveRCK(self, _seed):
        results = rck.ProjectRCK().runModel(self.tau, _seed, self.subvention, False, self.probabilityDist)
        return results


    def pickleResults(self, _results):
        with open(par.TwofileName, 'ab+') as dataStorage:
            pickle.dump(_results, dataStorage)
            
        
if __name__ == '__main__':


    myParallelProcessor     = TwoDParallelProcessor()
    myParallelProcessor.solveAndSaveMultipleRuns()


''' END '''            
        
