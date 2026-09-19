import re,os
count=0
failed=[]
with open("aut.log",'r+') as data:
	for line in data:
		if "login failed" in line:
			failed.append(line)
			count+=1

with open("faied_log.txt",'a') as save:
	for f in failed:
		save.write(f)
with open("faied_log.txt",'a') as sav:
		sav.write(f"number of ligin failed is:{count}")
