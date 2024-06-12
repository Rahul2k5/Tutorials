class check_file:
    def __init__(self,f1):
        self.f1=f1
    def check_for_word(self):
        with open(self.f1) as file1:
            text=file1.read()
            if 'neha' in text:
                return True
            else: 
                return False
    def count_word(self):
        with open(self.f1) as file1:
            text=file1.read()
            a=text.split()
            i=0
            count=0
            while i<len(a):
                if 'neha'==a[i]:
                    count+=1
                i+=1
            return count
    
def main():
    file1="/home/rahul/Rahulpython/python/x.text"
    obj=check_file(file1)
    a=obj.check_for_word()
    #print("True")
    #else:
    print(a)
    count = obj.count_word()
    print(count)

if __name__=="__main__":
    main()