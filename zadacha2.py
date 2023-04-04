from random import randint
l= []
y = 1
m = randint(3,10)
while y <= m:
    l.append(randint(1,100))
    y += 1
print(l)
i=0
o=''
while i<m:
    j=i+1
    while j<m:
        if int(l[i])==int(l[j]):
            o=o+str(l[i])+' '
        j+=1
    i+=1
if o=='':
    print('Повторений нет')
else:
    print('ПОвторения: ',o)