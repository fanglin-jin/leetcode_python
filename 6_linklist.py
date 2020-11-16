'''
Project: leetcode_python
Author: jinfanglin
Date: 2020/11/16
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def LinkList(head):
    slow = fast = head
    if not head or not head.next:
        return False
    while slow and fast.next:
        if slow == fast.next:
            return True
        fast = fast.next.next
        slow = slow.next
    return False
if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    print(LinkList(n1))
    l1 = Node(1)
    l2 = Node(2)
    l3 = Node(3)
    l4 = Node(4)
    l5 = Node(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l1
    print(LinkList(l1))
