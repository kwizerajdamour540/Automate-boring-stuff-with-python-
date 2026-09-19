import re
import sys

print("we gonna make account:")
f_name=input("enter your first name:")
s_name=input("enter sur name:")
number=int(input("enter phone number e.g:07....:"))
password=input("enter strong password:")
cin=int(input("press \n 1.to login into your accout\n2.to quit app"))
while True:
	if cin==1:
		lfn=input("enter first name:")
		lsn=input("enter surname name:")
		ln=int(input("enter phone number :"))
		lp=input("enter your password:")
		obj1=re.compile(r"^f_name:{lfn} s_name:{lsn} number:{ln} password:{lp}$")
		login=obj1.fullmatch(f'f_name:{lfn} s_name: {lsn} number:{ln} password:{lp}')
		if login is not None:
			print("awesome login succesful")
			break
		else:
			print(" identity mismatch please try again ")
			
	else:
		print("good bye")
		sys.exit()

