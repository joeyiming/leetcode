def getAns(n:int):
    totalSec = n//1000
    hour = (totalSec//60//60) % 24
    min = (totalSec//60)%60
    sec = totalSec % 60
    # return str(hour).rjust(2, '0')+":"+str(min).rjust(2, '0')+":"+str(sec).rjust(2, '0')
    return f'{hour:02}:{min:02}:{sec:02}'

# print(getAns(3600000))
# print(getAns(46800999))
# print(getAns(46801997))
print(getAns(int(input())))
