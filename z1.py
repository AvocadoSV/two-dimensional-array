import random 

a = input('Enter two digits; First - the number of lists in the list; Second - the number of numbers in the inner list: ')
b=int(a[0])   
c=int(a[-1])  
h=list()        

for i in range(1,b+1):
    h.append(list())
for j in range (0,b):
    for k in range(0,c):
        g =random.randint(0,100)
        h[j].append(g)


print(f'This is your output --> {h}')