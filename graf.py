import random
n = 10
list1 = [random.randint(1, n) for i in range(n*2)]
list2 = [random.randint(1, n) for i in range(n*2)]
list3 = list(set(list1 + list2))
path = []
def graf(x, y, list1, list2):
    if x == list1[i] and y == list2[i]:
        return True
    else:
        return False
print (graf(5, 7, 10))
print (list3)