def even_to_str():
    a=[]
    n=int(input("enter rows : "))
    m=int(input("enter columns : "))
    x=1
    y='even'
    for i in range(n):
        b=[]
        for j in range(m):
            if (i+j)%2==0:
                b.append(y)
            else:
                b.append(x)
            x+=1
        a.append(b)
    a[0][0]=0
    print(a)
    for i in a:
        print(i)
even_to_str()