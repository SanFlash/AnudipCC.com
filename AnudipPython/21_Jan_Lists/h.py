ulist = []

for _ in range(5):
    ulist.append(input("Enter an element: "))

del ulist[0]
ulist.pop()
ulist.pop(3)

print(ulist)
