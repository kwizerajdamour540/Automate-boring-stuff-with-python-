import math

def coordinate(a,b):
	x=a[0]+b[0]
	y=a[1]+b[1]
	u=math.pow(x,2)+math.pow(y,2)
	return math.sqrt(u)


o=int(input("enter first point (x1,):"))

p=int(input("enter first point(,y1):"))

q=int(input("enter second  point (x2,):"))

r=int(input("enter second  point (,y2):"))

c1=(o,p)
c2=(q,r)

z=coordinate(c1,c2)

print (f"the distance btn point {c1} and {c2} is {z}")
