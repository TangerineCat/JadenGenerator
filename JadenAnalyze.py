import json
from pymarkovchain import MarkovChain
import re

filename = 'jadentweets.json'
statuses = json.loads(open(filename).read())

tweets = []

for tweet in statuses:
	tweets.append(tweet['text'].encode('ascii','ignore'))

longstring = ''
for tweet in tweets:
	if len(tweet)>1:
		insert = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet)
		longstring = longstring + "\n" + insert

mc = MarkovChain()
mc.generateDatabase(longstring, sentenceSep='[\n]')
for x in xrange(1,10):
	print(mc.generateString())