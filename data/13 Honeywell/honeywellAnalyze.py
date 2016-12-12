
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('honeywell.xls')
v = readVolume('honeywell.xls')

calCorrelation(s,v)
