#coding:utf-8

"""徐鼎翔"""
"""F74011140"""
"""
	First check input is enough(must have two input), and open file.
	Then read every line in file, check if it has "Links", and find url in "url" or "href".
	But if query in url or (xxx).(xxx) is not between "/" and "?", remove this url.
	Finally, count every type in url, and print it.
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
	check = False

	for line in fp:
		content = json.loads(line)
		if query in content["Envelope"]["WARC-Header-Metadata"]["WARC-Target-URI"]:
			check = True

		if query in content["Envelope"]["WARC-Header-Metadata"]["WARC-Target-URI"] and content["Envelope"]["Payload-Metadata"]["HTTP-Response-Metadata"]["HTML-Metadata"].has_key("Links"):
			links = content["Envelope"]["Payload-Metadata"]["HTTP-Response-Metadata"]["HTML-Metadata"]["Links"]

			for i in range(0, len(links)):
				link = ""
				if links[i].has_key("url"):
					link = links[i]["url"]
				elif links[i].has_key("href"):
					link = links[i]["href"]

				if query in link:
					continue

				link = re.findall("http[s]?://(?:.+\/)+.+\..+", link)
				if len(link) != 0:
					link = re.split("[\?]", link[ len(link) - 1 ])
					link = re.split(".+\.", link[0])

					if link[1] in output:
						output[ link[1] ] = output[ link[1] ] + 1
					else:
						output[ link[1] ] = 1

	if check:
		if len(output) != 0:
			for item in output:
				print item + ":" + str(output[item])
		else:
			print "Type not found!"
	else:
		print "Page not found!"

	fp.close()
