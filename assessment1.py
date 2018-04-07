#write a brief description of all the
#following Object Types and Data Structures
#we've learned about:

#Numbers: integers in python that can be
#used in math, variable names, strings
#or to count.

#Strings: words, numbers or symbols that
#are stored between quotes that are typically
#used as output for the user to read, or for
#the programmer to debug. Often used in
#conjunction with print statements.

#Lists: are sets of values that can be stored
#and called upon to store and analyze information.

#Tuples: sets of  keys and corresponding 
#values that can be stored. However, these 
#values cannot be changed once stored; they
#are immutable.

#Dictionaries: sets of keys and values that
#can be stored and called upon. These keys
#and values are mutable.



#Write an equation that uses multiplication,
#division, an exponent, addition, and 
#subtraction that is equal to 100.25.
x = (((((5 * 4) / 2) ** 2) + .50) - .25)
print (x)

a = 4 * (6 + 5)
#44
print (a)
b = 4 * 6 + 5
#29
print (b)
c = 4 + 6 * 5
#34
print(c)

#What is the type of the result of the 
#expression 3 + 1.5 + 4?
# = floating integer

#to find square root you use
# 2 ** (0.5)
#to find square you use
# 2 ** 2

#STRINGS
#Given the string 'hello' give an index 
#command that returns 'e'.
s = 'hello'
print(s[1])

#Reverse the string 'hello' using slicing:
print(s[::-1])

#Given the string hello, give two methods
#of producing the letter 'o' using indexing.
print(s[-1])
print(s[4])


#LISTS
#Build this list [0,0,0] two separate ways.
my_list = [0,0,0]
print(my_list)
a_list = [0,0]
a_list.append(0)
print(a_list)

#Reassign 'hello' in this nested list to 
#say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3)

#Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()
print(list4)




























