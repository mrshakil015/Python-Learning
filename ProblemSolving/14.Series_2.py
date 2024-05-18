# 3+7+11+15+…

seriessize = int(input("Enter the size of the series: "))
startnum = 3
i = 0
while i < seriessize:
    if i == seriessize-1:
        print(startnum, end='')
    else:
        print(startnum, end=' ')
    startnum = startnum + 4
    i+=1
