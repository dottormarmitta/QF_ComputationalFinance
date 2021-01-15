# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# #                                                  # #
# #  Here I want to create an object consisting of   # #
# #  a stream of payments, which is often used in    # #
# #  finance and financial applications. Ideally,    # #
# #  treat this as an array of floating numbers.     # #
# #                                                  # #

# My Object:
class StreamOfPayments:

    # Constructor:
    # I expect the following parameters:
    #
    # 1. paymentsTime MUST BE a list
    # 2. paymentsValue can either be a FLOAT (as constant payment) or LIST
    # 3. discountingFactors MUST BE a list
    def __init__(self, paymentsTime, paymentsValue, discountingFactors):

        # Some error checking on input:
        if not isinstance(paymentsTime, list):
            raise Exception("Wrong input type.")
        if not isinstance(paymentsValue, list):
            if isinstance(paymentsValue, float):
                paymentsValue = [paymentsValue]*len(paymentsTime)
        if not isinstance(discountingFactors, list):
            raise Exception("Wrong input type.")
        if not len(paymentsTime) == len(discountingFactors) and len(discountingFactors) == len(paymentsValue):
            raise Exception("Lengths do not agree.")

        # Building main field of my object
        # I find convenient to store the payment stream inside a dictonary: in this
        # way I can easily access the payments by their location in times!
        #
        # paymentStream = {time: [value, discounting]}
        localDict = {}
        for i in range(len(paymentsValue)):
            localDict[paymentsTime[i]] = [paymentsValue[i], discountingFactors[i]]
        self.paymentStream = localDict

    def getPresentValue(self):
        """
              p1     p2     p3               pn
        |------|------|------|------...------|------|---->
        0      t1     t2     t3               tn          time
    
        We know that:
        V(0) = p1*d1 + p2*d2 + p3*d3 + ... + pn*dn
     
        where pi is the payment at time i and d1 is the discounting factor
        between [0,i]
        """
        presentValue = 0
        for time in self.paymentStream:
            presentValue += self.paymentStream[time][0]*self.paymentStream[time][1]
        return presentValue
    
    def getTir(self):
        """
        This method returns 
        """
        presentValue = 0
        for time in self.paymentStream:
            presentValue += self.paymentStream[time][0]*self.paymentStream[time][1]
        return presentValue

    