# −5+(−3)+(−1)+1+3+…

seriessize = int(input("Enter the size of the series: "))
startnum = -5
i = 0
while i < seriessize:
    if i == seriessize-1:
        print(startnum, end='')
    else:
        print(startnum, end=' ')
    startnum = startnum + 2
    i+=1
