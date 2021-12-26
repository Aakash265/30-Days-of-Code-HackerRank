n = int(input())
lst = []
for i in range(n):
    lst.append(input())

lst1 = []
lst2 = []

for i in range(len(lst)):
    ele = lst[i]
    size = len(ele)
    for j in range(size):
        if (j%2 == 0):
            lst1.append(ele[j])
        else:
            lst2.append(ele[j])

    print(''.join(lst1), ''.join(lst2))


