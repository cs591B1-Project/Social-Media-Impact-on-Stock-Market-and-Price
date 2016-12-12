negativeFileName = 'nike_neg_'
postiveFileName = 'nike_pos_'
neutralFileName = 'nike_neu_'
numNegativ = 15
numPositive = 1
numNeutral = 2

for x in range(1, numNegativ+1):
	fileName = negativeFileName + str(x) + '.json'
	print fileName
	
