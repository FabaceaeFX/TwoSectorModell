import ParametersRCK     as par
import matplotlib        as mp
import matplotlib.pyplot as plt
import numpy             as np

class HarryPlotter:

    def __init__(self):
        
        pass
        
    def plotVectors(self, _capitalsMatrix, _savingsRatesMatrix,\
                              _totalCapitalVector, _productionVector):
        

    
        fig, axs = plt.subplots(2, 2)
        
        axs[0, 0].plot(_capitalsMatrix)
        axs[0, 0].set(xlabel='t', ylabel='Ki')
        axs[0, 0].set_title("Capitals of 100 agents over time")
        
        axs[1, 0].plot(_savingsRatesMatrix)
        axs[1, 0].set(xlabel='t', ylabel='Si')
        axs[1, 0].set_title("Savingsrates of 100 Agents over time")
        
        axs[0, 1].plot(_totalCapitalVector)
        axs[0, 1].set(xlabel='t', ylabel='K')
        axs[0, 1].set_title("Total capital over time")
        
        axs[1, 1].plot(_productionVector)
        axs[1, 1].set(xlabel='t', ylabel='Y')
        axs[1, 1].set_title("Production over time")
        
        fig.tight_layout()

        plt.show()
