
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('exxon.xls')
v = readVolume('exxon.xls')

calCorrelation(s,v)
