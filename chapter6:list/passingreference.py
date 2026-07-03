# in pyhton variable store refernce not values
def eggs(some_parameter):
    some_parameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)  # Prints [1, 2, 3, 'Hello']
#because of  eggs function appending something it moodifies spam

