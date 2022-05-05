import ParametersRCK     as par
import matplotlib        as mp
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy             as np


        

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
        
        #self.plotSavingsRates('c')
        #self.plotSavingsRates('f')
        #self.plotIncomes('c')
        #self.plotIncomes('f')
        self.plotIncOverInc()
        #self.plotSavOverSav()
        #self.plotSavingsOverInc('c')
        #self.plotSavingsOverInc('f')                                 
        self.plotMultiplot()
        #self.plotCapitalsOverSiOverRent('c')
        #self.plotCapitalsOverSiOverRent('f')
        
        
        
        
        
        
        
     
     
    def plotCapitals(self, _sector):

        cmap = ListedColormap(['r', 'g'])
        norm = BoundaryNorm([2,2], cmap.N)
        
        if _sector=='c': 
            plt.ylabel(r'Capital $K_{i,c}$', fontsize=par.fontsize)   
            capitalsMatrix = self.capitalsCMatrix
            
        else:   
            plt.ylabel(r'Capital $K_{i,f}$', fontsize=par.fontsize) 
            capitalsMatrix = self.capitalsFMatrix

        for i in range(0,par.numOfAgents-1):
            
            capitalTrajectory           =  capitalsMatrix[:,i].T
            colorCodingArray            =  self.sectorIdMatrix[:,i].T
            points                      = np.array([ self.tauTimeline, capitalTrajectory]).T.reshape(-1, 1, 2)
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
        
        
        
        
        

    def plotCapitalsOverSiOverRent(self, _sector):
    
        fig, (ax1,ax2, ax3) = plt.subplots(3, 1, sharex=True)
        ax4 = ax3.twinx()
            
        
        cmap = ListedColormap(['g', 'r'])
        norm = BoundaryNorm([2,2], cmap.N)
        
        if _sector=='c': 
            ax1.set_ylabel(r'Capital $K_{i,c}$', fontsize=par.fontsize)   
            ax3.set_ylabel(r'return $r_c$', color='tab:blue', fontsize=par.fontsize)
            ax4.set_ylabel(r'tot. capital $K_c$', color='tab:orange', fontsize=par.fontsize)
            capitalsMatrix = self.capitalsCMatrix
            savingsRates   = self.savingsRatesMatrixC
            avgSavings     = self.avgSavingsVectorC
            rent           = self.rentCVector
            totalCapital   = self.totalCapitalCVector
                        
        else:   
            ax1.set_ylabel(r'Capital $K_{i,f}$', fontsize=par.fontsize) 
            ax3.set_ylabel(r'return $r_f$', color='tab:blue', fontsize=par.fontsize)
            ax4.set_ylabel(r'tot. capital $K_f$', color='tab:orange', fontsize=par.fontsize)
            capitalsMatrix = self.capitalsFMatrix
            savingsRates   = self.savingsRatesMatrixF
            avgSavings     = self.avgSavingsVectorF
            rent           = self.rentFVector
            totalCapital   = self.totalCapitalFVector
            
        for i in range(0,par.numOfAgents-1):
            
            capitalTrajectory           =  capitalsMatrix[:,i].T
            colorCodingArray            =  self.sectorIdMatrix[:,i].T
            points                      = np.array([ self.tauTimeline, capitalTrajectory]).T.reshape(-1, 1, 2)
            segments                    = np.concatenate([points[:-1], points[1:]], axis=1)
            lc                          = LineCollection(segments, cmap=cmap, norm=norm)
            lc.set_array(colorCodingArray)
            lc.set_linewidth(1)

           
            ax1.add_collection(lc)
        
        

            
        ax1.set_xlim(0, 4333)
        ax1.set_ylim(0, 50)   
        ax1.set_yscale('symlog')   
           
        ax2.plot( self.tauTimeline,  savingsRates, linewidth=0.4)
        ax2.plot( self.tauTimeline,  avgSavings, linewidth=1, color='k', label=r'$\overline{s}_{i,c}$')
        ax2.set_ylabel(r'Savings-rate $s_{i,c}$', fontsize=par.fontsize)
        ax2.set_ylim([0,1])
        ax2.legend(loc='upper right')
             
        ax3.plot(self.tauTimeline, rent) 
        ax3.set_ylim(0.03,0.07)
        ax3.tick_params(axis='y', labelcolor='tab:blue')
        
        ax4.plot(self.tauTimeline, totalCapital, color='orange')       
        ax4.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
        ax4.set_ylim(10, 100)
        ax4.tick_params(axis='y', labelcolor='tab:orange')
        

        fig.tight_layout()
        plt.subplots_adjust(wspace=0.1, hspace=0.1)
        plt.show()
        
     
     
        
        
    def plotSavingsRates(self, _sector):
    
        if _sector=='c':
            savingsRatesMatrix = self.savingsRatesMatrixC
            avgSavingsVector   = self.avgSavingsVectorC
            markerColor        = 'r'
            sectorChange       = -1
            neighborSector     = 1
            plt.ylabel(r'Savings rate $s_{i,c}$', fontsize=par.fontsize)
            label              =r'$\overline{s}_{i,c}$'
        else: 
            savingsRatesMatrix = self.savingsRatesMatrixF
            avgSavingsVector   = self.avgSavingsVectorF
            markerColor        = 'g'
            sectorChange       = 1  
            neighborSector     = 2
            plt.ylabel(r'Savings rate $s_{i,f}$', fontsize=par.fontsize)
            label              =r'$\overline{s}_{i,f}$'
        
        for i in range(0,par.numOfAgents-1):
            
            sectorChangeId                     = self.getSectorChangeId(i, sectorChange)
            bestNeighborId                     = self.getBestNeighborsColorPlotVariables(i, neighborSector)
            savingsTrajectory, markerSavings   = self.getSavingsColorPlotVariables(i, savingsRatesMatrix, sectorChangeId)
           
            markerSectorChange                 = self.tauTimeline[sectorChangeId]
            markerBestNeighbor                 = self.tauTimeline[bestNeighborId]
            
            markerBestSavings                  = savingsTrajectory[bestNeighborId]
            
            line1 = plt.plot( self.tauTimeline, savingsTrajectory, linewidth=0.2, color='k')
            plt.scatter(markerSectorChange, markerSavings , marker = 'o', c=markerColor, alpha=1)
            plt.scatter(markerBestNeighbor, markerBestSavings , marker = 'o',   c='b', alpha=1)
           
   
        
        plt.plot( self.tauTimeline,  avgSavingsVector, linewidth=1.3, color='r', alpha=1, label=label) 
        plt.xlabel(r'$timesteps$', rotation=0, fontsize=par.fontsize)   
        plt.legend(loc='upper right')
        plt.show()
        
        
        
        
        
        
        
        
    def plotIncomes(self, _sector):
    
        if _sector=='c':
            incomesMatrix  = self.incomesCMatrix
            markerColor    = 'r'
            sectorChange   = -1
            neighborSector = 1
            plt.ylabel(r'Incomes $I_{i,c}$', fontsize=par.fontsize)
            
        else: 
            incomesMatrix  = self.incomesFMatrix
            markerColor    = 'g'
            sectorChange   = 1  
            neighborSector = 2
            plt.ylabel(r'Incomes $I_{i,c}$', fontsize=par.fontsize)
        
        for i in range(0,par.numOfAgents-1):
            
            sectorChangeId                     = self.getSectorChangeId(i, sectorChange)
            bestNeighborId                     = self.getBestNeighborsColorPlotVariables(i, neighborSector)
            incomesTrajectory, markerIncomes   = self.getIncomesColorPlotVariables(i, incomesMatrix, sectorChangeId)
           
            markerSectorChange                 = self.tauTimeline[sectorChangeId]
            markerBestNeighbor                 = self.tauTimeline[bestNeighborId]
            
            markerBestIncomes                  = incomesTrajectory[bestNeighborId]
            
           
            plt.plot( self.tauTimeline, incomesTrajectory, linewidth=0.2, color='k')
            plt.scatter(markerSectorChange, markerIncomes , marker = 'o', c=markerColor, alpha=1)
            plt.scatter(markerBestNeighbor, markerBestIncomes , marker = 'o',   c='b', alpha=1)
            
            
            plt.xlim(par.tmin, par.tend)
            plt.ylim(0,1.8)
           
       
       

        plt.axis('off')
        plt.xlabel(r'$timesteps$', rotation=0, fontsize=par.fontsize)   
        plt.legend(loc='upper right')
        plt.show()
        
        
     
     
     



    def plotSavingsOverInc(self, _sector):
    
        if _sector=='c':
            savingsRatesMatrix = self.savingsRatesMatrixC
            incomesMatrix      = self.incomesCMatrix
            rentVector         = self.rentCVector
            occupNumberVector  = self.occupNumberVectorC
            
            markerColor    = 'r'
            sectorChange   = -1
            neighborSector = 1
            siLabel        = r'$s_{i,c}$'
            IiLabel        = r'$I_{i,c}$'
            NLabel         = r'$N_c$'
            rLabel         = r'$r_c$'
            
        else: 
            incomesMatrix      = self.incomesFMatrix
            savingsRatesMatrix = self.savingsRatesMatrixF
            rentVector         = self.rentFVector
            occupNumberVector  = self.occupNumberVectorF
            markerColor    = 'g'
            sectorChange   = 1  
            neighborSector = 2
            siLabel        = r'$s_{i,f}$'
            IiLabel        = r'$I_{i,f}$'
            NLabel         = r'$N_f$'
            rLabel         = r'$r_f$'
            
            
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
            
            line1 = ax1.plot( self.tauTimeline, savingsTrajectory, linewidth=0.2, color='k')
            ax1.scatter(markerSectorChange, markerSavings , marker = 'o', c=markerColor, alpha=1)
            ax1.scatter(markerBestNeighbor, markerBestSavings , marker = 'o',   c='b', alpha=1)
           
            line2  = ax2.plot( self.tauTimeline, incomesTrajectory, linewidth=0.2, color='k')
            ax2.scatter(markerSectorChange, markerIncomes , marker = 'o', c=markerColor, alpha=1)
            ax2.scatter(markerBestNeighbor, markerBestIncomes , marker = 'o',   c='b', alpha=1)
            
            
        ax1.set_ylabel(siLabel, fontsize=par.fontsize)
        ax2.set_ylabel(IiLabel, fontsize=par.fontsize)
        ax3.set_ylabel(rLabel, fontsize=par.fontsize) 
        ax4.set_ylabel(NLabel, fontsize=par.fontsize)   
           
        ax3.plot(self.tauTimeline, rentVector) 
        ax3.set_ylim(0.03,0.07)
        ax3.tick_params(axis='y', labelcolor='tab:blue')
        ax3.set_xlabel(r'$timesteps$', rotation=0, fontsize=par.fontsize)

        
        
        ax4.plot( self.tauTimeline, occupNumberVector, color='g')
        ax4.set_ylim([0, par.numOfAgents])
        ax4.tick_params(axis='y', labelcolor='tab:green') 
          

        fig.tight_layout()
        plt.subplots_adjust(left=0.036, bottom=0.034, right=0.97, top=0.963, wspace=0.2, hspace=0.116)
        plt.show()
        
        
    def plotSavOverSav(self):
    
            
        fig, ((ax1,ax2),(ax3, ax4)) = plt.subplots(2, 2, sharex=True)
        ax3.axis('off')
            
        
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
            ax1.scatter(markerSectorChangeC, markerSavingsC, marker = 'o', c='r', alpha=1)
            ax1.scatter(markerBestNeighborC, markerBestSavingsC , marker = 'o',   c='b', alpha=1)
           
            ax2.plot( self.tauTimeline, savingsTrajectoryF, linewidth=0.2, color='k')
            ax2.scatter(markerSectorChangeF, markerSavingsF , marker = 'o', c='g', alpha=1)
            ax2.scatter(markerBestNeighborF, markerBestSavingsF , marker = 'o',   c='b', alpha=1)
            
            ax4.plot( self.tauTimeline, savingsTrajectoryF, linewidth=0.2, color='k')
            ax4.scatter(markerSectorChangeF, markerSavingsF , marker = 'o', c='g', alpha=1)
            ax4.scatter(markerBestNeighborF, markerBestSavingsF , marker = 'o',   c='b', alpha=1)
            
            
        ax1.set_ylabel(r'$s_{i,c}$', fontsize=par.fontsize)
        ax2.set_ylabel(r'$s_{i,f}$', fontsize=par.fontsize)
        ax4.set_ylabel(r'$s_{i,f}$', fontsize=par.fontsize)
        
        ax1.set_xlabel(r'$timesteps$', rotation=0, fontsize=par.fontsize) 
        ax4.set_xlabel(r'$timesteps$', rotation=0, fontsize=par.fontsize) 
          
        
        fig.tight_layout()
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
            
            
        ax1.set_ylabel(r'$I_{i,c}$', fontsize=par.fontsize)
        ax2.set_ylabel(r'$I_{i,f}$', fontsize=par.fontsize)
        ax2.set_xlabel(r'$timesteps$', rotation=0, fontsize=par.fontsize) 
          
        ax1.tick_params(labelsize=par.ticksize)
        ax2.tick_params(labelsize=par.ticksize)
        
        
                
        
        fig.tight_layout()
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
        

        
        
    def plotMultiplot(self):
        
     
            
        if par.plotSetting == 'Two':
        
            fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2, 2, sharex=True)
            
            ax1.plot( self.tauTimeline,  self.capitalsCMatrix,  linewidth=0.1, color='k')
            ax1.plot( self.tauTimeline,  self.avgCapitalCVector, linewidth=1, color='r', label=r'$\overline{K}_{i,c}$')
            ax1.plot( self.tauTimeline, self.eqCapitalC, linewidth=1, color='g')
            ax1.set_ylabel(r'Capital $K_{i,c}$', fontsize=par.fontsize)
            ax1.legend(loc='upper right')
            ax1.set_yscale("symlog")
            
            ax2.plot( self.tauTimeline,  self.capitalsFMatrix, linewidth=0.1, color='k')
            ax2.plot( self.tauTimeline,  self.avgCapitalFVector, linewidth=1, color='r', label=r'$\overline{K}_{i,f}$')
            ax2.plot( self.tauTimeline, self.eqCapitalF, linewidth=1, color='g')
            ax2.set_ylabel(r'Capital $K_{i,f}$', fontsize=par.fontsize)
            ax2.legend(loc='upper right')
            ax2.set_yscale('symlog')
            
           
            ax3.plot( self.tauTimeline,  self.savingsRatesMatrixC, linewidth=0.4)
            ax3.plot( self.tauTimeline,  self.avgSavingsVectorC, linewidth=1, color='k', label=r'$\overline{s}_{i,c}$')
            ax3.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
            ax3.set_ylabel(r'Savings rate $s_{i,c}$', fontsize=par.fontsize)
            ax3.set_ylim([0,1])
            ax3.legend(loc='upper right')
            
            ax4.plot( self.tauTimeline,  self.savingsRatesMatrixF, linewidth=0.4)
            ax4.plot( self.tauTimeline,  self.avgSavingsVectorF, linewidth=1, color='k', label=r'$\overline{s}_{i,f}$')
            ax4.set_xlabel(r'$timesteps$', fontsize = 16)
            ax4.set_ylabel(r'Savings rate $s_{i,f}$', fontsize=par.fontsize)
            ax4.set_ylim([0,1])
            ax4.legend(loc='upper right')
            
            
      
            
            fig.tight_layout()
            plt.show()
            
            fig, ((ax1,ax2),(ax3,ax4),(ax5,ax6),(ax7,ax8)) = plt.subplots(4, 2, sharex=True)

            
            ax1.plot( self.tauTimeline,  self.rentCVector)
            ax1.set_ylabel(r'$r_c$', fontsize=par.fontsize)
            ax1.set_yscale('symlog')
            ax1.set_ylim([0, 0.1])
                       
            ax2.plot( self.tauTimeline,  self.rentFVector)
            ax2.set_ylabel(r'$r_f$', fontsize=par.fontsize)
            ax2.set_yscale('symlog')
            ax2.set_ylim([0, 0.1])
                      
            ax3.plot( self.tauTimeline,  self.occupNumberVectorC)
            ax3.set_ylabel(r'$N_c$', fontsize=par.fontsize)
            ax3.set_ylim([0, par.numOfAgents])
            
            ax4.plot( self.tauTimeline,  self.occupNumberVectorF)
            ax4.set_ylabel(r'$N_f$', fontsize=par.fontsize)
            ax4.set_ylim([0, par.numOfAgents])
            
            ax5.plot( self.tauTimeline,  self.eqCapitalC)
            ax5.set_ylabel(r'$\overline{s}_{i,c}$', fontsize=par.fontsize)
            
            ax6.plot( self.tauTimeline,  self.eqCapitalF)
            ax6.set_ylabel(r'$\overline{s}_{i,c}$', fontsize=par.fontsize)
            
            ax7.plot( self.tauTimeline,  self.maxConsumCVector)
            ax7.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
            ax7.set_ylabel(r'$C_{max,c}$', fontsize=par.fontsize)
            
            ax8.plot( self.tauTimeline,  self.maxConsumFVector)
            ax8.set_xlabel(r'$timesteps$', fontsize=par.fontsize)
            ax8.set_ylabel(r'$C_{max,f}$', fontsize=par.fontsize)
            
            
            fig.tight_layout()
            plt.show()
     
     
     
     

      
      
    def plotHeatMap(self, _lastSavingsMatrix, _bifurcParamArray):

        print(_bifurcParamArray)
        print(_lastSavingsMatrix.shape)
        xmin, xmax, ymin, ymax = ( _bifurcParamArray[0],  _bifurcParamArray[-1], 0, 1)
        binsEdges = np.linspace(0,1,par.numOfBins+1)
        histogrammMatrix = np.zeros((len( _bifurcParamArray), par.numOfBins))

        for index in range(0, len( _bifurcParamArray)):
            
            histogrammArray            = np.histogram(_lastSavingsMatrix[index,:], bins=binsEdges)[0]
            histogrammMatrix[index, :] = np.flip(histogrammArray)



        imshow_kwargs = {
            'vmax': par.vmax,
            'vmin': 0,
            'cmap': 'inferno',
            'extent': (xmin*20, xmax*20, ymin, ymax),
        }

        fig, ax = plt.subplots()
        img = ax.imshow(np.transpose(histogrammMatrix), **imshow_kwargs)
        fig.colorbar(img)

        plt.show()
        


        
        
    
    
