# from datetime import datetime as dt
# stamp = input()
# print(dt.fromtimestamp(stamp))

totalsecs = int(input())//1000

hour = totalsecs // 3600 % 24
minute = totalsecs // 60 % 60
sec = totalsecs % 60
print(f'{hour:02}:{minute:02}:{sec:02}')
