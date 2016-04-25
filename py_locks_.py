import threading
import time

def do_this():
	global x, lock
	print "This is our_thread!!"
	
	lock.acquire()
	try:
		while x < 300:
			x += 1
		print x
	finally:
		lock.release()

def do_after():
	global x, lock
	print "This is new_thread!!"
	
	lock.acquire()
	try:
		x = 400
		while x < 600:
			x += 1
		print x
	finally:
		lock.release()

def main():
	global x, lock
	x = 0
	
	lock = threading.Lock()
	our_thread = threading.Thread(target=do_this, name="other_thread")
	our_thread.start()
	
	new_thread = threading.Thread(target=do_after, name="new_thread")
	new_thread.start()
	
	# time.sleep(.5)
	print "From main thread!!"

if __name__ == "__main__":
	main()