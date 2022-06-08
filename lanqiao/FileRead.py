import os

count=0
if os.path.exists('./String.txt'):
    f = os.open('./String.txt',os.O_RDONLY)
    content = os.read(f,os.path.getsize(f)).decode()
    print(content)
    for ch in content:
        if ch.isdigit():
            if int(ch)>5:
                count+=1

    print(count)