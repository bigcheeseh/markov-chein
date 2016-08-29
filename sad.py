import urllib2

response = urllib2.urlopen('https://www.gutenberg.org/files/135/135-h/135-h.htm')
html = response.read()

sad = 0

split_of_words = html.split(' ')

for word in split_of_words:
	word = word.lower()
	if word == 'sad':
		sad += 1

print sad

with open('sadbook.txt', 'r+') as sadbook:
	if sad > 50:
		sadbook.write('very sad book')
	else:
		sadbook.write('not very sad')			