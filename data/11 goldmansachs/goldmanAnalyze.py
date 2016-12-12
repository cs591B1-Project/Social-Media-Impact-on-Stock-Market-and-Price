
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('goldmansachs.xls')
v = readVolume('goldmansachs.xls')

calCorrelation(s,v)
