#computaton of lowest common multiple
def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    return abs(a * b) // gcd(a, b)

while True:
	try:
	 x=int(input("enter number 1:")) 
	 y=int(input("enter number 2:"))
	 break
	except:
	 print ("enter integer please")
z=lcm(x,y)
print (f"the LCM of {x}  and  {y} is :{z}")

