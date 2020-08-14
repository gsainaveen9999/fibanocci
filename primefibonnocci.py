n1,n2=map(int,input().split())
l=[]
l1=[]
l2=[]
for i in range(n1,n2+1):
  if(i>1):
    for j in range(2,i):
      if(i%j==0):
          break
    else:
        l.append(i)
for i in l:
    for j in l:
        if(i!=j):
            x=str(i)+str(j)
            y=int(x)
            l1.append(y)
for i in l1:
    for j in range(2,i):
      if(i%j==0):
          break
    else:
        if i not in l2:
            l2.append(i)
f=min(l2)
s=max(l2)
n=len(l2)
def fibonacci(n): 
    a = f
    b = s
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 
print(fibonacci(n)) 
