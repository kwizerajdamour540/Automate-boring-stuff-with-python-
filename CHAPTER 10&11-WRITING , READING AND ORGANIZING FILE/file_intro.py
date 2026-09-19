from pathlib import Path,os
print(f"your are working at:{Path.cwd()}")
print(f"i'm trying to use older version to get path!:{os.getcwd()}")
print(f"nah,don't forget to to call home directory:{Path.home()}")
print("now i'm gonna show you path pieces:\n")
z=Path.cwd()
print(z)
print(f" anchor:{z.anchor}")
print(f"parent:{z.parent}")
print(f"name:{z.name}")
print("we gonna divide name into two categories\t stem \t suffix:\n")
print(f"stem:{z.stem}\n suffix:{z.suffix}")
print("now we are gonna add file size and stamp:\n")
p=Path.cwd()
print(f"file size and timestamp:{p.stat()}")
print(f"now we can see size:{p.stat().st_size}")
print(f"now we are gonna look last modiefied timestamp:{p.stat().st_mtime} in bytes")
#we are gonna use time module so let's import it first
import time
f=time.asctime(time.localtime(p.stat().st_mtime))
print(f"now wegonna convert last modified timestamp in loaltime\n answer:{f}")

