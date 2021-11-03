import threading

# global variable x
x = 0

def thread_task():
	global x
	for _ in range(100000):
		x += 1

def main():
	global x
	x = 0

	# creating threads
	t1 = threading.Thread(target=thread_task)
	t2 = threading.Thread(target=thread_task)

	# starting threads
	t1.start()
	t2.start()

	# waiting until threads finish their job
	t1.join()
	t2.join()


for i in range(8):
	main()
	print("Iteration " + str(i) + ": " + str(x))
