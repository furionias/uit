import random
import threading

def password_generator():
   lower = "abcdefghijklmnopqrstuvwxyz"
   upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   numbers = "0123456789"
   symbols = "!'£$%^&*()_-+=:;@#~?/><.,¬`"
   all_1 = lower + upper + symbols + numbers
   length = random.randrange(1, 100)
   result = "".join(random.sample(all_1, length))
   while True:
   	  print(result)

password_generator()
threads = []
for i in range(120):
	t = threading.Thread(target=password_generator)
	t.start
	threads.append(t)

for thread in threads:
	thread.join()



password_generator()