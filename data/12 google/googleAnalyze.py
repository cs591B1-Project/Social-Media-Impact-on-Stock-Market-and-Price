import numpy
from numpy import *
from operator import truediv
from ast import literal_eval
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as st
import scipy.stats as scit

s = [ 782.52002,
782.52002,
782.52002,
790.51001,
785.309998,
762.559998,
754.02002,
754.02002,
754.02002,
736.080017,
758.48999,
764.47998,
771.22998,
760.539978,
760.539978,
760.539978,
769.200012,
768.27002,
760.98999,
760.98999,
761.679993,
761.679993,
761.679993,
768.23999,
770.840027,
758.039978,
747.919983,
750.5,
750.5,
750.5]

p = [line.rstrip('\n') for line in open("positive.txt")]
n = [line.rstrip('\n') for line in open("negative.txt")]
a = [line.rstrip('\n') for line in open("all.txt")]

pInt = numpy.array(map(float, p))+1
nInt = numpy.array(map(float, n))+1
aInt = numpy.array(map(float, a))+1

p_social = [line.rstrip('\n') for line in open("positive_social.txt")]
n_social = [line.rstrip('\n') for line in open("negative_social.txt")]
a_social = [line.rstrip('\n') for line in open("all_social.txt")]

p_s_Int = numpy.array(map(float, p_social))+1
n_s_Int = numpy.array(map(float, n_social))+1
a_s_Int = numpy.array(map(float, a_social))+1

# Grab 30 data points for analysis
pInt = pInt[0:30]
nInt = nInt[0:30]
aInt = aInt[0:30]

p_corr = numpy.corrcoef([pInt, s])
n_corr = numpy.corrcoef([nInt, s])
a_corr = numpy.corrcoef([aInt, s])

print "Positive Sentiment: " + str(p_corr)
print "Negative Sentiment: " + str(n_corr)
print "Neutral Sentiment: " + str(a_corr)

# Grab 30 data points for p_s_Int
p_s_Int = p_s_Int[0:30]
n_s_Int = n_s_Int[0:30]
a_s_Int = a_s_Int[0:30]

print p_s_Int

p_s_corr = numpy.corrcoef([p_s_Int, s])
n_s_corr = numpy.corrcoef([n_s_Int, s])
a_s_corr = numpy.corrcoef([a_s_Int, s])

print "Positive Social Sentiment: " + str(p_s_corr)
print "Negative Social Sentiment: " + str(n_s_corr)
print "Neutral Social Sentiment: " + str(a_s_corr)

p_allcorr = numpy.corrcoef([numpy.add(pInt, p_s_Int), s])
n_allcorr = numpy.corrcoef([numpy.add(nInt, n_s_Int), s])
a_allcorr = numpy.corrcoef([numpy.add(aInt, a_s_Int), s])

print "Positive All Sentiment: " + str(p_allcorr)
print "Negative All Sentiment: " + str(n_allcorr)
print "Neutral All Sentiment: " + str(a_allcorr)

allVolumn = numpy.add(pInt, nInt)
allVolumn = numpy.add(allVolumn, aInt)
allCorr = numpy.corrcoef([allVolumn, s])

print "All Volumn: " + str(allCorr)

pn_ratio = pInt/nInt
print pn_ratio
pnr_corr = numpy.corrcoef([pn_ratio, s])

print "PNR Corr: " + str(pnr_corr)

p_sum = numpy.add(pInt, p_s_Int)
n_sum = numpy.add(nInt, n_s_Int)

print "P_SUM:" + str(p_sum)
print "N_SUM:" + str(n_sum)


beta = 1
alpha = 1

p_sum = pInt*numpy.array(p_s_Int)*beta
n_sum = nInt*numpy.array(n_s_Int)*alpha

pn_sum_ratio = p_sum/n_sum
pnr_sum_corr = numpy.corrcoef([pn_sum_ratio, s])

print "PNR Sum Corr: " + str(pnr_sum_corr)

spearman_r = scit.spearmanr(pn_sum_ratio, s)
print "Spearman's Correlation: " + str(spearman_r)

cross_corr = numpy.correlate(pn_sum_ratio, s)
print cross_corr

testVector = numpy.column_stack((s, pn_ratio))
st.grangercausalitytests(testVector, 8, verbose = True)

testVector = numpy.column_stack((pn_ratio, s))
st.grangercausalitytests(testVector, 8, verbose = True)
