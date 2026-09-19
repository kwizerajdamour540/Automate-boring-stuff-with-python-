import re
def remove_any_space(word):
	remove=re.sub(r'\s',"",word)
	return remove
print("enter sentence include space to be removed:")
name=input()
print(f"answer:{remove_any_space(name)}")