import threading
import time
import random


def get_value():
	while True:
	 p =  random.randrange(1, 1000000)
	
	 print(p)

get_value()

threads = []
for i in range(1220):
	t = threading.Thread(target=get_value)
	threads.append(t)

for i in range(10):
	threads[i].start()

for i in range(10):
	threads[i].join()