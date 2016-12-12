
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('mcdonalds.xls')
v = readVolume('mcdonalds.xls')

calCorrelation(s,v)
