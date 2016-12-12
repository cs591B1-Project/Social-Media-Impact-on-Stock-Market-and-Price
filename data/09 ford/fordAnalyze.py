
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('ford.xls')
v = readVolume('ford.xls')

calCorrelation(s,v)
