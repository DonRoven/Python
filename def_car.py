import random
def city(x, y):
    n = 10
    list1 = [random.randint(1, n) for i in range(n*2)]
    list2 = [random.randint(1, n) for i in range(n*2)]
    zip(list1,list2)

print city(4, 6)