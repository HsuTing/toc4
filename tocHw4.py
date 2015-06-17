#coding:utf-8

"""徐鼎翔"""
"""F74011140"""
"""
"""
import sys
import json
import re

"""main"""
if len(sys.argv) < 3:
	print "input number is not enough."
elif len(sys.argv) > 3:
	print "input number is too much."
else:
	fp = open(sys.argv[1], "r")
	query = sys.argv[2]
	output = {}

	for line in fp:
		content = json.loads(line)

		if query in content["Envelope"]["WARC-Header-Metadata"]["WARC-Target-URI"] and content["Envelope"]["Payload-Metadata"]["HTTP-Response-Metadata"]["HTML-Metadata"].has_key("Links"):
			links = content["Envelope"]["Payload-Metadata"]["HTTP-Response-Metadata"]["HTML-Metadata"]["Links"]

			for i in range(0, len(links)):
				link = ""

				if links[i].has_key("url"):
					link = links[i]["url"]
				elif links[i].has_key("href"):
					link = links[i]["href"]

				linktemp = re.findall("http[s]?://[^" + query + "]", link)
				if len(linktemp) != 0:
					print linktemp[0]
					print link

	fp.close()
