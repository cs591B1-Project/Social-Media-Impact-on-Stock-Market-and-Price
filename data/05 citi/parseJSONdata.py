import json;
import time;
from datetime import datetime, timedelta
from parseJSON import getSocialData

def parseData(negativeFileName, postiveFileName, neutralFileName, numNegativ, numPositive, numNeutral):
	days_back = 30
	date_days_ago = datetime.now() - timedelta(days=days_back)
	day = datetime.today().day
	day = 7

	#  array to track number of positive articles by day
	ap = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	ap_social = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	ap_trump = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	ap_clinton = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	ap_election = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	#  array to track number of positive articles by day
	an = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	an_social = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	an_trump = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	an_clinton = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	an_election = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


	#  array to track number of positive articles by day
	aa = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	aa_social = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	aa_trump = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	aa_clinton = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	aa_election = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	for x in range(1, numNegativ+1):
		fileName = negativeFileName + str(x) + '.json'
		print fileName

		# Negative News Articles from 1 to 9 JSON files
		with open(fileName) as json_data:
		    d = json.load(json_data)

		rn = d["posts"]

		# go through all posts
		for post in rn:
			p = post["published"]
			m = int(p[5:7])
			if m == 11:
				d = int(p[8:10])
			else:
				d = int(p[8:10])+30
			an[d-day] += 1
			social_impact = getSocialData(post)
			an_social[d-day] += social_impact

			# Get text from news object
			text = post["text"]
			text = text.encode('ascii','ignore')
			
			# Search for Trump
			foundindx = text.find("Trump") 
			if foundindx > 0:
				an_trump[d-day] += 1

			# Search for Election
			foundindx = text.find("election") 
			if foundindx > 0:
				an_election[d-day] += 1

			# Search for Election
			foundindx = text.find("Clinton") 
			if foundindx > 0:
				an_clinton[d-day] += 1


	print "Found Trump: " + str(an_trump)
	print "Found Election: " + str(an_election)
	print "Found Election: " + str(an_clinton)

	out0 = open('negative.txt', 'w')
	out0.truncate()
	for i in an:
		out0.write(str(i))
		out0.write("\n")
	out0.close()

	out0 = open('negative_social.txt', 'w')
	out0.truncate()
	for i in an_social:
		out0.write(str(i))
		out0.write("\n")
	out0.close()

	out0 = open('negative_election.txt', 'w')
	out0.truncate()
	for i in an_election:
		out0.write(str(i))
		out0.write("\n")
	out0.close()

	out0 = open('negative_trump.txt', 'w')
	out0.truncate()
	for i in an_trump:
		out0.write(str(i))
		out0.write("\n")
	out0.close()

	out0 = open('negative_clinton.txt', 'w')
	out0.truncate()
	for i in an_clinton:
		out0.write(str(i))
		out0.write("\n")
	out0.close()

	for x in range(1, numNeutral+1):
		fileName = neutralFileName + str(x) + '.json'
		print fileName

		# calculate total number of neutral articles by day
		with open(fileName) as json_data:
		    d = json.load(json_data)

		ra = d["posts"]

		for post in ra:
			p = post["published"]
			m = int(p[5:7])
			if m == 11:
				d = int(p[8:10])
			else:
				d = int(p[8:10])+30
			aa[d-day] += 1
			social_impact = getSocialData(post)
			an_social[d-day] += social_impact

			# Get text from news object
			text = post["text"]
			text = text.encode('ascii','ignore')
			
			# Search for Trump
			foundindx = text.find("Trump") 
			if foundindx > 0:
				aa_trump[d-day] += 1

			# Search for Election
			foundindx = text.find("election") 
			if foundindx > 0:
				aa_election[d-day] += 1

			# Search for Election
			foundindx = text.find("Clinton") 
			if foundindx > 0:
				aa_clinton[d-day] += 1


	print "Found Trump: " + str(aa_trump)
	print "Found Election: " + str(aa_election)
	print "Found Clinton: " + str(aa_clinton)

	out0 = open('all.txt', 'w')
	out0.truncate()
	for i in aa:
		out0.write(str(i))
		out0.write("\n")
	out0.close()

	out0 = open('all_social.txt', 'w')
	out0.truncate()
	for i in aa_social:
		out0.write(str(i))
		out0.write("\n")
	out0.close()

	out0 = open('all_election.txt', 'w')
	out0.truncate()
	for i in aa_election:
		out0.write(str(i))
		out0.write("\n")
	out0.close()

	out0 = open('all_trump.txt', 'w')
	out0.truncate()
	for i in aa_trump:
		out0.write(str(i))
		out0.write("\n")
	out0.close()

	out0 = open('all_clinton.txt', 'w')
	out0.truncate()
	for i in aa_clinton:
		out0.write(str(i))
		out0.write("\n")
	out0.close()

	for x in range(1, numPositive+1):
		fileName = postiveFileName + str(x) + '.json'
		print fileName

		# calculates number of positive articles per day, from the last 30 days
		with open(fileName) as json_data:
		    d = json.load(json_data)

		rp = d["posts"]

		for post in rp:
			p = post["published"]
			m = int(p[5:7])
			if m == 11:
				d = int(p[8:10])
			else:
				d = int(p[8:10])+30
			ap[d-day] += 1
			social_impact = getSocialData(post)
			an_social[d-day] += social_impact

			# Get text from news object
			text = post["text"]
			text = text.encode('ascii','ignore')
			
			# Search for Trump
			foundindx = text.find("Trump") 
			if foundindx > 0:
				ap_trump[d-day] += 1

			# Search for Election
			foundindx = text.find("election") 
			if foundindx > 0:
				ap_election[d-day] += 1

			# Search for Election
			foundindx = text.find("Clinton") 
			if foundindx > 0:
				ap_clinton[d-day] += 1

	print "Found Trump: " + str(ap_trump)
	print "Found Election: " + str(ap_election)
	print "Found Clinton: " + str(ap_clinton)

	out1 = open('positive.txt', 'w')
	out1.truncate()
	for i in ap:
		out1.write(str(i))
		out1.write("\n")
	out1.close()


	out1 = open('positive_social.txt', 'w')
	out1.truncate()
	for i in ap_social:
		out1.write(str(i))
		out1.write("\n")
	out1.close()

	out1 = open('positive_election.txt', 'w')
	out1.truncate()
	for i in ap_election: 
		out1.write(str(i))
		out1.write("\n")
	out1.close()

	out1 = open('positive_trump.txt', 'w')
	out1.truncate()
	for i in ap_trump: 
		out1.write(str(i))
		out1.write("\n")
	out1.close()

	out1 = open('positive_clinton.txt', 'w')
	out1.truncate()
	for i in ap_clinton: 
		out1.write(str(i))
		out1.write("\n")
	out1.close()