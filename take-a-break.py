import webbrowser
import time

def OpenWebsite():
	# Open A Website in new tab
	webbrowser.open('http://google.com', new=2)
	print "Done Opening URL."

def StopBreak():
	print 'Done Break. Start Working Again.'

def main():
	for i in xrange(3):
	    time.sleep(1*60) # In Second
	    OpenWebsite()

	    # End Break
	    time.sleep(1*60)
	    StopBreak()

if __name__ == '__main__':
	main()


