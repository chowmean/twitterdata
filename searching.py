import oauth2
import time
import urllib2
import json

url1 = "https://api.twitter.com/1.1/search/tweets.json"
params = {
	"oauth_version": "1.0",
	"oauth_nonce": oauth2.generate_nonce(),
	"oauth_timestamp": int(time.time())
}


consumer_key='6zSyLNhbmD1O68uNhZtF16ifJ'
consumer_secret='CbI4Ew3t4HLnkpGjBP7YC1Bm31HxTDJ9rQiERyiy37hGSdALyE'
access_token='298398033-jU0Q9NvuD2B0cmkiX97zgzoVig1Q3tgIgFSmj5Vx'
access_secret='mG6uiNPzu91V2I6KTCInm8Mh6NKorzGw5od4TNXknVd0f'


consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)
token = oauth2.Token(key=access_token, secret=access_secret)
params["oauth_consumer_key"] = consumer.key
params["oauth_token"] = token.key

prev_id = int("435458631669415936")

for i in range(1):
	url = url1
	params["q"] = "fifa"
	params["count"] = 15
#	params["geocode"] = ""
#	params["lang"] = "English"
	params["locale"] = "en"
	params["result_type"] = "popular" # Example Values: mixed, recent, popular
#	params["until"] = ""
#	params["since_id"] = ""

#	params["max_id"] = str(prev_id)
	req=oauth2.Request(method="GET",url=url,parameters=params)
	signature_method=oauth2.SignatureMethod_HMAC_SHA1()
	req.sign_request(signature_method,consumer,token)
	headers=req.to_header()
	url=req.to_url()
#	print headers
#	print url
	response=urllib2.Request(url)
	data=json.load(urllib2.urlopen(response))
	if data["statuses"] == []:
		print "end of data"
		break
	else:
		prev_id = int(data["statuses"][-1]["id"]) - 1
		print prev_id, i
	print data["statuses"]
	f = open("outfile_" + str(i) + ".txt", "w")
	json.dump(data["statuses"], f)
	f.close()
	time.sleep(5)
