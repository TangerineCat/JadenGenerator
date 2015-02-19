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
	trim_user=True, count = 200, include_rts=False, exclude_replies = True)

newid = statuses[-1]['id']
lastid = newid+1000000000

while lastid > newid:
	print(newid)
	lastid = newid
	new_statuses = t.statuses.user_timeline(screen_name=target, contributor_details=False, 
		trim_user=True, count = 200, include_rts=False, exclude_replies = True, max_id = lastid)
	try:
		newid = new_statuses[-1]['id']
		statuses += new_statuses
	except:
		print('reached end. what do?')
		print(new_statuses)
		break;

texts = []
for status in statuses:
	dick = {}
	dick['text'] = status['text']
	texts.append(dick)


with open('jadentweets.json', 'w') as outfile:
	json.dump(texts, outfile)