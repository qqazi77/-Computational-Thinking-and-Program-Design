start = int(input('請輸入n的數值？'))
sum = 0
for i in range(start+1):
    sum = sum + i**2
    print('i為', i**2, '時，累加結果為', sum)
