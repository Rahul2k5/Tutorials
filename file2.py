def printfile(x,y):
    f1=open(x,"r")
    f2=open(y,"w")
    i=True 
    while i==True:
        t=f1.read(50)
        if t=="":
            i=False
        f2.write(t)
    f1.close()
    f2.close()
    return
printfile("/home/rahul/python/x.text","/home/rahul/python/y.text")