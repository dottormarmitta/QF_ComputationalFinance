# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

from RateConverter import SpotRateConverter

# Build my object:
times = [[0, 1], [0,2], [0,3], [0,4], [0,5]]
yields = [0.02, 0.02, 0.021, 0.021, 0.022]
myRateConv = SpotRateConverter(times,yields,"Yield")

# Some testing
print("Bond prices: ", myRateConv.getBondPrices())
print()
print("Rates: ", myRateConv.getRates())
print()
print("Yields: ", myRateConv.getYields())
print()
print("ForwardBond: ", myRateConv.getForwardBond())
print()
print("ForwardRates: ", myRateConv.getForwardRates())
print()
print("Forward yields: ", myRateConv.getForwardYields())
