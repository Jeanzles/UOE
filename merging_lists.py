import random
list1 = []
list2 = []
for i in range(0,15):
    x = random.randint(0,101)
    list1.append(x)
    y = random.randint(0,101)
    list2.append(y)
list1.sort()
list2.sort()
new_List = list1 + list2
new_List.sort()
print(new_List)
