import threading

def do_this():
	global x
	print "This is our_thread!!"
	while x < 300:
		x += 1
	if x == 300:
		print x

def main():
	global x
	x = 0
	main_thread = threading.enumerate()[0]
	print main_thread.isDaemon()
	our_thread = threading.Thread(target=do_this, name="other_thread")
	# our_thread.setDaemon(True)
	our_thread.start()
	print our_thread.isDaemon()

if __name__ == "__main__":
	main()