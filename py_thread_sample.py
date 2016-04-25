import threading
import time

def do_this():
	global dead
	x = 0
	print "This is our thread!!"
	
	while not dead:
		x += 1

	print x

def main():
	global dead
	dead = False
	
	our_thread = threading.Thread(target=do_this, name="Dipankar Thread")
	our_thread.start()
	
	print threading.active_count()
	print threading.enumerate()
	print threading.current_thread()
	
	print our_thread.is_alive()
	
	raw_input("Hit enter to stop other thread.")
	dead = True
	
	time.sleep(1)
	print our_thread.is_alive()

if __name__ == "__main__":
	main()