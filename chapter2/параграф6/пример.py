list1 = []
sum1 = 0
sum2 = 0
sum3 = 0

for i in range(1, 100, 7):
    list1.append(i)

list2 = [i for i in range(100, 200, 13)]
list3 = [i for i in range(200, 300, 23)]
print(list1)
print(list2)
print(list3)
print(list3*3)
print(list1 + list2 + list3)

for i in range(len(list1)):
    sum1 += list1[i]
for i in range(len(list2)):
    sum2 += list2[i]
for i in range(len(list3)):
    sum3 += list3[i]

print(sum1)
print(sum2)
print(sum3)
