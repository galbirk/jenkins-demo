import sys

def add(a,b):
    return a+b

result = add(2,2)

with open('result.txt','w') as f:
    f.write(str(result))
    f.flush()
