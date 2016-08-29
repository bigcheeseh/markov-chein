import urllib2

response = urllib2.urlopen('http://gutenberg.org/')
html = response.read()

with open("html.txt", "r+")  as textfile:
	text = textfile.read()
	if text == '': 
		textfile.write(html)
		print 'Html captured'
	else:
		textfile.seek(0)
		textfile.truncate()
		print 'Now file is empty and you can capture html'