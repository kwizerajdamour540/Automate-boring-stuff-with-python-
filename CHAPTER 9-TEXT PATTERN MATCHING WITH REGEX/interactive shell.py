from pathlib import Path,os
a=open(Path.cwd()/"FIRSTFILE.txt",encoding='UTF-8')
print("no we are gonna writin siomething ofcourse you will not see it!!")
a.write('''When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate, hhh awesome for my first file''')
print("we are gonna read it compeletely:\n")
a.read()
pritn("we are gonna readit line by line:")
a.readlines()
a.close()
