def multiply(numbers):
	total = 1
	for i in numbers:
		total = total * i
	return total

print(multiply([1,2,3,-4]))