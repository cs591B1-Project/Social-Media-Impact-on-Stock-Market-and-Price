
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('timewarner.xls')
v = readVolume('timewarner.xls')

calCorrelation(s,v)
