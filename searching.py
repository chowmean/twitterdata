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

prev_id = int("INSERT BEGINNING TWITTER ID")

for i in range(1):
	url = url1
	params["q"] = "INSERT SEARCH QUERY"
	params["count"] = INSERT INTEGER FROM 1 TO 100
	params["geocode"] = ""
	params["lang"] = ""
	params["locale"] = ""
	params["result_type"] = "" # Example Values: mixed, recent, popular
	params["until"] = ""
	params["since_id"] = ""
	params["max_id"] = str(prev_id)
	if data["statuses"] == []:
		print "end of data"
		break
	else:
		prev_id = int(data["statuses"][-1]["id"]) - 1
		print prev_id, i
	f = open("outfile_" + str(i) + ".txt", "w")
	json.dump(data["statuses"], f)
	f.close()
	time.sleep(5)