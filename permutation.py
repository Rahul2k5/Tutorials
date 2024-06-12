def str_to_int(s):
    conv={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    number=0
    for i in s:
        if i in conv:
            x=conv[i]
            number = number*10 + x
    return number
y=str_to_int('12243')
print(y)