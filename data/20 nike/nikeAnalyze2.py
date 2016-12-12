
from readStockData import readClosingPrice
from readStockData import readVolume
from dataAnalysis import calCorrelation

s = readClosingPrice('nike.xls')
v = readVolume('nike.xls')

calCorrelation(s,v)
