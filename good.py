l=[]
d=1
for k in range(1,9):
    n=input()
    g=n.count('*')
    if g>1:
        d=0
    if '*' in n:
        c=n.index('*')+1
    l.append([k,c])
for m in range(len(l)):
    for c in range(m+1,len(l)):
        if l[m][0]==l[c][0] or l[m][1]==l[c][1] or abs(l[m][0]-l[c][0])==abs(l[m][1]-l[c][1]):
            d=0
if d:
    print("valid")
else:
    print("invalid")