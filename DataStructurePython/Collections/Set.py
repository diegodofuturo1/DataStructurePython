set0 = {1,1,2,2,3,3,4,4,5,5}
set1 = {1,2,3,4,5,6,7,8,9,10}
set2 = {2,4,6,8,10,12,14,16,18,20}


print('set: ')
for item in set(set0):
    print(item)
    
print('intersection: ')
for item in set1.intersection(set2):
    print(item)
    
print('diference 1: ')
for item in set1.difference(set2):
    print(item)
    
print('diference2: ')
for item in set2.difference(set1):
    print(item)