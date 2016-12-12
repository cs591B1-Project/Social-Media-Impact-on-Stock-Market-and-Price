
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('cvs.xls')
v = readVolume('cvs.xls')

calCorrelation(s,v)
