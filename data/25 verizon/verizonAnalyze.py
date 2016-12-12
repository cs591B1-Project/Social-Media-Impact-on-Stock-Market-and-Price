
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('verizon.xls')
v = readVolume('verizon.xls')

calCorrelation(s,v)
