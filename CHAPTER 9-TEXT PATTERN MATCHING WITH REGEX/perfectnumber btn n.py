number=int(input("enter  starting number:"))
end=int(input("enter ending point:"))
z=[]
for i in range(number,end+1):
	c=0
	for j in range(1,i+1):
		if (i%j==0):
			c+=1
	if (c==2):
		z.append(i)
print(f"perfect number between {number} and {end} is :{z}")
 
