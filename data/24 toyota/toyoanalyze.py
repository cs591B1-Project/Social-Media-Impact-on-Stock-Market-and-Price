
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('toyota.xls')
v = readVolume('toyota.xls')

calCorrelation(s,v)
