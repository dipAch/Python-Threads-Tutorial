import threading
import time

def do_this():
	global x
	print "This is our_thread!!"
	while x < 300:
		x += 1
	if x == 300:
		print x

def do_after():
	global x
	x = 400
	print "This is new_thread!!"
	while x < 600:
		x += 1
	print x

def main():
	global x
	x = 0
	our_thread = threading.Thread(target=do_this, name="other_thread")
	our_thread.start()
	
	print our_thread.ident
	our_thread.join()
	print our_thread.ident
	
	new_thread = threading.Thread(target=do_after, name="new_thread")
	new_thread.start()
	
	print new_thread.ident
	
	# time.sleep(.5)
	print "From main thread!!"
	
	print new_thread.ident

if __name__ == "__main__":
	main()