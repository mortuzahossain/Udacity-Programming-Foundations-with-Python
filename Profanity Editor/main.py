import urllib

def main():
	quotes = open('movie_quotes.txt')
	content_of_file = quotes.read()
	print checkProdanity(content_of_file)
	quotes.close()

def checkProdanity(text_to_check):
	connection = urllib.urlopen('http://www.wdylike.appspot.com/?q='+text_to_check)
	output = connection.read()
	connection.close()
	# For Better output
	if 'true' in output:
		output = 'Prodanity Aleart.'
	elif 'false' in output:
		output = 'This Document is clean.'
	else:
		output = 'Can not scan the doc please try again.'
	return output

if __name__ == '__main__':
	main()
