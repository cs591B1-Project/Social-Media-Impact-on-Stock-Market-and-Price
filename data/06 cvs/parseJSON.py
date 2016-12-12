
def getSocialData(post):
	# Get Thread Object
	threadObject	= post["thread"]
	
	domain_rank 	= threadObject["domain_rank"]	#domain_rank
	#print 'domain_rank:' + str(domain_rank)

	socialObject	= threadObject["social"]		#social data object
	facebookData 	= socialObject["facebook"]		#facebook data
	#print 'facebook data:' + str(facebookData["likes"]) + ', ' + str(facebookData["comments"]) + ', ' + str(facebookData["shares"])
	
	fb_likes = facebookData["likes"]
	fb_comments = facebookData["comments"] 
	fb_shares =  facebookData["shares"]

	gplusData 		= socialObject["gplus"]			#gplus data
	#print 'gplus data:' + str(gplusData["shares"])
	g_shares = gplusData["shares"]

	pinterestData 	= socialObject["pinterest"]		#pinterest data
	#print 'pinterest data:' + str(pinterestData["shares"])
	pin_shares = pinterestData["shares"]

	linkedinData 	= socialObject["linkedin"]		#linkedin data
	#print 'linked data:' + str(linkedinData["shares"])
	linkedin_shares = linkedinData["shares"]

	stumbleduponData= socialObject["stumbledupon"]
	#print 'lstumbleduponData:' + str(stumbleduponData["shares"])
	su_shares = stumbleduponData["shares"]

	vkData			= socialObject["vk"]
	#print 'vkData:' + str(vkData["shares"])
	vk_shares = vkData["shares"]

	social_impact = (fb_likes + fb_comments + fb_shares + g_shares + pin_shares + linkedin_shares + su_shares + vk_shares)
	#print str(social_impact)

	return social_impact