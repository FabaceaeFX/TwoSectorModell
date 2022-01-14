import ParametersRCK     as par
import matplotlib        as mp
import matplotlib.pyplot as plt
import numpy             as np

class HarryPlotter:

    def __init__(self):
        
        pass
        
    def plotVectors(self, _capitalsCMatrix, _capitalsFMatrix,\
                          _totalCapitalCVector, _totalCapitalFVector,\
                          _rentCVector, _rentFVector,\
                          _wagesCVector, _wagesFVector,\
                          _productionCVector, _productionFVector,\
                          _occupNumberVectorC, _occupNumberVectorF,\
                          _savingsRatesMatrixC, _savingsRatesMatrixF,\
                          _avgSavingsVectorC, _avgSavingsVectorF,\
                          _incomesMatrix, _consumptionsMatrix):
        
    
        if par.plotSetting == 'Two':
        
            fig, axs = plt.subplots(2, 2)
            
            axs[0, 0].plot(_capitalsCMatrix)
            axs[0, 0].set(xlabel='t', ylabel='Ki')
            axs[0, 0].set_title("Capitals clean")
            
            axs[0, 1].plot(_capitalsFMatrix)
            axs[0, 1].set(xlabel='t', ylabel='Ki')
            axs[0, 1].set_title("Capitals fossil")
            
            axs[1, 0].plot(_savingsRatesMatrixC)
            axs[1, 0].set(xlabel='t', ylabel='Si')
            axs[1, 0].set_title("Savings-rates in sector C")
            
            axs[1, 1].plot(_savingsRatesMatrixF)
            axs[1, 1].set(xlabel='t', ylabel='Si')
            axs[1, 1].set_title("Savings-rates in sector F")
            
      
            
            fig.tight_layout()

            plt.show()
            
            fig, axs = plt.subplots(3, 2)

            
            axs[0, 0].plot(_rentCVector)
            axs[0, 0].set(xlabel='t', ylabel='r_c')
            axs[0, 0].set_title("Rent of renewable sector")
            
            axs[0, 1].plot(_rentFVector)
            axs[0, 1].set(xlabel='t', ylabel='r_f')
            axs[0, 1].set_title("Rent of fossil sector")
            
            axs[1, 0].plot(_occupNumberVectorC)
            axs[1, 0].set(xlabel='t', ylabel='N')
            axs[1, 0].set_title("Occupation number renewable")
            
            axs[1, 1].plot(_occupNumberVectorF)
            axs[1, 1].set(xlabel='t', ylabel='N')
            axs[1, 1].set_title("Occupation number fossil")
            
            axs[2, 0].plot(_avgSavingsVectorC)
            axs[2, 0].set(xlabel='t', ylabel='<Si>')
            axs[2, 0].set_title("Average savings in renewable")
            
            axs[2, 1].plot(_avgSavingsVectorF)
            axs[2, 1].set(xlabel='t', ylabel='<Si>')
            axs[2, 1].set_title("Average savings in fossil")
            
            fig.tight_layout()

            plt.show()
            
            
        if par.plotSetting == 'Single':
        
            fig, axs = plt.subplots(2, 1)
            
            axs[0].plot(_capitalsCMatrix)
            axs[0].set(xlabel='t', ylabel='Ki')
            axs[0].set_title("Capitals clean")
            
            axs[1].plot(_totalCapitalCVector)
            axs[1].set(xlabel='t', ylabel='K')
            axs[1].set_title("Total capital in clean sector")
            
      
            
            fig.tight_layout()

            plt.show()
            
            fig, axs = plt.subplots(3, 2)

            
            axs[0, 0].plot(_rentCVector)
            axs[0, 0].set(xlabel='t', ylabel='r_c')
            axs[0, 0].set_title("Rent of renewable sector")
            
            axs[0, 1].plot(_wagesCVector)
            axs[0, 1].set(xlabel='t', ylabel='w')
            axs[0, 1].set_title("Wages")
            
            axs[1, 0].plot(_savingsRatesMatrix)
            axs[1, 0].set(xlabel='t', ylabel='Si')
            axs[1, 0].set_title("Savings")
            
            axs[1, 1].plot(_consumptionsMatrix)
            axs[1, 1].set(xlabel='t', ylabel='Ci')
            axs[1, 1].set_title("consumptions")
            
            axs[2, 0].plot(_avgSavingsVectorC)
            axs[2, 0].set(xlabel='t', ylabel='<Si>')
            axs[2, 0].set_title("Average savings in renewable")
            
            axs[2, 1].plot(_productionCVector)
            axs[2, 1].set(xlabel='t', ylabel='Yc')
            axs[2, 1].set_title("Production Clean")
            
            fig.tight_layout()

            plt.show()
        
            
    def plotDataFrame(self, _microDataFrame, _macroDataFrame):
        
        print(_microDataFrame["capitalsC"].to_numpy()[0,:])
        
        fig, axs = plt.subplots(2, 2)

        axs[0, 0].plot(_microDataFrame["capitalsC"].to_numpy()[0])
        axs[0, 0].set(xlabel='t', ylabel='Ki')
        axs[0, 0].set_title("Capitals clean")

        axs[0, 1].plot(_microDataFrame["capitalsF"].to_numpy()[0])
        axs[0, 1].set(xlabel='t', ylabel='Ki')
        axs[0, 1].set_title("Capitals fossil")

        axs[1, 0].plot(_microDataFrame["consumptions"].to_numpy()[0])
        axs[1, 0].set(xlabel='t', ylabel='K')
        axs[1, 0].set_title("Total capital in clean sector")

        axs[1, 1].plot(_microDataFrame["savingsRates"].to_numpy()[0])
        axs[1, 1].set(xlabel='t', ylabel='K')
        axs[1, 1].set_title("Total capital in fossil Sector")



        fig.tight_layout()

        plt.show()
            
           
        
    
