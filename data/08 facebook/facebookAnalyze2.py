
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('facebook.xls')
v = readVolume('facebook.xls')

calCorrelation(s,v)
