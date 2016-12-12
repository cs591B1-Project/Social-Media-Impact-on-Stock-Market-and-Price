
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('amazon.xls')
v = readVolume('amazon.xls')

calCorrelation(s,v)
