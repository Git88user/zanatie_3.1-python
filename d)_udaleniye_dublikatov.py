list = [1, 1, 2, 2, 2, 3, 4, 5, 2, 5]
newlist = []
for i in list:
    if i not in newlist:
        newlist.append(i)
print(newlist)
