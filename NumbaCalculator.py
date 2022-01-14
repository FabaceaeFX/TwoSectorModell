import numpy as np
from numba import njit
import ParametersRCK as par


    
    
@njit    
def calculateWages(_totalCapital, _totalLabor):
    
    if _totalLabor != 0:
    
        wages = par.alpha * _totalLabor ** (par.alpha - 1) * _totalCapital ** par.beta
        
    else: 
    
        wages = 0
    
    return wages
    
@njit   
def calculateRents(_totalCapital, _totalLabor):

    if _totalCapital != 0:
    
        rent =  par.beta * _totalLabor ** par.alpha * _totalCapital ** (par.beta - 1)
        
    else: 
    
        rent = 0
    
    return rent
          
@njit                                                         
def calculateIncomes(_capitalsC, _capitalsF, _rentC, _rentF, _wagesC,\
                      _wagesF, _laborsC, _laborsF):

    incomes = _wagesC * _laborsC + _wagesF * _laborsF + _rentC * _capitalsC + _rentF * _capitalsF 
    
    return incomes
       
@njit                     
def calculateProduction(_totalCapital, _totalLabor):

    production = _totalCapital ** par.beta * _totalLabor ** par.alpha   
    
    return production
     
@njit      
def calculateConsumptions(_savingsRates, _incomes):

    consumptions = _incomes * (np.ones(len(_savingsRates)) - _savingsRates)
    
    return consumptions
    
@njit    
def calculateAvgSavingsC(_occupNumberC, _savingsRates, _sectorIdArray, _savingsSumC):

    if _occupNumberC != 0:
        avgSavingsC = _savingsSumC/_occupNumberC
        
    else:
        avgSavingsC = 0
        
    return avgSavingsC
    
@njit   
def calculateAvgSavingsF(_occupNumberF, _savingsRates, _sectorIdArray, _savingsSumF):

    if _occupNumberF != 0:
        avgSavingsF = _savingsSumF/_occupNumberF
        
    else:
        avgSavingsF = 0
    
    return avgSavingsF
    
    
   
@njit    
def calculateCapitalDots(_capitalsC, _capitalsF, _savingsRates, _incomes, _sectorIdArray, _indexC, _indexF):
    
    depreciationTermC          = -par.depreciation * _capitalsC
    depreciationTermF          = -par.depreciation * _capitalsF

    capitalDotsC          = np.ones(par.numOfAgents) * depreciationTermC
    capitalDotsF          = np.ones(par.numOfAgents) * depreciationTermF
    
    capitalDotsC[_indexC] += _savingsRates[_indexC]*_incomes[_indexC]                             
    capitalDotsF[_indexF] += _savingsRates[_indexF]*_incomes[_indexF]
    
    return capitalDotsC, capitalDotsF
    
    
@njit    
def calculateTotalLaborDot(_totalLaborC, _totalLaborF):

    totalLaborDotC        = par.populationGrowthRate * _totalLaborC
    totalLaborDotF        = par.populationGrowthRate * _totalLaborF
    
    return totalLaborDotC, totalLaborDotF
        

@njit        
def concatenateCapitalsAndTotalLabor(_capitalsC, _capitalsF, _totalLaborC, _totalLaborF):
    
    concatenatedInitsC    = np.append(_capitalsC, _totalLaborC)
    concatenatedInitsF    = np.append(_capitalsF, _totalLaborF)
    
    return concatenatedInitsC, concatenatedInitsF
    
    
@njit       
def RCKderiv(_capitalDots, _totalLaborDot):

    concatenatedDots     = np.append(_capitalDots, _totalLaborDot)
    
    return concatenatedDots
     
        


        
