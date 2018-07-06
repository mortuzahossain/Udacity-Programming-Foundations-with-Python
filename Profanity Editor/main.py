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
	return output

if __name__ == '__main__':
	main()
