
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('jj.xls')
v = readVolume('jj.xls')

calCorrelation(s,v)
