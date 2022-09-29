import ParametersRCK     as par
import matplotlib        as mp
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm, LogNorm
import numpy             as np
import string


        

class SingleHarryPlotter:


    def __init__(self):
        pass
        
        
    def plotVectors(self, _tauTimeline,\
                          _capitalsCMatrix, _capitalsFMatrix,\
                          _totalCapitalCVector, _totalCapitalFVector,\
                          _avgCapitalCVector, _avgCapitalFVector,\
                          _rentCVector, _rentFVector,\
                          _wagesCVector, _wagesFVector,\
                          _productionCVector, _productionFVector,\
                          _occupNumberVectorC, _occupNumberVectorF,\
                          _maxConsumCVector, _maxConsumFVector,\
                          _savingsRatesMatrixC, _savingsRatesMatrixF,\
                          _avgSavingsVectorC, _avgSavingsVectorF,\
                          _incomesCMatrix, _incomesFMatrix,\
                          _incomesMatrix, _consumptionsMatrix,\
                          _sectorIdMatrix, _bestNeighborMatrix, \
                          _eqCapitalC, _eqCapitalF,\
                          _eqReturnsC, _eqReturnsF):
        self.tauTimeline          = _tauTimeline
        self.capitalsCMatrix      = _capitalsCMatrix
        self.capitalsFMatrix      = _capitalsFMatrix
        self.totalCapitalCVector  = _totalCapitalCVector
        self.totalCapitalFVector  = _totalCapitalFVector
        self.avgCapitalCVector    = _avgCapitalCVector
        self.avgCapitalFVector    = _avgCapitalFVector
        self.rentCVector          = _rentCVector
        self.rentFVector          = _rentFVector
        self.wagesCVector         = _wagesCVector
        self.wagesFVector         = _wagesFVector
        self.productionCVector    = _productionCVector
        self.productionFVector    = _productionFVector
        self.occupNumberVectorC   = _occupNumberVectorC
        self.occupNumberVectorF   = _occupNumberVectorF
        self.maxConsumCVector     = _maxConsumCVector
        self.maxConsumFVector     = _maxConsumFVector
        self.savingsRatesMatrixC  = _savingsRatesMatrixC
        self.savingsRatesMatrixF  = _savingsRatesMatrixF
        self.avgSavingsVectorC    = _avgSavingsVectorC
        self.avgSavingsVectorF    = _avgSavingsVectorF
        self.incomesCMatrix       = _incomesCMatrix
        self.incomesFMatrix       = _incomesFMatrix
        self.incomesMatrix        = _incomesMatrix
        self.consumptionsMatrix   = _consumptionsMatrix
        self.sectorIdMatrix       = _sectorIdMatrix
        self.bestNeighborMatrix   = _bestNeighborMatrix   
        self.eqCapitalC           = _eqCapitalC
        self.eqCapitalF           = _eqCapitalF
        self.eqReturnsC           = _eqReturnsC
        self.eqReturnsF           = _eqReturnsF
        
    
        #self.plotSingleOverview() 
        #self.plotColorCodedCapitals('c')
        #self.plotColorCodedCapitals('f')
        #self.plotSavOverInc('c')
        #self.plotSavOverInc('f')
        #self.plotRentOverTotalCapital(self.rentCVector, self.totalCapitalCVector, r'returns $r^c$', r'tot. capital $K^c$')
        #self.plotRentOverTotalCapital(self.rentFVector, self.totalCapitalFVector, r'returns $r^f$', r'tot. capital $K^f$')
        #self.plotTotCapVsTotCap()
        #self.plotTotCapDiffereny()
        #self.plotRentAgainstTotalCapital(self.rentCVector, r'$r^c$', self.totalCapitalCVector, r'$K^c$')
        #self.plotRentAgainstTotalCapital(self.rentFVector, r'$r^f$', self.totalCapitalFVector, r'$K^f$')
        self.plotRentAgainstOccupNumber(self.eqReturnsC, r'return $r^c$', self.occupNumberVectorC, r'occup. number $N^c$',  r'$r^c$',  r'$N^c$')
        self.plotRentAgainstOccupNumber(self.eqReturnsF, r'return $r^f$', self.occupNumberVectorF, r'occup. number $N^f$',  r'$r^f$',  r'$N^f$')
        #self.plotSavings(self.savingsRatesMatrixC, self.avgSavingsVectorC, r'$s_i^c$', r'$\overline{s}_i^c$')
        #self.plotSavings(self.savingsRatesMatrixF, self.avgSavingsVectorF, r'$s_i^f$', r'$\overline{s}_i^f$')
        #self.plotOccupVsOccup()
        #self.plotCapitalEquilibrium('c')
        #self.plotCapitalEquilibrium('f')
        #self.plotRentVsRent()
        self.plot3D()
        #self.plotReturnVsReturn()
        
        
    def plot3D(self):
        ax = plt.axes(projection='3d')

        ax.plot3D(self.eqReturnsC, self.avgSavingsVectorC, self.occupNumberVectorC, 'gray')
        ax.set_xlim(0,0.08)
        ax.set_xlabel(r'return $r^c$', fontsize=par.fontsize)
        ax.set_ylim(0,1)
        ax.set_ylabel(r'avg. savings $\bar{s}_i^c$', fontsize=par.fontsize)
        ax.set_zlim(0,100)
        ax.set_zlabel(r'occup. # $N^c$', fontsize=par.fontsize)
        plt.tight_layout()
        plt.show()
        
        
    def plotSingleOverview(self):
       
        plt.plot( self.tauTimeline,  self.capitalsCMatrix,  linewidth=0.1, color='k')
        plt.plot( self.tauTimeline,  self.avgCapitalCVector, linewidth=1, color='r', label=r'$\overline{K}_i^c$')
        #plt.plot( self.tauTimeline, self.eqCapitalC, linewidth=1, color='b')
        plt.ylabel(r'capitals $K_i^c$', fontsize=par.fontsize)
        plt.legend(loc='upper right', prop={'size':par.fontsize-7})
        plt.yscale("symlog")
        plt.tick_params(labelsize=par.ticksize)
        plt.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.617, right=0.96, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()    
        
        plt.plot( self.tauTimeline,  self.capitalsFMatrix,  linewidth=0.1, color='k')
        plt.plot( self.tauTimeline,  self.avgCapitalFVector, linewidth=1, color='r', label=r'$\overline{K}_i^f$')
        #plt.plot( self.tauTimeline, self.eqCapitalC, linewidth=1, color='b')
        plt.ylabel(r'capitals $K_i^f$', fontsize=par.fontsize)
        plt.legend(loc='upper right', prop={'size':par.fontsize-7})
        plt.yscale("symlog")
        plt.tick_params(labelsize=par.ticksize)
        plt.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.617, right=0.96, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()    
   
   
        plt.plot( self.tauTimeline,  self.savingsRatesMatrixC, linewidth=0.4)
        plt.plot( self.tauTimeline,  self.avgSavingsVectorC, linewidth=1, color='k', label=r'$\overline{s}_i^c$')
        plt.ylabel(r'saving-rates $s_i^c$', fontsize=par.fontsize)
        plt.ylim([0,1])
        plt.legend(loc='upper right', prop={'size':par.fontsize-7})
        plt.tick_params(labelsize=par.ticksize)
        plt.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.617, right=0.96, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()
        
        
        plt.plot( self.tauTimeline,  self.savingsRatesMatrixF, linewidth=0.4)
        plt.plot( self.tauTimeline,  self.avgSavingsVectorF, linewidth=1, color='k', label=r'$\overline{s}_i^f$')
        plt.xlabel(r'$timesteps$', fontsize=par.fontsize)
        plt.ylabel(r'saving-rates $s_i^f$', fontsize=par.fontsize)
        plt.ylim([0,1])
        plt.legend(loc='upper right', prop={'size':par.fontsize-7})
        plt.tick_params(labelsize=par.ticksize)
        plt.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.617, right=0.96, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()
        
    
    
    def plotColorCodedCapitals(self, _sector):
        fig, ax1 = plt.subplots()
        cmap = ListedColormap(['g', 'r'])
        norm = BoundaryNorm([2,2], cmap.N)
        if _sector=='c': 
            capitalsMatrix = self.capitalsCMatrix[:,:50]
            capitalsLabel  = r'capitals $K_i^c$'
        else:   
            capitalsMatrix = self.capitalsFMatrix[:,:50]
            capitalsLabel  = r'capitals $K_i^f$'
        for i in range(0,49):            
            capitalTrajectory           =  capitalsMatrix[:,i].T
            colorCodingArray            =  self.sectorIdMatrix[:,i].T
            points                      = np.array([ self.tauTimeline, capitalTrajectory]).T.reshape(-1, 1, 2)
            segments                    = np.concatenate([points[:-1], points[1:]], axis=1)
            lc                          = LineCollection(segments, cmap=cmap, norm=norm)
            lc.set_array(colorCodingArray)
            lc.set_linewidth(1)
            ax1.add_collection(lc)
            
        ax1.tick_params(labelsize=par.ticksize)
        ax1.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
        ax1.set_xlim(par.plotStart, par.plotStop)  
        ax1.set_ylim(0, capitalsMatrix.max())
        ax1.set_yscale('symlog')
        ax1.set_ylabel(capitalsLabel, fontsize=par.fontsize)
        plt.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.617, right=0.96, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()
        
        
    def plotRentOverTotalCapital(self, _returnVector, _totalCapital, _rentLabel, _totalCapitalLabel):
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.plot(self.tauTimeline, _returnVector, color='blue', label=_rentLabel) 
        ax2.plot(self.tauTimeline, _totalCapital, color='orange', label=_totalCapitalLabel)      
        
        ax1.set_ylim(0.04,0.2)
        ax1.legend(loc='upper left', prop={'size':par.fontsize-7})
        ax1.tick_params(labelsize=par.ticksize)
        ax1.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        ax1.set_xlim(par.plotStart, par.plotStop)
        ax1.set_ylabel(_rentLabel, fontsize=par.fontsize)
        ax1.set_yscale('symlog')
        ax2.set_ylim(500,15000)
        ax2.set_ylabel(_totalCapitalLabel, fontsize=par.fontsize)
        ax2.set_yscale('symlog')
        ax2.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax2.tick_params(labelsize=par.ticksize)


        fig.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.617, right=0.929, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()           
        
        
    def plotSavings(self, _savingsRates, _avgSavings, _savingsLabel, _avgSavLabel):
        fig, ax1 = plt.subplots()
        ax1.plot( self.tauTimeline, _savingsRates, linewidth=0.4)    
        ax1.plot( self.tauTimeline,  _avgSavings, linewidth=1, color='k', label=_avgSavLabel)    
        ax1.set_ylabel(r'saving-rates '+_savingsLabel, fontsize=par.fontsize) 
        ax1.legend(loc='upper right', prop={'size':par.fontsize})
        ax1.set_ylim([0,1])
        ax1.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        ax1.set_xlim([par.plotStart, par.plotStop])
        ax1.tick_params(labelsize=par.ticksize)
        plt.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.617, right=0.96, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()
        
        
    def plotOccupVsOccup(self):
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.plot( self.tauTimeline, self.occupNumberVectorC, color='green', label=r'$N^c$')    
        ax1.set_ylabel(r'occup. number $N^c$', fontsize=par.fontsize) 
        ax1.legend(loc='upper left', prop={'size':par.fontsize-7})
        ax1.set_ylim([0,par.numOfAgents])
        ax2.plot( self.tauTimeline, self.occupNumberVectorF, color='brown', label=r'$N^f$')
        ax2.set_ylabel(r'occup. number $N^f$', fontsize=par.fontsize) 
        ax2.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax2.set_ylim([0,par.numOfAgents])
        ax1.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        ax1.set_xlim([par.plotStart, par.plotStop])
        ax1.tick_params(labelsize=par.ticksize)
        ax2.tick_params(labelsize=par.ticksize)
        plt.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.617, right=0.929, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()
    
    def plotReturnVsReturn(self):
        fig, (ax1) = plt.subplots(1, 1)

        ax1.plot(self.rentCVector, self.rentFVector, linewidth=0.3, color='black')
        ax1.set_ylabel(r'avg. saving-rate $\overline{s}_i^f$', fontsize=par.fontsize)
        ax1.set_xlabel(r'avg. saving-rate $\overline{s}_i^c$', fontsize=par.fontsize)
        ax1.set_xlim(0, 0.08)
        ax1.set_ylim(0, 0.08)
          
        fig.tight_layout()
        plt.subplots_adjust(left=0.06, bottom=0.1, right=0.932, top=0.939, wspace=0.2, hspace=0.2)
        plt.show()         
        
    def plotRentAgainstTotalCapital(self, _rent, _rentLabel, _totalCapital, _capitalLabel):
        fig, ax1 = plt.subplots()
        ax2=ax1.twinx()
        ax1.plot(self.tauTimeline, _rent, color='blue', label=_rentLabel) 
        ax1.set_ylim(0.02,0.08)
        ax1.set_ylabel(_rentLabel, fontsize=par.fontsize) 
        ax1.legend(loc='upper left', prop={'size':par.fontsize-7})
        ax1.tick_params(axis='y', labelcolor='tab:blue', labelsize=par.ticksize)
        ax1.tick_params(axis='x', labelsize=par.ticksize)
        ax1.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        ax1.set_xlim([par.plotStart, par.plotStop])
        ax2.plot(self.tauTimeline, _totalCapital, color='orange', label=_capitalLabel)  
        ax2.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax2.set_ylabel(_capitalLabel, fontsize=par.fontsize) 
        ax2.tick_params(axis='y', labelcolor='tab:orange', labelsize=par.ticksize)
        plt.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.617, right=0.929, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()
        
    
    def plotRentAgainstOccupNumber(self, _rent, _rentLabel, _occupNumber, _occupNumberLabel, _shortRentL, _shortOccupL):  
        fig, ax1 = plt.subplots()
        ax2=ax1.twinx()        
        
        
        ax1.plot(self.tauTimeline, _rent, color='blue', label=_shortRentL) 
        #ax1.set_ylim(0.02, 0.09)
        ax1.set_ylabel(_rentLabel, fontsize=par.fontsize) 
        ax1.legend(loc='upper left', prop={'size':par.fontsize-7})
        ax1.set_xlabel(r'$timesteps$', rotation=0, fontsize=par.fontsize)
        ax1.set_xlim(par.plotStart, par.plotStop)
        ax1.tick_params(axis='y', labelcolor='tab:blue', labelsize=par.ticksize)
        ax1.tick_params(axis='x',  labelsize=par.ticksize)

        ax2.plot( self.tauTimeline, _occupNumber, color='brown', label=_shortOccupL)
        ax2.set_ylim([0, par.numOfAgents+2])
        ax2.set_ylabel(_occupNumberLabel, fontsize=par.fontsize)   
        ax2.tick_params(axis='y', labelcolor='tab:brown', labelsize=par.ticksize)
        ax2.legend(loc='upper right', prop={'size':par.fontsize-7})
        
        plt.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.617, right=0.929, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()
        
       
    def plotCapitalEquilibrium(self, _sector):
        fig, ax1 = plt.subplots()
        
        if _sector=='c': 
            capitalsMatrix = self.capitalsCMatrix
            avgCapital     = self.avgCapitalCVector
            eqCapital      = self.eqCapitalC
            capitalsLabel  = r'capitals $K_i^c$'
            avgCapitalLabel = r'$\overline{K}_i^c$'
            eqCapitalLabel = r'$\overline{K}_i^{*c}$'
        else:   
            capitalsMatrix = self.capitalsFMatrix
            avgCapital     = self.avgCapitalFVector
            eqCapital      = self.eqCapitalF
            capitalsLabel  = r'capitals $K_i^f$'
            avgCapitalLabel = r'$\overline{K}_i^f$'
            eqCapitalLabel = r'$\overline{K}_i^{*f}$'
            
        ax1.plot( self.tauTimeline, capitalsMatrix,  linewidth=0.1, color='k')
        ax1.plot( self.tauTimeline, avgCapital, linewidth=1, color='r', label=avgCapitalLabel)
        ax1.plot( self.tauTimeline, eqCapital, linewidth=1, color='b', label=eqCapitalLabel)
        ax1.set_ylabel(capitalsLabel, fontsize=par.fontsize)
        ax1.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax1.set_xlim(par.plotStart, par.plotStop)
        ax1.set_yscale("symlog")
        ax1.tick_params(labelsize=par.ticksize)
        
        fig.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.617, right=0.929, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()          


    def plotRentVsRent(self):
         
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
            
        ax1.plot( self.tauTimeline,  self.rentCVector, linewidth=1.5, color='g', label=r'$r^c$')
        ax1.set_ylabel(r'return $r^c$', fontsize=par.fontsize)
        ax1.set_ylim(0.02, 0.09)
        ax1.legend(loc='upper left', prop={'size':par.fontsize-7})
        ax1.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        ax1.set_xlim(par.plotStart, par.plotStop)
        ax1.tick_params(labelsize=par.ticksize)
        
        ax2.plot( self.tauTimeline,  self.rentFVector, linewidth=1.5, color='brown', label=r'$r^f$')
        ax2.set_ylabel(r'return $r^f$', fontsize=par.fontsize)
        ax2.set_ylim(0.02, 0.09)
        ax2.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax2.tick_params(labelsize=par.ticksize)
        
  
        fig.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.617, right=0.929, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()  
    
    
    def plotTotCapVsTotCap(self):
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
            
        ax1.plot( self.tauTimeline,  self.totalCapitalCVector, linewidth=1.5, color='g', label=r'$K^c$')
        ax1.set_ylabel(r'tot. capital $K^c$', fontsize=par.fontsize)
        ax1.set_ylim(0, 15000)
        ax1.legend(loc='upper left', prop={'size':par.fontsize})
        ax1.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        ax1.set_xlim(par.plotStart, par.plotStop)
        ax1.tick_params(labelsize=par.ticksize)
        
        ax2.plot( self.tauTimeline,  self.totalCapitalFVector, linewidth=1.5, color='brown', label=r'$K^f$')
        ax2.set_ylabel(r'tot. capital $K^f$', fontsize=par.fontsize)
        ax2.set_ylim(0, 15000)
        ax2.legend(loc='upper right', prop={'size':par.fontsize})
        ax2.tick_params(labelsize=par.ticksize)
        
  
        fig.tight_layout()
        plt.subplots_adjust(left=0.074, bottom=0.617, right=0.927 , top=0.947, wspace=0.21, hspace=0.14)
        plt.show()              
        
        
    def plotTotCapDiffereny(self):
        fig, ax1 = plt.subplots()
            
        ax1.plot( self.tauTimeline,  self.totalCapitalCVector-self.totalCapitalFVector, linewidth=1.5, color='g', label=r'$K^c$')
        ax1.set_ylabel(r'tot. capital difference $K^c-K^f$', fontsize=par.fontsize)
        #ax1.set_ylim(0, 15000)
        ax1.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        ax1.set_xlim(par.plotStart, par.plotStop)
        ax1.tick_params(labelsize=par.ticksize)
        
  
        fig.tight_layout()
        plt.subplots_adjust(left=0.074, bottom=0.617, right=0.927 , top=0.947, wspace=0.21, hspace=0.14)
        plt.show()                  
        
    def plotSavOverInc(self, _sector):
        if _sector=='c':
            savingsRatesMatrix = self.savingsRatesMatrixC
            incomesMatrix      = self.incomesCMatrix
            markerColor    = 'r'
            sectorChange   = -1
            neighborSector = 1
            crossLabel     = 'inflow from sector f'
            siLabel        = r'savings-rates $s_i^c$'
            IiLabel        = r'incomes $I_i^c$'          
        else: 
            incomesMatrix      = self.incomesFMatrix
            savingsRatesMatrix = self.savingsRatesMatrixF
            markerColor    = 'g'
            crossLabel     = 'inflow from sector c'
            sectorChange   = 1  
            neighborSector = 2
            siLabel        = r'saving-rates $s_i^f$'
            IiLabel        = r'incomes $I_i^f$'
                
        for i in range(0,par.numOfAgents-1):
            sectorChangeId                     = self.getSectorChangeId(i, sectorChange)
            bestNeighborId                     = self.getBestNeighborsColorPlotVariables(i, neighborSector)
            savingsTrajectory, markerSavings   = self.getSavingsColorPlotVariables(i, savingsRatesMatrix, sectorChangeId)
            markerSectorChange                 = self.tauTimeline[sectorChangeId]
            markerBestNeighbor                 = self.tauTimeline[bestNeighborId]
            markerBestSavings                  = savingsTrajectory[bestNeighborId]
      
            line1 = plt.plot( self.tauTimeline, savingsTrajectory, linewidth=0.2, color='k', alpha=0.3)
            plt.scatter(markerSectorChange, markerSavings , marker = 'x', c=markerColor, alpha=1, s=25, label=crossLabel)
            plt.scatter(markerBestNeighbor, markerBestSavings , marker = 'o',   c='b', alpha=0.5, s=8, label='best consumer')
        
       # plt.legend(loc='upper right', prop={'size':par.fontsize}) 
       # plt.title(r'mean update time $\tau=$'+str(par.tau), fontsize=par.fontsize)
        plt.ylabel(siLabel, fontsize=par.fontsize) 
        plt.xlim(par.plotStart, par.plotStop)
        plt.xlabel(r'timesteps', fontsize=par.fontsize)
        plt.tick_params(axis='y', labelsize=par.ticksize)
        plt.tick_params(axis='x', labelsize=par.ticksize)
        #plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)      
        plt.tight_layout()
        plt.subplots_adjust(left=0.218, bottom=0.617, right=0.639, top=0.947, wspace=0.21, hspace=0.14)
        plt.show()  
           
        for i in range(0,par.numOfAgents-1):
            sectorChangeId                     = self.getSectorChangeId(i, sectorChange)
            bestNeighborId                     = self.getBestNeighborsColorPlotVariables(i, neighborSector)
            incomesTrajectory, markerIncomes   = self.getIncomesColorPlotVariables(i, incomesMatrix, sectorChangeId) 
            markerSectorChange                 = self.tauTimeline[sectorChangeId]
            markerBestNeighbor                 = self.tauTimeline[bestNeighborId]
            markerBestIncomes                  = incomesTrajectory[bestNeighborId] 
           
            line2  = plt.plot( self.tauTimeline, incomesTrajectory, linewidth=0.2, color='k')
            plt.scatter(markerSectorChange, markerIncomes , marker = 'x', c=markerColor, alpha=1, s=25, label=crossLabel)
            plt.scatter(markerBestNeighbor, markerBestIncomes , marker = 'o',   c='b', alpha=0.5, s=8, label='best consumer')
         
        #plt.legend(loc='upper right', prop={'size':par.fontsize}) 
        plt.ylabel(IiLabel, fontsize=par.fontsize)
        plt.xlabel('timesteps', fontsize=par.fontsize)
        plt.xlim(par.plotStart, par.plotStop)
        plt.tick_params(axis='y', labelsize=par.ticksize) 
        plt.tick_params(axis='x',  labelsize=par.ticksize)
        plt.tight_layout()
        plt.subplots_adjust(left=0.199, bottom=0.166, right=0.598, top=0.85, wspace=0.21, hspace=0.14)
        plt.show()    
        
        
        
    def getSavingsColorPlotVariables(self, _i, _savingsRatesMatrix, _sectorChangeId):
        savingsTrajectory            =  _savingsRatesMatrix[:,_i].T 
        markerSavings                = savingsTrajectory[_sectorChangeId]
        return savingsTrajectory, markerSavings


    def getIncomesColorPlotVariables(self, _i, _incomesMatrix, _sectorChangeId):
        incomesTrajectory            = _incomesMatrix[:,_i].T 
        markerIncomes                = incomesTrajectory[_sectorChangeId]
        return incomesTrajectory, markerIncomes
        
     
    def getBestNeighborsColorPlotVariables(self, _i, _neighborSector):
         bestNeighborTrajectory       =  self.bestNeighborMatrix[:,_i].T
         bestNeighborId               =  np.where(bestNeighborTrajectory == _neighborSector)[0]
         markerPoints                 =  self.tauTimeline[bestNeighborId]
         return bestNeighborId
         
     
    def getSectorChangeId(self, _i, _sectorChange):
        sectorChangeSignals          = np.zeros(len( self.tauTimeline))
        sectorChangeSignals[1:]      = np.diff( self.sectorIdMatrix[:,_i].T)
        sectorChangeId               = np.where(sectorChangeSignals == _sectorChange)[0]
        return sectorChangeId             
        


        
        

 
                   

