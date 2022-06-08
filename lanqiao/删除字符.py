word = 'LANQIAO'
remainOp = 3

charList = list(word)
while remainOp:
    if charList[0]>charList[1]:
        del charList[0]
    else:
        del charList[1]
        
    remainOp -= 1
        
    
word = ''.join(charList)
print(word)
