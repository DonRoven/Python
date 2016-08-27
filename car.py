import random
n = 10
list1 = [random.randint(1, n) for i in range(n)]
list2 = [random.randint(1, n) for i in range(n)]

cities = {}
for k, v in zip(list1,list2):
    if k in cities:
        cities[k].append(v) 
    else:
        cities[k] = [v]
for k, v in zip(list1,list2):
    if k not in cities:
        if v in cities:
            cities[v].append(k) 
        else:
            cities[v] = [k]
    
print (cities)