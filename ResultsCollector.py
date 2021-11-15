class ResultsCollector:

    def __init__(self):
        pass
        
    def getResultsHeaders(self):

        listHeaders = ["Time","Capitals", "totalLabor", "Wages", "Rent", "incomes", \
                                         "Production", "SavingsRates", "Consumptions"]

        return listHeaders
        
        
    def getResultsLine(self, _time, _capitals, _totalLabor, _wages, _rent, _incomes, _production, _savingsRates, _consumptions):
                                       
        listEntry = [_time, _capitals, _totalLabor, _wages, _rent, _incomes, _production, _savingsRates,  _consumptions]
                                          
        return listEntry
        
        

