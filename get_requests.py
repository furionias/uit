

import requests
import threading


def find_requests():#function that gets requests from website

	i = input("Enter website url:")
	k = requests.get(i, 2)
	print(k)

find_requests()