
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('netflix.xls')
v = readVolume('netflix.xls')

calCorrelation(s,v)
