# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

import math

# #                                                  # #
# #  Here I want to create an object consisting of   # #
# #  a rate converter, which is often used in        # #
# #  finance and financial applications.             # #
# #                                                  # #

class SpotRateConverter():
    """
    Convert from one rate type to another. Given SPOT Bond, Rate or Yield curve
    it performs useful actions

    ...

    Attributes
    ----------
    valuesDict : dict
        a dictonary of the kind {time: value} of the kind
        {[t, T]: v(t, T)} where v can either be B, i, h

    Methods
    -------
    getBondPrices()
        return a dictonary {time: bondPrice} of the kind {[t, T]: P(t, T)}
    
    getRates()
        return a dictonary {time: rates} of the kind {[t, T]: i(t, T)}

    getYields()
        return a dictonary {time: yields} of the kind {[t, T]: h(t, T)}

    getForwardBond()
        return a dictonary {time: Bond} of the kind {[0, t, T]: P(0, t, T)}
    
    getForwardRates()
        return a dictonary {time: rates} of the kind {[0, t, T]: i(0, t, T)}
    
    getForwardYields()
        return a dictonary {time: yelds} of the kind {[0, t, T]: h(0, t, T)}
    
    """
    
    # Constructor. This class must be constructed using:
    #
    # 1. A list of times, which are intended to be maturity of rates
    # 2. A list of floating values
    # 3. The type of values provided: {Bond, Rate, Yield}
    def __init__(self, times, values, rateType):
        """
        Parameters
        ----------
        times : list
            which are intended to be maturities
        values : list
            list of values (can also be a single floating if flat curve)
        rateType : str
            "Bond", "Rate" or "Yield" identifying input type
        """

        # Input checking:
        if not isinstance(times, list):
            raise Exception("Wrong input type: times must be a list!")
        if not isinstance(values, list):
            if isinstance(values, float):
                values = [values]*len(times)
            else:
                raise Exception("Wrong input type: values must be at least float!")
        if values[0] == 1 or times[0] == [0, 0]:
            raise Exception("Do not provide value for B(0,0), i(0,0) or h(0,0): it is already assumed to be 1")
        if not (rateType == "Bond" or rateType == "Rate" or rateType == "Yield"):
            raise Exception("Wrong input type: rate type must either be: Bond, Rate, Yield")
        if not (len(values) == len(times)):
            raise Exception("Length of input do not agree.")
        
        # Building block:
        localDict = {}
        for i in range(len(times)):
            localDict[tuple(times[i])] = values[i]
        self.valuesDict = localDict
        self.valuesType = rateType

    # Methods:
    def getBondPrices(self):

        # Divivde from the three cases:
        if (self.valuesType == "Bond"):
            return self.valuesDict

        elif (self.valuesType == "Rate"):
            bondDict = {}
            for t in self.valuesDict:
                bondDict[t] = (self.valuesDict[t] + 1)**(-(t[1]-t[0]))
            return bondDict

        elif (self.valuesType == "Yield"):
            bondDict = {}
            for t in self.valuesDict:
                bondDict[t] = math.exp(self.valuesDict[t]*(-(t[1]-t[0])))
            return bondDict
            
    def getRates(self):

        # Divivde from the three cases:
        if (self.valuesType == "Bond"):
            ratesDict = {}
            for t in self.valuesDict:
                ratesDict[t] = self.valuesDict[t]**(-1/(t[1]-t[0])) - 1
            return ratesDict

        elif (self.valuesType == "Rate"):
            return self.valuesDict

        elif (self.valuesType == "Yield"):
            ratesDict = {}
            for t in self.valuesDict:
                ratesDict[t] = math.exp(self.valuesDict[t]) - 1
            return ratesDict

    def getYields(self):

        # Divivde from the three cases:
        if (self.valuesType == "Bond"):
            yieldsDict = {}
            for t in self.valuesDict:
                yieldsDict[t] = (-1/(t[1]-t[0]))*math.log(self.valuesDict[t])
            return yieldsDict

        elif (self.valuesType == "Rate"):
            yieldsDict = {}
            for t in self.valuesDict:
                yieldsDict[t] = math.log(1+self.valuesDict[t])
            return yieldsDict

        elif (self.valuesType == "Yield"):
            return self.valuesDict
    
    def getForwardBond(self):
        """
        This function returns B(0, t, T)

        """
        # We have to find every T which is in {[0,T]: value}
        availableTimes = []
        for t in self.valuesDict:
            availableTimes.append(t[1])

        # Divivde from the three cases:
        if (self.valuesType == "Bond"):
            fwdBond = {}
            for t in availableTimes:
                for T in availableTimes:
                    if (t<T):
                        fwdBond[tuple([0, t, T])] = self.valuesDict[tuple([0,T])]/self.valuesDict[tuple([0,t])]
            return fwdBond

        elif (self.valuesType == "Rate"):
            bondPrices = self.getBondPrices()
            fwdBond = {}
            for t in availableTimes:
                for T in availableTimes:
                    if (t<T):
                        fwdBond[tuple([0, t, T])] = bondPrices[tuple([0,T])]/bondPrices[tuple([0,t])]
            return fwdBond

        elif (self.valuesType == "Yield"):
            bondPrices = self.getBondPrices()
            fwdBond = {}
            for t in availableTimes:
                for T in availableTimes:
                    if (t<T):
                        fwdBond[tuple([0, t, T])] = bondPrices[tuple([0,T])]/bondPrices[tuple([0,t])]
            return fwdBond
    
    def getForwardRates(self):
        """ This function returns i(0, t, T) """
        forwardBond = self.getForwardBond()
        convertableBonds = []
        convetableTimes = []
        for t in forwardBond:
            convetableTimes.append([t[1], t[2]])
            convertableBonds.append(forwardBond[t])
        myCurrentObj = SpotRateConverter(convetableTimes, convertableBonds, "Bond")
        rawRates = myCurrentObj.getRates()
        orderedRates = {}
        for t in rawRates:
            orderedRates[tuple([0]) + t] = rawRates[t]
        return orderedRates

    def getForwardYields(self):
        """ This function returns i(0, t, T) """
        forwardBond = self.getForwardBond()
        convertableBonds = []
        convetableTimes = []
        for t in forwardBond:
            convetableTimes.append([t[1], t[2]])
            convertableBonds.append(forwardBond[t])
        myCurrentObj = SpotRateConverter(convetableTimes, convertableBonds, "Bond")
        rawRates = myCurrentObj.getYields()
        orderedRates = {}
        for t in rawRates:
            orderedRates[tuple([0]) + t] = rawRates[t]
        return orderedRates
    




           