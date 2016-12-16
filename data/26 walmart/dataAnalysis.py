import numpy
from numpy import *
from operator import truediv
from ast import literal_eval
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as st
import scipy.stats as scit


def calCorrelation(s,v):

	# STEP 1: Read all data files 
	p = [line.rstrip('\n') for line in open("positive.txt")]
	n = [line.rstrip('\n') for line in open("negative.txt")]
	a = [line.rstrip('\n') for line in open("all.txt")]

	p_social = [line.rstrip('\n') for line in open("positive_social.txt")]
	n_social = [line.rstrip('\n') for line in open("negative_social.txt")]
	a_social = [line.rstrip('\n') for line in open("all_social.txt")]

	p_election = [line.rstrip('\n') for line in open("positive_election.txt")]
	n_election = [line.rstrip('\n') for line in open("negative_election.txt")]
	a_election = [line.rstrip('\n') for line in open("all_election.txt")]

	p_trump = [line.rstrip('\n') for line in open("positive_trump.txt")]
	n_trump = [line.rstrip('\n') for line in open("negative_trump.txt")]
	a_trump = [line.rstrip('\n') for line in open("all_trump.txt")]

	p_clinton = [line.rstrip('\n') for line in open("positive_clinton.txt")]
	n_clinton = [line.rstrip('\n') for line in open("negative_clinton.txt")]
	a_clinton = [line.rstrip('\n') for line in open("all_clinton.txt")]

	# STEP 2: Convert into numpy.array and float + bias of 1 for 0 data to avoid divided by 0 erro
	pInt = numpy.array(map(float, p))+1
	nInt = numpy.array(map(float, n))+1
	aInt = numpy.array(map(float, a))+1

	p_s_Int = numpy.array(map(float, p_social))+1
	n_s_Int = numpy.array(map(float, n_social))+1
	a_s_Int = numpy.array(map(float, a_social))+1

	p_elec = numpy.array(map(float, p_election))+1
	n_elec = numpy.array(map(float, n_election))+1
	a_elec = numpy.array(map(float, a_election))+1

	p_tr = numpy.array(map(float, p_trump))+1
	n_tr = numpy.array(map(float, n_trump))+1
	a_tr = numpy.array(map(float, a_trump))+1

	p_hc = numpy.array(map(float, p_clinton))+1
	n_hc = numpy.array(map(float, n_clinton))+1
	a_hc = numpy.array(map(float, a_clinton))+1

	# STEP 3: Grab only 30 data since those are only needed for samples to calculate correlation
	pInt = pInt[0:30]
	nInt = nInt[0:30]
	aInt = aInt[0:30]

	p_s_Int = p_s_Int[0:30]
	n_s_Int = n_s_Int[0:30]
	a_s_Int = a_s_Int[0:30]

	p_elec = p_elec[0:30]
	n_elec = n_elec[0:30]
	a_elec = a_elec[0:30]

	p_tr = p_tr[0:30]
	n_tr = n_tr[0:30]
	a_tr = a_tr[0:30]

	p_hc = p_hc[0:30]
	n_hc = n_hc[0:30]
	a_hc = a_hc[0:30]

	print n_tr
	print p_tr
	print a_tr

	print n_elec
	print p_elec
	print a_elec

	# STEP 4: Simple Correlation of Data against Stock Market Prices
	p_corr = numpy.corrcoef([pInt, s])
	n_corr = numpy.corrcoef([nInt, s])
	a_corr = numpy.corrcoef([aInt, s])

	print "Positive Sentiment Corr: " + str(p_corr)
	print "Negative Sentiment Corr: " + str(n_corr)
	print "Neutral Sentiment Corr: " + str(a_corr)

	cross_corr = numpy.correlate(pInt, s)
	print cross_corr

	# STEP 5: Simple Correlation of Social Medica Data against Stock Market Prices
	p_s_corr = numpy.corrcoef([p_s_Int, s])
	n_s_corr = numpy.corrcoef([n_s_Int, s])
	a_s_corr = numpy.corrcoef([a_s_Int, s])

	print "Positive Social Sentiment Corr: " + str(p_s_corr)
	print "Negative Social Sentiment Corr: " + str(n_s_corr)
	print "Neutral Social Sentiment Corr: " + str(a_s_corr)

	# above caculation does not tell us much

	# STEP 6: Sentiment with Social Medica Factor Corr
	p_allcorr = numpy.corrcoef([numpy.add(pInt, p_s_Int), s])
	n_allcorr = numpy.corrcoef([numpy.add(nInt, n_s_Int), s])
	a_allcorr = numpy.corrcoef([numpy.add(aInt, a_s_Int), s])

	print "Positive Articles + Social Sentiment Corr: " + str(p_allcorr)
	print "Negative Articles + Sentiment Corr: " + str(n_allcorr)
	print "Neutral Articles + Sentiment Corr: " + str(a_allcorr)


	# STEP 7: Volumn & News Article Correlation
	p_v_corr = numpy.corrcoef([pInt, v])
	n_v_corr = numpy.corrcoef([nInt, v])
	a_v_corr = numpy.corrcoef([aInt, v])

	print "Positive Articles Sentiment - Volume Corr: " + str(p_v_corr)
	print "Negative Sentiment - Volume Corr: " + str(n_v_corr)
	print "Neutral Sentiment - Volume Corr: " + str(a_v_corr)

	# with social media
	p_all_v_corr = numpy.corrcoef([numpy.add(pInt, p_s_Int), v])
	n_all_v_corr = numpy.corrcoef([numpy.add(nInt, n_s_Int), v])
	a_all_v_corr = numpy.corrcoef([numpy.add(aInt, a_s_Int), v])

	print "Positive Articles + Social Sentiment Corr: " + str(p_all_v_corr)
	print "Negative Articles + Sentiment Corr: " + str(n_all_v_corr)
	print "Neutral Articles + Sentiment Corr: " + str(a_all_v_corr)

	pn_ratio = pInt/nInt
	print pn_ratio
	pnr_corr = numpy.corrcoef([pn_ratio, s])

	print "PNR Corr: " + str(pnr_corr)



	tr_corr = numpy.corrcoef([n_tr+p_tr+a_tr, s])
	print tr_corr

	elec_corr = numpy.corrcoef([n_elec + p_elec + a_elec, s])
	print elec_corr

	n_elec_corr = numpy.corrcoef([n_elec, s])
	print n_elec_corr



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


#spearman_r = scit.spearmanr(pn_sum_ratio, s)
#print "Spearman's Correlation: " + str(spearman_r)

#cross_corr = numpy.correlate(pn_sum_ratio, s)
#print cross_corr
	print "Null Hypothesis - Postive Sentiment does not cause stock market price"
	testVector = numpy.column_stack((s, pInt))
	st.grangercausalitytests(testVector, 8, verbose = True)

	print "Null Hypothesis - Negative Sentiment does not cause stock market price"
	testVector = numpy.column_stack((s, nInt))
	st.grangercausalitytests(testVector, 8, verbose = True)

	print "Null Hypothesis - Neutral Sentiment does not cause stock market price"
	testVector = numpy.column_stack((s, aInt))
	st.grangercausalitytests(testVector, 8, verbose = True)

	testVector = numpy.column_stack((s, pn_ratio))
	st.grangercausalitytests(testVector, 8, verbose = True)

	testVector = numpy.column_stack((pn_ratio, s))
	st.grangercausalitytests(testVector, 8, verbose = True)
