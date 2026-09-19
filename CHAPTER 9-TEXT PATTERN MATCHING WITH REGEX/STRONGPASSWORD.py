import re
def is_strong_password(password):
	obj1=re.compile(r'\d')
	obj2=re.compile(r'[A-Z]')
	obj3=re.compile(r'[a-z]')
	obj4=re.compile(r'[^A-Za-z0-9\s]')
	c=password
	d=0
	if len(c)>=8:
			print("it has at least 8 character")
			d+=1
			if obj1.search(c)!=None:
				print("it has also digit")
				d+=1
				if obj2.search(c)!=None:
					print("it has also at least one upper case character")
					d+=1
					if obj3.search(c)!=None:
						print("it has also at least one lowercase character")
						d+=1
						if obj4.search(c)!=None:
							print("it has also at least one symbol")
							d+=1

	if d==5:
		print("awesome your password is strong!!")
	else:
		print("your password is weak")
your=input("enter your password:")
is_strong_password(your)