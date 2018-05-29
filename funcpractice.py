def lesser_of_two_evens(a,b):
	if a%2 == 0 and b%2 == 0:
		if a > b:
			return(b)
		else:
			return(a)
	elif a%3 == 0 or b%3 == 0:
		if a > b:
			return(a)
		else:
			return(b)
	else:
		print("Come on! Why do you have to make everything so complicated!")


def animal_crackers(words):
	two_words = words.lower().split()
	return two_words[0][0] == two_words[1][0]
		
print(animal_crackers('Crazy Kangaroo'))


def makes_twenty(n1,n2):
	if n1 + n2 == 20 or n1 == 20 or n2 == 20:
		return True
	else:
		return False
print(makes_twenty(2,3))
 

def old_macdonald(name):
	new = name.split()
	return (new[0][0].capitalize() + new[0][1:3] + new[0][3].capitalize() + new[0][4:])
print(old_macdonald('macdonald'))


def master_yoda(text):
	yoda = " ".join(reversed(text.split()))
	return yoda
print(master_yoda('I am great'))


def almost_there(n):
	if n>=90 and n<=110 or n>=190 and n<=210:
		return True
	else:
		return False

def has_33(nums):
	for i in range(0,len(nums) - 1):
		if nums[i] == 3 and nums[i + 1] == 3:
			return True
	return False

print(has_33([1, 3, 3]))



def paper_doll(text):
	result = ' '

	for char in text:
		result += char * 3
	return result

print(paper_doll('Hello'))

def blackjack(a,b,c):
	pass

























