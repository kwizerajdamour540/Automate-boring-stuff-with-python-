from pathlib import Path,os
a=open(Path.cwd()/"FIRSTFILE.txt",'r+')
print("unfortunetely we are  gonna write some statement ofcourse you will not see it:")
c='''disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate,awesome!!'''
a.write(c)
a.close()
a=open(Path.cwd()/"FIRSTFILE.txt",encoding='UTF-8')
print("we are gonna read it compeletely:\n")
print(a.read())
a.close()
a=open(Path.cwd()/"FIRSTFILE.txt",'r')
print("we are gonna readit line by line:")
print(a.readlines())
a.close()
