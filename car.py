import random
n = 10
list1 = [random.randint(1, n) for i in range(n)]
list2 = [random.randint(1, n) for i in range(n)]
d1 = dict(zip(list1,list2))
citys = {}
for i in list1:
    if i in citys:
        citys[list1[i]] += list2[i]
    else:
        citys[list1[i]] = list2[i]
    
