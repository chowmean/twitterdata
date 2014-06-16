from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey='6zSyLNhbmD1O68uNhZtF16ifJ'
csecret='CbI4Ew3t4HLnkpGjBP7YC1Bm31HxTDJ9rQiERyiy37hGSdALyE'
atoken='298398033-jU0Q9NvuD2B0cmkiX97zgzoVig1Q3tgIgFSmj5Vx'
asecret='mG6uiNPzu91V2I6KTCInm8Mh6NKorzGw5od4TNXknVd0f'

class listener(StreamListener):
	def on_data(self,data):
		print data
		return True
	def on_error(self,status):
		print status

auth = OAuthHandler(ckey,csecret)

auth.set_access_token(atoken,asecret)

twitterStream =Stream(auth,listener())
twitterStream.filter(track=["fifa"])

