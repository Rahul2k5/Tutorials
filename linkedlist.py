class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def create(self,data=0):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
        else:
            tail=self.head
            while True:
                if tail.next == None:
                    break
                tail=tail.next
            tail.next=newnode
    def display(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next
    def insert_middle(self,data):
        inode=Node(data)
        count=0
        set_head=self.head
        while True:
            if set_head==None:
                break
            set_head=set_head.next
            count+=1
        
        if count==0:
            self.head=inode
            print("list is empty")

        count=count//2
        set_head=self.head
        i=0
        while i<count-1:
            set_head=set_head.next
            i+=1
        inode.next=set_head.next
        set_head.next=inode

    def remove_end(self):
        start=self.head
        count=0
        if self.head==None:
                print("list is empty")
        while True:
            if start==None:
                break
            start=start.next
            count+=1
        if count==1:
            self.head=None
            return 
        delend=self.head
        i=0
        while i<count-2:
            delend=delend.next
            i+=1
        delend.next=None

    def delete_At_n(self,n):
        start=self.head
        count=0
        i=0
        if n==1:
            self.head=self.head.next
        while True:
            if start.next==None:
                break 
            start=start.next
            count+=1
            i+=1
        if n<count+1:
            del_prev=self.head
            k=0
            while k<n-2:
                del_prev=del_prev.next
                k+=1
            del_nex=self.head
            j=0
            while j<n:
                del_nex=del_nex.next
                j+=1
            del_prev.next=del_nex
        else:
            print(f"{n} position does not exist !!")

            




List1=LinkedList()
List1.create(1)
List1.create(2)
List1.create(3)
List1.create(4)
List1.create(5)
List1.create(6)
List1.create(7)
List1.create(8)
List1.create(9)
List1.create(10)



#List1.insert_middle(31)
#List1.remove_end()

List1.delete_At_n(1)

List1.display()
