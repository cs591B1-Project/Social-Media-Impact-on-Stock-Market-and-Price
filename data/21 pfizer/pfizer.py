
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('pfizer.xls')
v = readVolume('pfizer.xls')

calCorrelation(s,v)
