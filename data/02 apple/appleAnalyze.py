
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('apple.xls')
v = readVolume('apple.xls')

calCorrelation(s,v)
