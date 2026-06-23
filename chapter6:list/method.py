#list in python 
animal=[]
number=[]
spam=[]
#to add cat inside animal list

animal.append("cat")
#by index
animal.insert(0,"dog")
print (f"after addin dog at index 0 {animal}")

animal.insert(2,"horse")
print (f"after adding horse at index 2 {animal}")
#removing value
animal.remove("dog")
print (f"after removing dog {animal}")

import random
number=[x for x in range(10)]
print ("random generating number:\n")
#sorting by acsending
number.sort()
print (number)
number.sort(reverse=True)

print (f" after reverse list look like{number}")

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']

print (f"new string list:\n{spam}")
spam.reverse()

print (f"after reversing our  list:\n{spam}")

print ("i want to delete bob:\n")


del spam[-3]
print (f"bob deleted on list:\n{spam}")
