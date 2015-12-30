import requests
import json
from wget import download
  
def buildSentReq(text, api_key):
	return 'https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?text=' + text + '&apikey=' + api_key

# request JSON data for Sentiment
reqSent = requests.post(buildSentReq('I love the glorious feeling of marinating myself in juice and imagining the possibilities of life as a meatball', '7b54e31e-f0bb-4b91-9ccf-bea208ecf4b4'))
jsonSent = json.loads(reqSent.content)

print jsonSent['aggregate']['score']