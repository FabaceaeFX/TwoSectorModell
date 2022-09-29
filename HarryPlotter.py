import ParametersRCK     as par
import matplotlib        as mp
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm, LogNorm
import numpy             as np
import string


        

class HarryPlotter:


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
                          _eqCapitalC, _eqCapitalF):
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
        self.eqCapitalC          = _eqCapitalC
        self.eqCapitalF          = _eqCapitalF
                                          
        #self.plotCapitals('c')
        #self.plotCapitals('f')
        self.plotOverview()
        #self.plotAvgSavOverReturn()
        #self.plotAvgSavOverOccupNumber()
        #self.plotOccupNumberOverReturn()
        #self.plotAvgSavOverSav()
        #self.plotMacroVariables()
        #self.plotSavingsRates('c')
        #self.plotSavingsRates('f')
        #self.plotIncomes('c')
        #self.plotIncomes('f')
        #self.plotIncOverInc()
        self.plotSavOverSav()
        #self.plotSavOverInc('c')
        #self.plotSavOverInc('f') 
        #self.plotCapitalEquilibrium()                                
        
        #self.plotCapitalsOverSiOverRent('c')
        #self.plotCapitalsOverSiOverRent('f')
   
   
   
   
   
   
   
    def plotOverview(self):
        fig, (ax1,ax2,ax3,ax4) = plt.subplots(4,1, sharex=True)
       
        ax1.plot( self.tauTimeline,  self.capitalsCMatrix,  linewidth=0.1, color='k')
        ax1.plot( self.tauTimeline,  self.avgCapitalCVector, linewidth=1, color='r', label=r'$\overline{K}_i^c$')
        #ax1.plot( self.tauTimeline, self.eqCapitalC, linewidth=1, color='b')
        ax1.set_ylabel(r'capitals $K_i^c$', fontsize=par.fontsize)
        ax1.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax1.set_yscale("symlog")
        
        ax2.plot( self.tauTimeline,  self.capitalsFMatrix, linewidth=0.1, color='k')
        ax2.plot( self.tauTimeline,  self.avgCapitalFVector, linewidth=1, color='r', label=r'$\overline{K}_i^f$')
        #ax2.plot( self.tauTimeline, self.eqCapitalF, linewidth=1, color='b')
        ax2.set_ylabel(r'capitals $K_i^f$', fontsize=par.fontsize)
        ax2.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax2.set_yscale('symlog')
             
        ax3.plot( self.tauTimeline,  self.savingsRatesMatrixC, linewidth=0.4)
        ax3.plot( self.tauTimeline,  self.avgSavingsVectorC, linewidth=1, color='k', label=r'$\overline{s}_i^c$')
        ax3.set_ylabel(r'saving-rates $s_i^c$', fontsize=par.fontsize)
        ax3.set_ylim([0,1])
        ax3.legend(loc='upper right', prop={'size':par.fontsize-7})
        
        ax4.plot( self.tauTimeline,  self.savingsRatesMatrixF, linewidth=0.4)
        ax4.plot( self.tauTimeline,  self.avgSavingsVectorF, linewidth=1, color='k', label=r'$\overline{s}_i^f$')
        ax4.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        ax4.set_ylabel(r'saving-rates $s_i^f$', fontsize=par.fontsize)
        ax4.set_ylim([0,1])
        ax4.legend(loc='upper right', prop={'size':par.fontsize-7})
        
        ax1.tick_params(labelsize=par.ticksize)
        ax2.tick_params(labelsize=par.ticksize)
        ax3.tick_params(labelsize=par.ticksize)
        ax4.tick_params(labelsize=par.ticksize)
  
        fig.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.1, right=0.96, top=0.963, wspace=0.21, hspace=0.14)
        plt.show()    


    def plotCapitalsOverSiOverRent(self, _sector):
        fig, (ax1,ax2, ax3) = plt.subplots(3, 1, sharex=True)
        ax4 = ax3.twinx()
        cmap = ListedColormap(['g', 'r'])
        norm = BoundaryNorm([2,2], cmap.N)
        if _sector=='c': 
            ax1.set_ylabel(r'capitals $K_i^c$', fontsize=par.fontsize)  
            ax2.set_ylabel(r'saving-rates $s_i^c$', fontsize=par.fontsize) 
            ax3.set_ylabel(r'return $r_c$', fontsize=par.fontsize)
            ax4.set_ylabel(r'tot. capital $K_c$', fontsize=par.fontsize)
            capitalsMatrix = self.capitalsCMatrix
            savingsRates   = self.savingsRatesMatrixC
            avgSavings     = self.avgSavingsVectorC
            rent           = self.rentCVector
            totalCapital   = self.totalCapitalCVector
            avgSavLabel    = r'$\overline{s}_i^c$'
            returnLabel    = r'$r^c$'
            capitalLabel   = r'$K^f$'
        else:   
            ax1.set_ylabel(r'capitals $K_i^f$', fontsize=par.fontsize)
            ax2.set_ylabel(r'saving-rates $s_i^f$', fontsize=par.fontsize)
            ax3.set_ylabel(r'return $r_f$', fontsize=par.fontsize)
            ax4.set_ylabel(r'tot. capital $K_f$', fontsize=par.fontsize)
            capitalsMatrix = self.capitalsFMatrix
            savingsRates   = self.savingsRatesMatrixF
            avgSavings     = self.avgSavingsVectorF
            rent           = self.rentFVector
            totalCapital   = self.totalCapitalFVector
            avgSavLabel    = r'$\overline{s}_i^f$'
            returnLabel    = r'$r^f$'
            capitalLabel   = r'$K^f$'
        for i in range(0,par.numOfAgents-1):            
            capitalTrajectory           =  capitalsMatrix[:,i].T
            colorCodingArray            =  self.sectorIdMatrix[:,i].T
            points                      = np.array([ self.tauTimeline, capitalTrajectory]).T.reshape(-1, 1, 2)
            segments                    = np.concatenate([points[:-1], points[1:]], axis=1)
            lc                          = LineCollection(segments, cmap=cmap, norm=norm)
            lc.set_array(colorCodingArray)
            lc.set_linewidth(1)

           
            ax1.add_collection(lc)
    
        
           
        ax2.plot( self.tauTimeline,  savingsRates, linewidth=0.4)
        ax2.plot( self.tauTimeline,  avgSavings, linewidth=1, color='k', label=avgSavLabel)
        ax3.plot(self.tauTimeline, rent, color='blue', label=returnLabel) 
        ax4.plot(self.tauTimeline, totalCapital, color='orange', label=capitalLabel)       

        ax1.tick_params(labelsize=par.ticksize)
        ax1.set_xlim(par.plotStart, par.plotStop)  
        ax1.set_ylim(0, capitalsMatrix.max())
        ax1.set_yscale('symlog')   

        ax2.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax2.set_ylim([0,1])
        ax2.tick_params(labelsize=par.ticksize)
        ax3.set_ylim(0.02,0.08)
        ax3.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax3.tick_params(labelsize=par.ticksize)
        ax3.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        #ax4.set_ylim(0,100)
        ax4.legend(loc='upper left', prop={'size':par.fontsize-7})
        ax4.tick_params(labelsize=par.ticksize)
        
        fig.tight_layout()
        plt.subplots_adjust(left=0.06, bottom=0.083, right=0.935, top=0.962, wspace=0.2, hspace=0.16)
        plt.show()
        
            
    def plotSavOverSav(self): 
        fig, (ax1,ax2, ax3) = plt.subplots(3, 1, sharex=True)
        ax4 = ax3.twinx()
        
        for i in range(0,par.numOfAgents-1):
            sectorChangeIdC                    = self.getSectorChangeId(i, -1)
            bestNeighborIdC                    = self.getBestNeighborsColorPlotVariables(i, 1)
            savingsTrajectoryC, markerSavingsC = self.getSavingsColorPlotVariables(i, self.savingsRatesMatrixC, sectorChangeIdC)
           
            sectorChangeIdF                    = self.getSectorChangeId(i, 1)
            bestNeighborIdF                    = self.getBestNeighborsColorPlotVariables(i, 2)
            savingsTrajectoryF, markerSavingsF = self.getSavingsColorPlotVariables(i, self.savingsRatesMatrixF, sectorChangeIdF)
            
            markerSectorChangeC                 = self.tauTimeline[sectorChangeIdC]
            markerBestNeighborC                 = self.tauTimeline[bestNeighborIdC]
            
            markerSectorChangeF                 = self.tauTimeline[sectorChangeIdF]
            markerBestNeighborF                 = self.tauTimeline[bestNeighborIdF]
            
            markerBestSavingsC                  = savingsTrajectoryC[bestNeighborIdC]
            markerBestSavingsF                  = savingsTrajectoryF[bestNeighborIdF]
            
            ax1.plot( self.tauTimeline, savingsTrajectoryC, linewidth=0.2, color='k')
            ax1.scatter(markerSectorChangeC, markerSavingsC, marker = 'x', c='r', alpha=1)
            ax1.scatter(markerBestNeighborC, markerBestSavingsC , marker = 'o',   c='b', alpha=0.5)
           
            ax2.plot( self.tauTimeline, savingsTrajectoryF, linewidth=0.2, color='k')
            ax2.scatter(markerSectorChangeF, markerSavingsF , marker = 'x', c='g', alpha=1)
            ax2.scatter(markerBestNeighborF, markerBestSavingsF , marker = 'o',   c='b', alpha=0.5)
        
        ax3.plot( self.tauTimeline,  self.occupNumberVectorC, linewidth=1, color='g', label=r'$N^c$')
        ax3.set_ylabel(r'occup. number $N^c$', fontsize=par.fontsize)
        ax3.set_ylim([0,100])
        ax3.legend(loc='upper left', prop={'size':par.fontsize-7})
        ax3.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        
        ax4.plot( self.tauTimeline,  self.occupNumberVectorF, linewidth=1, color='brown', label=r'$N^f$')
        ax4.set_ylabel(r'occup. number $N^f$', fontsize=par.fontsize)
        ax4.set_ylim([0,100])
        ax4.legend(loc='upper right', prop={'size':par.fontsize-7})    
                        
        ax1.set_ylabel(r'saving-rates $s_i^c$', fontsize=par.fontsize)
        ax2.set_ylabel(r'saving-rates $s_i^f$', fontsize=par.fontsize)

        ax1.set_title(r'$\tau=$'+str(par.tau), fontsize=par.fontsize)
        ax1.tick_params(labelsize=par.ticksize)
        ax2.tick_params(labelsize=par.ticksize)
        ax3.tick_params(labelsize=par.ticksize)
        ax4.tick_params(labelsize=par.ticksize)
         
        fig.tight_layout()
        plt.subplots_adjust(left=0.085, bottom=0.09, right=0.916, top=0.968, wspace=0.2, hspace=0.109)
        plt.show()                    
                        
        
    def plotSavOverInc(self, _sector):
        if _sector=='c':
            savingsRatesMatrix = self.savingsRatesMatrixC
            incomesMatrix      = self.incomesCMatrix
            rentVector         = self.rentCVector
            occupNumberVector  = self.occupNumberVectorC
            markerColor    = 'r'
            sectorChange   = -1
            neighborSector = 1
            siLabel        = r'savings-rates $s_i^c$'
            IiLabel        = r'incomes $I_i^c$'
            NLabel         = r'occup. number $N_c$'
            NShort         = r'$N_c$'
            rLabel         = r'return $r_c$'  
            rShort         = r'$r_c$'           
        else: 
            incomesMatrix      = self.incomesFMatrix
            savingsRatesMatrix = self.savingsRatesMatrixF
            rentVector         = self.rentFVector
            occupNumberVector  = self.occupNumberVectorF
            markerColor    = 'g'
            sectorChange   = 1  
            neighborSector = 2
            siLabel        = r'saving-rates$s_i^f$'
            IiLabel        = r'incomes $I_i^f$'
            NLabel         = r'occup. Number $N_f$'
            NShort         = r'$N_f$'
            rLabel         = r'return $r_f$'
            rShort         = r'$r_f$'
                
        fig, (ax1,ax2, ax3) = plt.subplots(3, 1, sharex=True)
        ax4 = ax3.twinx()
    
        for i in range(0,par.numOfAgents-1):
            sectorChangeId                     = self.getSectorChangeId(i, sectorChange)
            bestNeighborId                     = self.getBestNeighborsColorPlotVariables(i, neighborSector)
            savingsTrajectory, markerSavings   = self.getSavingsColorPlotVariables(i, savingsRatesMatrix, sectorChangeId)
            incomesTrajectory, markerIncomes   = self.getIncomesColorPlotVariables(i, incomesMatrix, sectorChangeId) 
            markerSectorChange                 = self.tauTimeline[sectorChangeId]
            markerBestNeighbor                 = self.tauTimeline[bestNeighborId]
            markerBestSavings                  = savingsTrajectory[bestNeighborId]
            markerBestIncomes                  = incomesTrajectory[bestNeighborId]
      
            line1 = ax1.plot( self.tauTimeline, savingsTrajectory, linewidth=0.2, color='k', alpha=0.3)
            ax1.scatter(markerSectorChange, markerSavings , marker = 'x', c=markerColor, alpha=1, s=25)
            ax1.scatter(markerBestNeighbor, markerBestSavings , marker = 'o',   c='b', alpha=0.5, s=8)
           
            line2  = ax2.plot( self.tauTimeline, incomesTrajectory, linewidth=0.2, color='k')
            ax2.scatter(markerSectorChange, markerIncomes , marker = 'x', c=markerColor, alpha=1, s=25)
            ax2.scatter(markerBestNeighbor, markerBestIncomes , marker = 'o',   c='b', alpha=0.5, s=8)
                        
        ax1.set_ylabel(siLabel, fontsize=par.fontsize)
        ax2.set_ylabel(IiLabel, fontsize=par.fontsize)
        ax3.set_ylabel(rLabel, fontsize=par.fontsize) 
        ax4.set_ylabel(NLabel, fontsize=par.fontsize)   
        
        ax1.tick_params(axis='y', labelsize=par.ticksize)        
        ax2.tick_params(axis='y', labelsize=par.ticksize) 
        ax3.tick_params(axis='y', labelcolor='tab:blue', labelsize=par.ticksize)
        ax4.tick_params(axis='y', labelcolor='tab:brown', labelsize=par.ticksize) 
                   
        ax3.plot(self.tauTimeline, rentVector, color='blue', label=rShort) 
        ax3.set_ylim(0.02, 0.09)
        ax3.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax3.set_xlabel(r'$timesteps$', rotation=0, fontsize=par.fontsize)
        ax3.tick_params(axis='x',  labelsize=par.ticksize)

        ax4.plot( self.tauTimeline, occupNumberVector, color='brown', label=NShort)
        ax4.set_ylim([0, par.numOfAgents+2])
        ax4.legend(loc='upper right', prop={'size':par.fontsize-7})

        fig.tight_layout()
        plt.subplots_adjust(left=0.06, bottom=0.083, right=0.935, top=0.962, wspace=0.2, hspace=0.16)
        plt.show()
        
                 
    def plotIncOverInc(self):
        fig, (ax1,ax2) = plt.subplots(2, 1, sharex=True)
        for i in range(0,par.numOfAgents-1):
            sectorChangeIdC                    = self.getSectorChangeId(i, -1)
            bestNeighborIdC                    = self.getBestNeighborsColorPlotVariables(i, 1)
            incomesTrajectoryC, markerIncomesC = self.getIncomesColorPlotVariables(i, self.incomesCMatrix, sectorChangeIdC)
           
            sectorChangeIdF                    = self.getSectorChangeId(i, 1)
            bestNeighborIdF                    = self.getBestNeighborsColorPlotVariables(i, 2)
            incomesTrajectoryF, markerIncomesF = self.getIncomesColorPlotVariables(i, self.incomesFMatrix, sectorChangeIdF)
            
            markerSectorChangeC                 = self.tauTimeline[sectorChangeIdC]
            markerBestNeighborC                 = self.tauTimeline[bestNeighborIdC]
            
            markerSectorChangeF                 = self.tauTimeline[sectorChangeIdF]
            markerBestNeighborF                 = self.tauTimeline[bestNeighborIdF]
            
            markerBestIncomesC                  = incomesTrajectoryC[bestNeighborIdC]
            markerBestIncomesF                  = incomesTrajectoryF[bestNeighborIdF]
            
            ax1.plot( self.tauTimeline, incomesTrajectoryC, linewidth=0.2, color='k')
            ax1.scatter(markerSectorChangeC, markerIncomesC, marker = 'o', c='r', alpha=1)
            ax1.scatter(markerBestNeighborC, markerBestIncomesC , marker = 'o',   c='b', alpha=1)
           
            line2  = ax2.plot( self.tauTimeline, incomesTrajectoryF, linewidth=0.2, color='k')
            ax2.scatter(markerSectorChangeF, markerIncomesF , marker = 'o', c='g', alpha=1)
            ax2.scatter(markerBestNeighborF, markerBestIncomesF , marker = 'o',   c='b', alpha=1)
            
            
        ax1.set_ylabel(r'incomes $I_i^c$', fontsize=par.fontsize)
        ax2.set_ylabel(r'incomes $I_i^f$', fontsize=par.fontsize)
        ax2.set_xlabel(r'$timesteps$', rotation=0, fontsize=par.fontsize) 
          
        ax1.tick_params(labelsize=par.ticksize)
        ax2.tick_params(labelsize=par.ticksize)
        fig.tight_layout()
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.963, wspace=0.21, hspace=0.14)
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
      
      
    def plotHeatMap(self, _lastSavingsMatrix, _bifurcParamArray):
        xmin, xmax, ymin, ymax = ( _bifurcParamArray[0],  _bifurcParamArray[-1], 0, 1)
        binsEdges = np.linspace(0,1,par.numOfBins+1)
        histogrammMatrix = np.zeros((len( _bifurcParamArray), par.numOfBins))
        for index in range(0, len( _bifurcParamArray)):
            histogrammArray            = np.histogram(_lastSavingsMatrix[index,:], bins=binsEdges)[0]
            histogrammMatrix[index, :] = np.flip(histogrammArray)
        histogrammMatrix = np.log(histogrammMatrix+1)
        imshow_kwargs = {
            'vmin': 0,
            'vmax':histogrammMatrix.max(),
            'cmap': 'inferno',
            'extent': (xmin, xmax, ymin, ymax),
        }
        current_cmap = mp.cm.get_cmap()
        current_cmap.set_bad(color='black')
        fig, ax = plt.subplots()
        img = ax.imshow(np.transpose(histogrammMatrix), **imshow_kwargs, aspect='auto')
        ticks = np.linspace(xmin, xmax, 11)
       # ax.set_xticks(np.arange(len(ticks)), labels=ticks)
        fig.colorbar(img)

        plt.show()
        
        
    def plotMultiHeatMapBis(self, _lastSavingsMatrixC, _lastSavingsMatrixF, _avgOccupNumberC, _avgOccupNumberF, _varianzOccupC, _varianzOccupF, _bifurcParamArray):
        xmin, xmax, ymin, ymax = ( _bifurcParamArray[0],  _bifurcParamArray[-1], 0, 1)
        binsEdges = np.linspace(0,1,par.numOfBins+1)
        histogrammMatrixC = np.zeros((len( _bifurcParamArray), par.numOfBins))
        histogrammMatrixF = np.zeros((len( _bifurcParamArray), par.numOfBins))
        for index in range(0, len( _bifurcParamArray)):
            histogrammArrayC            = np.histogram(_lastSavingsMatrixC[index,:], bins=binsEdges)[0]
            histogrammArrayF            = np.histogram(_lastSavingsMatrixF[index,:], bins=binsEdges)[0]
            histogrammMatrixC[index, :] = np.flip(histogrammArrayC)
            histogrammMatrixF[index, :] = np.flip(histogrammArrayF)
        histogrammMatrixC = np.log(histogrammMatrixC+1)
        histogrammMatrixF = np.log(histogrammMatrixF+1)
        imshow_kwargs = {
            'vmin': 0,
            'vmax':5,
            'cmap': 'inferno',
            'extent': (xmin, xmax, ymin, ymax),
        }
        current_cmap = mp.cm.get_cmap()
        current_cmap.set_bad(color='black')
        
        fig = plt.figure()
        gs = fig.add_gridspec(3, 1, height_ratios=(7, 7, 3))
        (ax1, ax2, ax3) = gs.subplots(sharex='col')
        ax4 = ax3.twinx()
        
        img1 = ax1.imshow(np.transpose(histogrammMatrixC), **imshow_kwargs, aspect='auto')
        ax1.set_ylabel(r'saving-rates $s_i^c$', fontsize=par.fontsize)
        ax1.set_title(r'$\gamma=$'+str(par.subvention), fontsize=par.fontsize)
        
        img2 = ax2.imshow(np.transpose(histogrammMatrixF), **imshow_kwargs, aspect='auto')
        ax2.set_ylabel(r'saving-rates $s_i^f$', fontsize=par.fontsize)
        
        ax3.plot(_bifurcParamArray, _avgOccupNumberC, color="g")
        ax3.errorbar(_bifurcParamArray, _avgOccupNumberC, yerr=_varianzOccupC, color="g", capsize=3)
        ax3.set_ylabel(r'$\overline{N}^c$', fontsize=par.fontsize)
        ax3.set_ylim([0, par.numOfAgents]) 
        ax3.set_xlabel(r'$\tau$', fontsize=par.fontsize)
      #  ax4.set_xlim([0.9, 1.3])
                
        ax4.plot(_bifurcParamArray, _avgOccupNumberF, color="brown")
        ax4.errorbar(_bifurcParamArray, _avgOccupNumberF, yerr= _varianzOccupF,  color="brown", capsize=3)
        ax4.set_ylabel(r'$\overline{N}^f$', fontsize=par.fontsize)
        ax4.set_ylim([0, par.numOfAgents])
        
        ax1.tick_params(labelsize=par.ticksize)
        ax2.tick_params(labelsize=par.ticksize)
        ax3.tick_params(labelsize=par.ticksize)
        ax4.tick_params(labelsize=par.ticksize)
        
        fig.subplots_adjust(right=0.8)
        cbar_ax = fig.add_axes([0.85, 0.14, 0.05, 0.7])
        cbar = fig.colorbar(img2, cax=cbar_ax, ticks=[0,1,2,3,4,5])
        cbar.set_label('density', fontsize=par.fontsize)
        cbar.ax.set_yticklabels(['0','1','2','3','4','5'], size=par.ticksize)

        fig.tight_layout()
        plt.subplots_adjust(left=0.062, bottom=0.081, right=0.28, top=0.959, wspace=0.21, hspace=0.14)
        plt.show()
      
     
    def plotMultiHeatMap(self, _lastSavingsMatrixC, _lastSavingsMatrixF, _avgOccupNumberC, _avgOccupNumberF, _varianzOccupC, _varianzOccupF, _bifurcParamArray):
        xmin, xmax, ymin, ymax = ( _bifurcParamArray[0],  _bifurcParamArray[-1], 0, 1)
        binsEdges = np.linspace(0,1,par.numOfBins+1)
        histogrammMatrixC = np.zeros((len( _bifurcParamArray), par.numOfBins))
        histogrammMatrixF = np.zeros((len( _bifurcParamArray), par.numOfBins))
        for index in range(0, len( _bifurcParamArray)):
            histogrammArrayC            = np.histogram(_lastSavingsMatrixC[index,:], bins=binsEdges)[0]
            histogrammArrayF            = np.histogram(_lastSavingsMatrixF[index,:], bins=binsEdges)[0]
            histogrammMatrixC[index, :] = np.flip(histogrammArrayC)
            histogrammMatrixF[index, :] = np.flip(histogrammArrayF)
        histogrammMatrixC = np.log(histogrammMatrixC+1)
        histogrammMatrixF = np.log(histogrammMatrixF+1)
        imshow_kwargs = {
            'vmin': 0,
            'vmax':5,
            'cmap': 'inferno',
            'extent': (xmin, xmax, ymin, ymax),
        }
        current_cmap = mp.cm.get_cmap()
        current_cmap.set_bad(color='black')
        
        fig, (ax1,ax2) = plt.subplots(1, 2)
        
        img1 = ax1.imshow(np.transpose(histogrammMatrixC), **imshow_kwargs, aspect='auto')
        ax1.set_ylabel(r'saving-rates $s_i^c$', fontsize=par.fontsize)
        ax1.set_xlabel(r'mean update time $\tau$', fontsize=par.fontsize)
        ax1.set_title('sector c', fontsize=par.fontsize)
        ax1.tick_params(labelsize=par.ticksize)  
      
        img2 = ax2.imshow(np.transpose(histogrammMatrixF), **imshow_kwargs, aspect='auto')
        ax2.set_ylabel(r'saving-rates $s_i^f$', fontsize=par.fontsize)
        ax2.set_xlabel(r'mean update time $\tau$', fontsize=par.fontsize)
        ax2.set_title('sector f', fontsize=par.fontsize)
        ax2.tick_params(labelsize=par.ticksize)       
        
        fig.subplots_adjust(right=0.8)
        cbar_ax = fig.add_axes([0.85, 0.14, 0.05, 0.7])
        cbar = fig.colorbar(img2, cax=cbar_ax, ticks=[0,1,2,3,4,5])
        cbar.set_label(r'density of $s_i$ states', fontsize=par.fontsize)
        cbar.ax.set_yticklabels(['0','1','2','3','4','5'], size=par.ticksize)

        fig.tight_layout()
        fig.suptitle('Capital depreciation rate $\kappa = $' + str(par.depreciation), fontsize=par.fontsize)
        plt.subplots_adjust(left=0.062, bottom=0.096, right=0.822, top=0.887, wspace=0.21, hspace=0.14)
        plt.show()
        
        
        fig, (ax1,ax2) = plt.subplots(1, 2)
         
        ax1.plot(_bifurcParamArray, _avgOccupNumberC, color="g")
        #ax1.errorbar(_bifurcParamArray, _avgOccupNumberC, yerr=_varianzOccupC, color="g", capsize=3)
        ax1.set_ylabel(r'avg. occup. # $\overline{N}^c$', fontsize=par.fontsize)
        ax1.set_ylim([0, par.numOfAgents])
        ax1.set_xlabel(r'rel. productivity $\gamma$', fontsize=par.fontsize)
      #  ax4.set_xlim([0.9, 1.3])
        ax1.tick_params(labelsize=par.ticksize)
      
        ax2.plot(_bifurcParamArray, _avgOccupNumberF, color="brown")
        #ax2.errorbar(_bifurcParamArray, _avgOccupNumberF, yerr= _varianzOccupF,  color="brown", capsize=3)
        ax2.set_ylabel(r'avg. occup. # $\overline{N}^f$', fontsize=par.fontsize)
        ax2.set_xlabel(r'rel. productivity $\gamma$', fontsize=par.fontsize)
        ax2.set_ylim([0, par.numOfAgents])      
        ax2.tick_params(labelsize=par.ticksize)
        
        fig.tight_layout()
        plt.subplots_adjust(left=0.062, bottom=0.615, right=0.822, top=0.887, wspace=0.21, hspace=0.14)
        plt.show()
     
     
      
    def plot2DParameterHeatmap(self, _parameterMatrixC, _parameterMatrixF, _paramArray1, _paramArray2):
        xmin, xmax, ymin, ymax = (  _paramArray2[0], _paramArray2[-1] ,  _paramArray1[0], _paramArray1[-1])
        if _parameterMatrixC.max()>_parameterMatrixF.max():
            vmax = _parameterMatrixC.max()
        else:
            vmax = _parameterMatrixF.max()
        imshow_kwargs = {
            'vmin': 0,
            'vmax':vmax,
            'extent': (xmin, xmax, ymin, ymax),
        }
        fig, (ax1,ax2) = plt.subplots(1, 2)
        
        img1 = ax1.imshow(_parameterMatrixC, **imshow_kwargs, aspect='auto')
        ax1.set_ylabel(r'rel. productivity $\gamma$', fontsize=par.fontsize)
        ax1.set_xlabel(r'mean update time $\tau$', fontsize=par.fontsize)
        
        img2 = ax2.imshow(_parameterMatrixF, **imshow_kwargs, aspect='auto')
        ax2.set_ylabel(r'rel. productivity $\gamma$', fontsize=par.fontsize)
        ax2.set_xlabel(r'mean update time $\tau$', fontsize=par.fontsize)
        
        ax1.set_title('sector c', fontsize=par.fontsize)
        ax2.set_title('sector f', fontsize=par.fontsize)
        ax1.tick_params(labelsize=par.ticksize)
        ax2.tick_params(labelsize=par.ticksize)
        
        fig.subplots_adjust(right=0.8)
        cbar_ax = fig.add_axes([0.85, 0.14, 0.05, 0.7])
        cbar = fig.colorbar(img2, cax=cbar_ax, ticks=[0,1,2,3,4,5])
        cbar.set_label('density of splits', fontsize=par.fontsize)
        cbar.ax.set_yticklabels(['0','1','2','3','4','5'], size=par.ticksize)
        fig.tight_layout()
        
        fig.tight_layout()
        plt.subplots_adjust(left=0.062, bottom=0.096, right=0.822, top=0.887, wspace=0.21, hspace=0.14)
        plt.show()
        
     
    def plotMacroVariables(self):
        fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6),(ax7,ax8)) = plt.subplots(4, 2)

        ax1.plot(self.rentCVector, self.avgSavingsVectorC, linewidth=0.1)
        ax1.set_ylabel(r'$\overline{s}_i^c$', fontsize=par.fontsize)
        ax1.set_xlim([0,0.08])
                   
        ax2.plot( self.rentFVector,  self.avgSavingsVectorF, linewidth=0.2)
        ax2.set_ylabel(r'$\overline{s}_i^f$', fontsize=par.fontsize)
        ax2.set_xlim([0,0.08])
                  
        ax3.plot( self.tauTimeline,  self.occupNumberVectorC)
        ax3.set_ylabel(r'$N_c$', fontsize=par.fontsize)
        ax3.set_ylim([0, par.numOfAgents])
        
        ax4.plot( self.tauTimeline,  self.occupNumberVectorF)
        ax4.set_ylabel(r'$N_f$', fontsize=par.fontsize)
        ax4.set_ylim([0, par.numOfAgents])
        
        ax5.plot( self.tauTimeline,  self.totalCapitalCVector)
        ax5.set_ylabel(r'$K^c$', fontsize=par.fontsize)
        
        ax6.plot( self.tauTimeline,  self.totalCapitalFVector)
        ax6.set_ylabel(r'$K^f$', fontsize=par.fontsize)
        
        ax7.plot( self.tauTimeline,  self.maxConsumCVector)
        ax7.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        ax7.set_ylabel(r'$C_{max,c}$', fontsize=par.fontsize)
        
        ax8.plot( self.tauTimeline,  self.maxConsumFVector)
        ax8.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        ax8.set_ylabel(r'$C_{max,f}$', fontsize=par.fontsize)
        
        ax1.tick_params(labelsize=par.ticksize)
        ax2.tick_params(labelsize=par.ticksize)
        ax3.tick_params(labelsize=par.ticksize)
        ax4.tick_params(labelsize=par.ticksize)
        ax5.tick_params(labelsize=par.ticksize)
        ax6.tick_params(labelsize=par.ticksize)
        ax7.tick_params(labelsize=par.ticksize)
        ax8.tick_params(labelsize=par.ticksize)
        
        fig.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.081, right=0.96, top=0.963, wspace=0.21, hspace=0.14)
        plt.show()
     
          
    def plotCapitals(self, _sector):
        cmap = ListedColormap(['r', 'g'])
        norm = BoundaryNorm([2,2], cmap.N)
        if _sector=='c': 
            plt.ylabel(r'Capital $K_i^c$', fontsize=par.fontsize)   
            capitalsMatrix = self.capitalsCMatrix
        else:   
            plt.ylabel(r'Capital $K_i^f$', fontsize=par.fontsize) 
            capitalsMatrix = self.capitalsFMatrix
        for i in range(0,par.numOfAgents-1):
            capitalTrajectory           =  capitalsMatrix[:,i].T
            colorCodingArray            =  self.sectorIdMatrix[:,i].T
            points                      = np.array([ self.tauTimeline,  capitalTrajectory]).T.reshape(-1, 1, 2)
            segments                    = np.concatenate([points[:-1], points[1:]], axis=1)
            lc                          = LineCollection(segments, cmap=cmap, norm=norm)
            lc.set_array(colorCodingArray)
            lc.set_linewidth(1)
            plt.gca().add_collection(lc)
            plt.xlim(par.tmin, par.tend)
            plt.ylim(0, 50)
           
        plt.xlabel(r'$timesteps$', fontsize=par.fontsize)
        plt.yscale('symlog')
        plt.show()   
        
        
    def plotSavingsRates(self, _sector):
        if _sector=='c':
            savingsRatesMatrix = self.savingsRatesMatrixC
            avgSavingsVector   = self.avgSavingsVectorC
            markerColor        = 'r'
            sectorChange       = -1
            neighborSector     = 1
            plt.ylabel(r'$s_i^c$', fontsize=par.fontsize)
            label              =r'$\overline{s}_i^c$'
        else: 
            savingsRatesMatrix = self.savingsRatesMatrixF
            avgSavingsVector   = self.avgSavingsVectorF
            markerColor        = 'g'
            sectorChange       = 1  
            neighborSector     = 2
            plt.ylabel(r'$s_i^f$', fontsize=par.fontsize)
            label              =r'$\overline{s}_i^f$'
        for i in range(0,par.numOfAgents-1):
            sectorChangeId                     = self.getSectorChangeId(i, sectorChange)
            bestNeighborId                     = self.getBestNeighborsColorPlotVariables(i, neighborSector)
            savingsTrajectory, markerSavings   = self.getSavingsColorPlotVariables(i, savingsRatesMatrix, sectorChangeId)
            markerSectorChange                 = self.tauTimeline[sectorChangeId]
            markerBestNeighbor                 = self.tauTimeline[bestNeighborId]
            markerBestSavings                  = savingsTrajectory[bestNeighborId]
            line1 = plt.plot( self.tauTimeline, savingsTrajectory, linewidth=0.2, color='k')
            plt.scatter(markerSectorChange, markerSavings , marker = 'o', c=markerColor, alpha=0.2)
            plt.scatter(markerBestNeighbor, markerBestSavings , marker = 'o',   c='b', alpha=0.2)
           
        plt.tick_params(labelsize=par.ticksize)
        plt.plot( self.tauTimeline,  avgSavingsVector, linewidth=1.3, color='r', alpha=0.4, label=label) 
        plt.xlabel(r'$timesteps$', rotation=0, fontsize=par.fontsize)  
        plt.axis('off') 
        #plt.legend(loc='upper right')
        plt.show()    
 
        
    def plotIncomes(self, _sector):  
        fig, ax1 = plt.subplots()
        if _sector=='c':
            incomesMatrix  = self.incomesCMatrix
            markerColor    = 'r'
            sectorChange   = -1
            neighborSector = 1
            plt.ylabel(r'Incomes $I_i^c$', fontsize=par.fontsize)      
        else: 
            incomesMatrix  = self.incomesFMatrix
            markerColor    = 'g'
            sectorChange   = 1  
            neighborSector = 2
            plt.ylabel(r'Incomes $I_i^c$', fontsize=par.fontsize)
        for i in range(0,par.numOfAgents-1):           
            sectorChangeId                     = self.getSectorChangeId(i, sectorChange)
            bestNeighborId                     = self.getBestNeighborsColorPlotVariables(i, neighborSector)
            incomesTrajectory, markerIncomes   = self.getIncomesColorPlotVariables(i, incomesMatrix, sectorChangeId)
            markerSectorChange                 = self.tauTimeline[sectorChangeId]
            markerBestNeighbor                 = self.tauTimeline[bestNeighborId]
            markerBestIncomes                  = incomesTrajectory[bestNeighborId]           
           
            ax1.plot( self.tauTimeline, incomesTrajectory, linewidth=0.2, color='k')
            ax1.scatter(markerSectorChange, markerIncomes , marker = 'o', c=markerColor, alpha=0.7)
            ax1.scatter(markerBestNeighbor, markerBestIncomes , marker = 'o',   c='b', alpha=0.4)   
            ax1.yaxis.set_ticks_position('left')
            ax1.xaxis.set_ticks_position('bottom')   
            ax1.axis('off')     
         
 
        ax1.tick_params(labelsize=par.ticksize)
        #ax1.x_label(r'$timesteps$', rotation=0, fontsize=par.fontsize)   
        ax1.legend(loc='upper right')
        plt.show()    
           
    
    def plotAvgSavOverReturn(self):
        fig, (ax1,ax2) = plt.subplots(1, 2)

        ax1.plot(self.rentCVector, self.avgSavingsVectorC, linewidth=0.3)
        ax1.set_ylabel(r'$\overline{s}_i^c$', fontsize=par.fontsize)
        ax1.set_xlabel(r'$r^c$', fontsize=par.fontsize)
        ax1.set_ylim([0,1])
        ax1.set_xlim([0.03,0.1])
                   
        ax2.plot( self.rentFVector,  self.avgSavingsVectorF, linewidth=0.3)
        ax2.set_ylabel(r'$\overline{s}_i^f$', fontsize=par.fontsize)
        ax2.set_xlabel(r'$r^f$', fontsize=par.fontsize)
        ax2.set_ylim([0,1])
        ax2.set_xlim([0.03,0.1])
         
        ax1.tick_params(labelsize=par.ticksize)
        ax2.tick_params(labelsize=par.ticksize) 
        fig.tight_layout()
        plt.subplots_adjust(left=0.077, bottom=0.156, right=0.928, top=0.865, wspace=0.38, hspace=0.2)
        plt.show()  
    

        
    def plotOccupNumberOverReturn(self):
        fig, (ax1,ax2) = plt.subplots(1, 2)

        ax1.plot(self.rentCVector, self.occupNumberVectorC, linewidth=0.3)
        ax1.set_ylabel(r'occup. number $N^c$', fontsize=par.fontsize)
        ax1.set_xlabel(r'return $r^c$', fontsize=par.fontsize)
        ax1.set_xlim([0.03,0.1])
        ax1.set_ylim([0,100])
                   
        ax2.plot( self.rentFVector,  self.occupNumberVectorF, linewidth=0.3)
        ax2.set_ylabel(r'occup. number $N^f$', fontsize=par.fontsize)
        ax2.set_xlabel(r'return $r^f$', fontsize=par.fontsize)
        ax2.set_xlim([0.03,0.1])
        ax2.set_ylim([0,100])
        
        ax1.tick_params(labelsize=par.ticksize)
        ax2.tick_params(labelsize=par.ticksize) 
        fig.tight_layout()
        plt.subplots_adjust(left=0.077, bottom=0.156, right=0.928, top=0.865, wspace=0.38, hspace=0.2)
        plt.show()  
        
        
    def plotAvgSavOverOccupNumber(self):
        fig, (ax1,ax2) = plt.subplots(1, 2)

        ax1.plot(self.occupNumberVectorC, self.avgSavingsVectorC, linewidth=0.3, color='brown')
        ax1.set_ylabel(r'$\overline{s}_i^c$', fontsize=par.fontsize)
        ax1.set_ylim([0,1])
        ax1.set_xlabel(r'$N^c$', fontsize=par.fontsize)
        ax1.set_xlim([0,100])
                   
        ax2.plot( self.occupNumberVectorF,  self.avgSavingsVectorF, linewidth=0.3, color='brown')
        ax2.set_ylabel(r'$\overline{s}_i^f$', fontsize=par.fontsize)
        ax2.set_ylim([0,1])
        ax2.set_xlabel(r'$N^f$', fontsize=par.fontsize)
        ax2.set_xlim([0,100])
        
        ax1.tick_params(labelsize=par.ticksize)
        ax2.tick_params(labelsize=par.ticksize)
        fig.tight_layout()
        plt.subplots_adjust(left=0.077, bottom=0.156, right=0.928, top=0.865, wspace=0.38, hspace=0.2)
        plt.show()                   
        
        
    def plotAvgSavOverSav(self):
        fig, (ax1) = plt.subplots(1, 1)

        ax1.plot(self.avgSavingsVectorC, self.avgSavingsVectorF, linewidth=0.3, color='black')
        ax1.set_ylabel(r'avg. saving-rate $\overline{s}_i^f$', fontsize=par.fontsize)
        ax1.set_xlabel(r'avg. saving-rate $\overline{s}_i^c$', fontsize=par.fontsize)
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)
          
        fig.tight_layout()
        plt.subplots_adjust(left=0.06, bottom=0.1, right=0.932, top=0.939, wspace=0.2, hspace=0.2)
        plt.show()                   
                  
    
    def plotCapitalEquilibrium(self):
        fig, (ax1,ax2,ax3) = plt.subplots(3,1, sharex=True)
        ax4 = ax3.twinx()
       
        ax1.plot( self.tauTimeline,  self.capitalsCMatrix,  linewidth=0.1, color='k')
        ax1.plot( self.tauTimeline,  self.avgCapitalCVector, linewidth=1, color='r', label=r'$\overline{K}_i^c$')
        ax1.plot( self.tauTimeline, self.eqCapitalC, linewidth=1, color='b', label=r'$\overline{K}_i^{*c}$')
        ax1.set_ylabel(r'capitals $K_i^c$', fontsize=par.fontsize)
        ax1.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax1.set_yscale("symlog")
        
        ax2.plot( self.tauTimeline,  self.capitalsFMatrix, linewidth=0.1, color='k')
        ax2.plot( self.tauTimeline,  self.avgCapitalFVector, linewidth=1, color='r', label=r'$\overline{K}_i^f$')
        ax2.plot( self.tauTimeline, self.eqCapitalF, linewidth=1, color='b', label=r'$\overline{K}_i^{*f}$')
        ax2.set_ylabel(r'capitals $K_i^f$', fontsize=par.fontsize)
        ax2.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax2.set_yscale('symlog')
             
        ax3.plot( self.tauTimeline,  self.rentCVector, linewidth=1.5, color='g', label=r'$r^c$')
        ax3.set_ylabel(r'return $\r^c$', fontsize=par.fontsize)
        ax3.set_ylim(0.02, 0.09)
        ax3.legend(loc='upper right', prop={'size':par.fontsize-7})
        ax3.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        
        ax4.plot( self.tauTimeline,  self.rentFVector, linewidth=1.5, color='brown', label=r'$r^f$')
        ax3.set_ylabel(r'return $r^f$', fontsize=par.fontsize)
        ax4.set_ylim(0.02, 0.09)
        ax4.legend(loc='upper right', prop={'size':par.fontsize-7})
        
        ax1.tick_params(labelsize=par.ticksize)
        ax2.tick_params(labelsize=par.ticksize)
        ax3.tick_params(labelsize=par.ticksize)
        ax4.tick_params(labelsize=par.ticksize)
  
        fig.tight_layout()
        plt.subplots_adjust(left=0.07, bottom=0.1, right=0.96, top=0.963, wspace=0.21, hspace=0.14)
        plt.show()    
        
