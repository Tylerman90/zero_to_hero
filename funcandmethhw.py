import math
def vol(rad):
	volume = (4/3)*(math.pi)*(rad**3)
	return volume

print (vol(8))

def ran_check(num,low,high):
	if num >= low and num <= high:
		return f"{num} is in the range between {low} and {high}!"
	else:
		return f"{num} is not in the range between {low} and {high}."

print(ran_check(5,2,4))

def up_low(s):
	u = 0
	l = 0
	for letter in s:
		if letter.isupper():
			u += 1
		elif letter.islower():
			l += 1
	print("Original String: ", s)
	print(f'No. of Upper case Characters : {u}')
	print(f'No. of Lower case Characters : {l}')

up_low('Hello People')
 


def unique_list(lst):
	my_list = []
	for item in lst:
		if item not in my_list:
			my_list.append(item)
	return my_list

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))



def multiply(numbers):
	sum = 1
	for i in numbers:
		newsum == sum * i
	return newsum

print multiply([1,2,3,-4])







