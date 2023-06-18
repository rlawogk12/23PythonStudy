scores=[[75,83,80],[86,86,73],[76,95,83],[89,96,69],[89,76,93]]
for i in range(len(scores)):
    sum=0
    for j in range(len(scores[i])):
        sum=sum+scores[i][j]
    avg=sum/len(scores[i])
    print("%d번째 학생의 합계:%d,vudrbs:%2f" %(i+1,sum,avg))