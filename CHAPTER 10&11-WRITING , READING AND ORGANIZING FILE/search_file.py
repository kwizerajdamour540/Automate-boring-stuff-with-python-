from pathlib import Path,os
g=Path.cwd()
print(f"your list of files:{list(g.glob("*"))}")
print("before output look like chaosfor many file now we are gonna make it clear list:")
for name in g.glob("*"):
	print(name)
print("good well listed!!")
print("now we gonna chech if file path exist:\n")
f=Path("c:/users/kwizera/python")
print(f"let's check is path\" {f}\"exist here answer should be false\n answer:{f.exists()}")
f=Path("c:/users/kwizera/Desktop/python")
print(f"let's check is path\" {f}\"exist here answer should be true\n answer:{f.exists()}")
print("we move to check if this folder we are working exist!!: here answer should be true")
print(f"in path :{Path.cwd()} folder:{f.is_dir()} exist")
print(f"this is amazing yo can check if there is flash disk on your pc:")
flash=Path('D:/')
print(f" flash disk mounted on your pc or D drive?:{flash.is_dir()} ")


