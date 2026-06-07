# jumping statements - break & continue
for i in range(1,11):
    if i==5:
        break
    print(i) # 1 2 3 4

for i in range(1,11):
    if i==3 or i==7 or i==9:
        continue
    print(i) # 1 2 4 5 6 8 10


