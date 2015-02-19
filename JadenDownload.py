import twitter
import json

CONSUMER_KEY = 'XXX'
CONSUMER_SECRET = 'XXX'
OAUTH_TOKEN = 'XXX'
OAUTH_TOKEN_SECRET = 'XXX'

target = 'officialjaden'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

t = twitter.Twitter(auth=auth)

since = 1
statuses = t.statuses.user_timeline(screen_name=target, contributor_details=False, 
	trim_user=True, count = 200, include_rts=False)

with open('jadentweets.json', 'w') as outfile:
	json.dump(statuses, outfile)