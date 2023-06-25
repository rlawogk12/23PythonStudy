data=[[10,20,30],[40,50],[60,70,80,90]]
for row in range(len(data)):
    for x in range(len(data[row])):
        print(data[row][x],end=" ")
    print()

for row in data:
    for x in row:
        print(x,end=" ")
    print()

