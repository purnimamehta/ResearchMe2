import datetime as dt
import json, sys
from apiclient.discovery import build
import urllib2

#-----------Michael-----------#
from HTMLParser import HTMLParser, HTMLParseError
from htmlentitydefs import name2codepoint
import re
import binascii

import requests
import json
from wget import download

resume = {"cover_letter":"I love the glorious feeling of marinating myself in juice and imagining the possibilities of life as a meatball","first_name":"Michael","last_name":"O'Connell","city":"Toronto","skills":"None"}
magic_list = {"michael":3}
score = 0

def buildSentReq(text, api_key):
	return 'https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?text=' + text + '&apikey=' + api_key

class _HTMLToText(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._buf = []
        self.hide_output = False

    def handle_starttag(self, tag, attrs):
        if tag in ('p', 'br') and not self.hide_output:
            self._buf.append('\n')
        elif tag in ('script', 'style'):
            self.hide_output = True

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self._buf.append('\n')

    def handle_endtag(self, tag):
        if tag == 'p':
            self._buf.append('\n')
        elif tag in ('script', 'style'):
            self.hide_output = False

    def handle_data(self, text):
        if text and not self.hide_output:
            self._buf.append(re.sub(r'\s+', ' ', text))

    def handle_entityref(self, name):
        if name in name2codepoint and not self.hide_output:
            c = unichr(name2codepoint[name])
            self._buf.append(c)

    def handle_charref(self, name):
        if not self.hide_output:
            n = int(name[1:], 16) if name.startswith('x') else int(name)
            self._buf.append(unichr(n))

    def get_text(self):
        return re.sub(r' +', ' ', ''.join(self._buf))


#-----------Qile-----------#
if __name__ == '__main__':
    # Create an output file name in the format "srch_res_yyyyMMdd_hhmmss.json"
    now_sfx = dt.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = './output/'
    output_fname = output_dir + 'srch_res_' + now_sfx + '.json'
    #-----------Michael-----------#
    search_term = resume["first_name"] + " " + resume["last_name"] + " " + resume["city"] #search_term = sys.argv[1]

    #-----------Qile-----------#
    # Key codes we created earlier for the Google CustomSearch API
    search_engine_id = '000189178235351906276:4wq155moutq'
    api_key = 'AIzaSyBk4Ad294hf10qqnbexaDDC6fZehy5qmOM'
    
    # The build function creates a service object. It takes an API name and API 
    # version as arguments. 
    service = build('customsearch', 'v1', developerKey=api_key)
    # A collection is a set of resources. We know this one is called "cse"
    # because the CustomSearch API page tells us cse "Returns the cse Resource".
    collection = service.cse()

    sites = 10

    output_f = open(output_fname, 'ab')

    # Make an HTTP request object
    request = collection.list(q=search_term,
        num=sites, #this is the maximum & default anyway
        start=1,
        cx=search_engine_id
    )
    response = request.execute()
    output = json.dumps(response, sort_keys=True, indent=2)
    output_f.write(output)
    print('Wrote 5 search results...')

    output_f.close()
    print('Output file "{}" written.'.format(output_fname))

    #-----------Michael-----------#
    f = open(output_fname, "r")
    parsed_file = json.loads(f.read())
    full_resume = ("\n".join(resume.values())).lower()
    for i in range(sites):
    	if "linkedin" not in parsed_file["items"][i]["link"]:
	    	web_file = urllib2.urlopen(parsed_file["items"][i]["link"])
	    	print("\"" + parsed_file["items"][i]["link"] + "\" crawled...")
	    	raw_web_data = web_file.read()
	    	parser = _HTMLToText()
	    	try:
	    		parser.feed(binascii.b2a_qp(raw_web_data))
	    		parser.close()
	    	except HTMLParseError:
	    		pass
	    	web_data = parser.get_text().lower()
	    	for word in magic_list.keys():
	    		count = web_data.count(word)
	    		if count > 0:
	    			score += magic_list[word] * 2 * count
		else:sites -= 1
    for word in magic_list.keys():
    	rCount = full_resume.count(word)
    	if rCount > 0:score += magic_list[word] * rCount
	print("Score is: " + str(round(score/sites,1)))
    # request JSON data for Sentiment
	reqSent = requests.post(buildSentReq(resume["cover_letter"], '7b54e31e-f0bb-4b91-9ccf-bea208ecf4b4'))
	jsonSent = json.loads(reqSent.content)
	print(round(10 * jsonSent['aggregate']['score'], 1))






















