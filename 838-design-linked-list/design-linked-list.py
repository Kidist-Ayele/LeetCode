class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(0, index):
            cur = cur.next
        
        return cur.val

    def addAtHead(self, val: int) -> None:

        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:

        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.size:
            return 
        
        cur = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = cur
            self.head = new_node
        else:
            for _ in range(index - 1):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.head

        if index == 0:
            self.head = self.head.next
        
        else:
            
            for _ in range(0, index - 1):
                cur = cur.next
            cur.next = cur.next.next
        self.size -= 1


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)