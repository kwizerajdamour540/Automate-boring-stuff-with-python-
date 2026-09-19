import re
try:
	number=input("enter rwanda telephone number eg 07....:")
except:
	print("enter string please")
obj=re.compile(r'\d{10}')
d1=obj.findall(f"my number is {number}")
match=re.search(r"^-\d{2}",d1)
if match.group()[0:2]=="07":
	print("rwandan number")
else:
	print("not rwandan number")