
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('bankofamerica.xls')
v = readVolume('bankofamerica.xls')

calCorrelation(s,v)
