# © Guglielmo Del Sarto -> guglielmo.delsarto@outlook.com

# Here I show how to StreamOfPayment is used

# First, we have to import it:
from StreamOfPayment import StreamOfPayments

# I build a new, consisting of various payments:
timeIntervals = [0, 0.5, 1, 1.5]
payments = [-100, 50, 30, 20]
discountingFactors = [1, 0.99, 0.98, 0.97]
myFirstStream = StreamOfPayments(timeIntervals, payments, discountingFactors)
print(myFirstStream.getPresentValue())