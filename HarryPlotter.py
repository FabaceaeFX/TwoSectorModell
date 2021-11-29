import ParametersRCK     as par
import matplotlib        as mp
import matplotlib.pyplot as plt
import numpy             as np

class HarryPlotter:

    def __init__(self):
        
        pass
        
    def plotVectors(self, _capitalsCMatrix, _capitalsFMatrix,\
                              _totalCapitalCVector, _totalCapitalFVector):
        

    
        fig, axs = plt.subplots(2, 2)
        
        axs[0, 0].plot(_capitalsCMatrix)
        axs[0, 0].set(xlabel='t', ylabel='Ki')
        axs[0, 0].set_title("Capitals clean")
        
        axs[1, 0].plot(_capitalsFMatrix)
        axs[1, 0].set(xlabel='t', ylabel='Ki')
        axs[1, 0].set_title("Capitals fossil")
        
        axs[0, 1].plot(_totalCapitalCVector)
        axs[0, 1].set(xlabel='t', ylabel='K')
        axs[0, 1].set_title("Total capital in clean sector")
        
        axs[1, 1].plot(_totalCapitalFVector)
        axs[1, 1].set(xlabel='t', ylabel='K')
        axs[1, 1].set_title("Total capital in fossil Sector")
        
        fig.tight_layout()

        plt.show()
