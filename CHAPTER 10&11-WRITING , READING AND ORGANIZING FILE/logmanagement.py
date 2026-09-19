import os,shutil
from pathlib import Path
print(Path.cwd())
path=Path.cwd()/"logs"
try:
	for file in path.glob("*.logs"):
		with open(file)as obj:
			shutil.copy("file",f"{file.stem}_backups")
			for i in obj.readlines():
				if "login failed" in i:
					with open(f"{file.stem}_failed",'a') as read:
						read.write(i)

except FileNotFoundError:
	print("file not found")    