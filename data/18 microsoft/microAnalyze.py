
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('microsoft.xls')
v = readVolume('microsoft.xls')

calCorrelation(s,v)
