a = [1,2,3,4,5,6,7,8,9,10]

a.append(20)
a.append(21)
a.append(22)
a.append(23)
a.append(24)
a.append(25)
print ('List =',a)
print('List_index : ',a[0],a[9],a[10],a[15])

s1 = a[2:-3]
s2 = a[-6:]

print('Slice1 : ',s1)
print('Slice2 : ',s2)

set1 = {1,2,3}
set2 = {2,3,5}

interSet = set1.intersection(set2)
print(interSet)

uniSet = set1.union(set2)
print(uniSet)

diffSet = set1.difference(set2)
print(diffSet)

symDiffSet = set1.symmetric_difference(set2)
print(symDiffSet)
