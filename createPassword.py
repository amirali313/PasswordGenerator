import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
special = string.punctuation



def mkPassword(l , A):
	#return ''.join(random.choice(A) for _ in range(0,l))
	stri = ''
	for i in range(0,l):
		stri += random.choice(A)
	return stri


def createPassword(num):
	assert num > 3 , "error"
	password = ''
	for i in range(num):
		password += mkPassword(1 , lower)
		password += mkPassword(1 , upper)
		password += mkPassword(1 , number)
		password += mkPassword(1 , special)

	password = mkPassword(num , password)
		
	#return password[:len(password)/4]
	return password
		




num = 10
print(createPassword(num))
#for i in range(1, 50):
#	try:
#		print(createPassword(i))
#	except AssertionError as e :
#		print("Error : " + e.args[0])
