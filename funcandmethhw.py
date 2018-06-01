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