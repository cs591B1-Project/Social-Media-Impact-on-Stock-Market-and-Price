
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('ge.xls')
v = readVolume('ge.xls')

calCorrelation(s,v)
