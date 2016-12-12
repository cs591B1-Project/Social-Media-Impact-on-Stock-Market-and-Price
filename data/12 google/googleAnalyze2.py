
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('google.xls')
v = readVolume('google.xls')

calCorrelation(s,v)
