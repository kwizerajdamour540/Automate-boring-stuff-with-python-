def fs(a):
    s = ' '
    if len(a) != 0:
        for i in range(len(a)):
            s =f"{s+ a[i] + ',' + ' '} "
        return s
    else:
        return s

spam = list(input("enter your list:").split(','))
print(f"list before converted to string:\n{spam}")

z = fs(spam)

print(f"string from list with space and comma:\n{z}")
