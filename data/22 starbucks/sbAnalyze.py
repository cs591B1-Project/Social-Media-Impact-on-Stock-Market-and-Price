
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('starbucks.xls')
v = readVolume('starbucks.xls')

calCorrelation(s,v)
