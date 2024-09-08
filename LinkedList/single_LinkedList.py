class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def Linkedlist(arr):
    head=Node(arr[0])
    curr=head
    count=1
    for el in arr[1:]:
        if el==-1:
            break
        newnode=Node(el)
        curr.next=newnode
        curr=newnode
        count+=1
    return head,count
def print_LinkedList(head,count):
    curr=head
    while curr:
        print(curr.data,end="")
        if curr.next is not None:
            print("->",end="")
        curr=curr.next
    print("\nthe size is :",count)
def insert_at_head(head,data,count):
    new=Node(data)
    new.next=head
    head=new
    count+=1
    return head,count
def insert_at_tail(head,data,count):
    new=Node(data)
    curr=head
    while curr.next:
        
        curr=curr.next
        count=count+1
    curr.next=new
    return head,count
def insert_after(head,count,pos,data):
    new=Node(data)
    curr=head
    while curr.data!=pos:
        curr=curr.next
    new.next=curr.next.next
    curr.next=new
    # new.next=curr.next.next
    count+=1
    
    return head,count
    
arr=[int(x) for x in input().split(" ")]
head,count=Linkedlist(arr)
print("The original Linked List is : ")
print("The size of the linked list is :",count)
print_LinkedList(head,count)
newhead,count=insert_at_head(head,11,count)
print("\nAfter inserting at the head the linked list : ")
print_LinkedList(newhead,count)
tailhead,count=insert_at_tail(newhead,6,count)
print("\nAfter inserting at the tail")
print_LinkedList(tailhead,count)
head_after_specific_Pos,count=insert_after(newhead,count,5,10)
print("\n After inserting node after the specific position is : ")
print_LinkedList(head_after_specific_Pos,count)

    