
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('boeing.xls')
v = readVolume('boeing.xls')

calCorrelation(s,v)
