#single linked list
class Nodes:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node= Nodes(data)
        if not self.head:
            self.head=new_node
            return
        last_node= self.head
        while last_node.next:
            last_node= last_node.next
        last_node.next= new_node
    def display(self):
        current= self.head
        while current:
            print(current.data, end=" ->")
            current= current.next
        print("None")
sll= singlyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.display()

#Reversed linked list
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node= curr.next
            curr.next = prev
            prev= curr
            curr = next_node
        return prev
    
#Merge two sorted lists
class Solution(object):
    def mergeTwoLists(self,list1,list2, ListNode):
        dummy = ListNode(-1)
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current= current.next
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return dummy.next
    
#Remove Nth Node from End to List
class Solution(object):
    def removeNthFromEnd(self, head, n, ListNode):
        dummy = ListNode (0, head)
        slow = fast = dummy
        for i in range(n):
            fast=fast.next
        while fast.next:
            slow= slow.next
            fast = fast.next
            slow.next = slow.next.next
            return dummy.next