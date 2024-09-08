class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def linkedList(arr):
    head=Node(arr[0])
    curr=head
    for el in arr[1:]:
        new=Node(el)
        curr.next=new
        curr=new
    return head
def Print_LinkedList(head):
    curr=head
    while curr:
        print(curr.data,end="")
        if curr.next is not None:
            print("->",end="")
        curr=curr.next
def delete_head(head):
    head=head.next

    return head
def delete_tail(head):
    curr=head
    while curr.next.next is not None:
        curr=curr.next
    curr.next=None
    return head
def delete_specificNode(head,pos):

    curr=head
    if pos==head.data:
        delete_head(head)
        
        
    while curr.next.data!=pos:
        curr=curr.next
    curr.next=curr.next.next
    return head
arr=[int(x) for x in input().split()]
head=linkedList(arr)
Print_LinkedList(head)
new_head=delete_head(head)
print()
Print_LinkedList(new_head)
new_head=delete_tail(new_head)
print()
Print_LinkedList(new_head)
print()
new_head1=delete_specificNode(new_head,5)
Print_LinkedList(new_head1)
        