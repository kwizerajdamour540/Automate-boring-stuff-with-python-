from pathlib import Path
import os,shutil
print("now we are gonna revise files:")
print(f"your cureent directory:{Path.cwd()}")
li=['coming','welcome','working']
print(f"now we are gonna convert list:{li} into window path\n path:{Path('coming','welcome','working')}")
print(f"we are gonna add path from path before:{li} and 'working'to be\npath:{Path('coming','welcome','working')/"working"}")
print("let's try to change directory:")
print(f"first working  directory:{Path.cwd()}")
os.chdir('C:/Users/kwizera/Desktop/python/CHAPTER 9-TEXT PATTERN MATCHING WITH REGEX')
print(f'second working directory:{Path.cwd()}')
print("awesome let's move back to our folder")
os.chdir('C:/Users/kwizera/Desktop/python/CHAPTER 10-WRITING AND READING FILE')
print(f"now we get back:{Path.cwd()}")
print("but don't forget to to make relative linktoabsolut:")
print(f"this link:'{Path('dm/first')} 'is not absolute but we can make it \nabsolute:{Path('dm/first').absolute()}")