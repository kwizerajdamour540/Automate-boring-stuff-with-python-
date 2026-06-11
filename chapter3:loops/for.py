#for loop to summ add number btn entered range

while True:

	x=int(input("enter starting point !remember add:"))
	if (x%2==1):
	 break
	else:
	 
	 continue
while True:
	y=int(input("enter ending point!remeber odd"))
	if (y%2==1):
	 break
	else:
	 continue
sum=0
for i in range(x,y):
	if(i%2==1):
	 sum+=i
print (f"sum of odd between {x} and {y} is equal {sum}")

