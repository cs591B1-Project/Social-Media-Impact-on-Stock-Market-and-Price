
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('walmart.xls')
v = readVolume('walmart.xls')

calCorrelation(s,v)
