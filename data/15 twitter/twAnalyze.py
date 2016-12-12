
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('twitter.xls')
v = readVolume('twitter.xls')

calCorrelation(s,v)
