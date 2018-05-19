st = 'Print only the words that start with s in this sentence'
words = st.split()
for word in words:
	if word[0] in 's':
		print(word)

print(list(range(0,11,2)))
#or
for num in range(0,11,2):
	print(num)

mylist = [num for num in range(0,51) if num%3 == 0]
print(mylist)

st = 'Print every word in this sentence that has an even number of letters'
words = st.split()
for even in words:
	if len(even)%2 == 0:
		print(even)

#Write a program that prints the integers from 1 to 100. 
#But for multiples of three print "Fizz" instead of the number, 
#and for the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".


for num in range(1,101):
	if num%5 == 0 and num%3 == 0:
		print('FizzBuzz')
	elif num%3 == 0:
		print('Fizz')
	elif num%5 ==0:
		print('Buzz')
	else:
		print(num)



