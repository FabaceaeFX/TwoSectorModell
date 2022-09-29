import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp

import ParametersRCK as par
import ProjectRCK    as rck
import HarryPlotter  as plot
import pickle
from random import random


class ParallelProcessor:

    def __init__(self):
        numOfTicks = int((par.paramMax-par.paramMin)/par.paramDelta+1)
        self.array = np.linspace(par.paramMin, par.paramMax, numOfTicks ) 
        with open(par.fileName, 'wb') as dataStorage:
            pass
        
        
    def solveAndSaveMultipleRuns(self):
        for i in range(0, len(self.array)): 
            pool = mp.Pool(mp.cpu_count()-1)
            print(self.array[i])
            for j in range(0, par.iterationMax):
                print(j)
                parameter = self.array[i]
                if par.parameter == 'tau':
                    self.tau = parameter
                    self.subvention = par.subvention
                    self.probabilityDist = par.probabilityDist    
                if par.parameter == 'subvention':
                    self.subvention = parameter
                    self.tau = par.tau 
                    self.probabilityDist = par.probabilityDist
                if par.parameter == 'probabilityDist':
                    self.probabilityDist = parameter
                    self.subvention = par.subvention
                    self.tau = par.tau 
                pool.apply_async(self.solveRCK, args = (j, ), callback=self.pickleResults)
            pool.close()
            pool.join()

    def solveRCK(self, _seed):
        results = rck.ProjectRCK().runModel(self.tau, _seed, self.subvention, False, self.probabilityDist)
        return results


    def pickleResults(self, _results):
        with open(par.fileName, 'ab+') as dataStorage:
            pickle.dump(_results, dataStorage)
            
        
if __name__ == '__main__':


    myParallelProcessor     = ParallelProcessor()
    myParallelProcessor.solveAndSaveMultipleRuns()


''' END '''            
        
