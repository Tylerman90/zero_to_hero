def lesser_of_two_evens(a,b):
	if a%2 == 0 and b%2 == 0:
		if a > b:
			print(b)
		else:
			print(a)
	elif a%3 == 0 or b%3 == 0:
		if a > b:
			print(a)
		else:
			print(b)
	else:
		print("Come on! Why do you have to make everything so complicated!")

lesser_of_two_evens(4,2)

def animal_crackers