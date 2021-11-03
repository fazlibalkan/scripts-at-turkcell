import threading

# global variable x
x = 0

def thread_task(lock):
	global x
	for _ in range(100000):
		lock.acquire()
		x += 1
		lock.release()

def main():
	global x
	x = 0

	lock = threading.Lock()

	# creating threads
	t1 = threading.Thread(target=thread_task, args=(lock,))
	t2 = threading.Thread(target=thread_task, args=(lock,))

	# starting threads
	t1.start()
	t2.start()

	# waiting until threads finish their job
	t1.join()
	t2.join()


for i in range(8):
	main()
	print("Iteration " + str(i) + ": " + str(x))
