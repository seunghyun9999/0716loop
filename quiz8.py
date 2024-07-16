import random

i= 0
res=[]
while len(res)==6:
    i = i+1
    new = random.randint(1,45)
    if new in res :
        print('중복')
    else :
        res.append(new)
print(res)
