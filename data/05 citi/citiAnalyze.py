
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('citi.xls')
v = readVolume('citi.xls')

calCorrelation(s,v)
