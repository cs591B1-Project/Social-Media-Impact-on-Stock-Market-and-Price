
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('ibm.xls')
v = readVolume('ibm.xls')

calCorrelation(s,v)
