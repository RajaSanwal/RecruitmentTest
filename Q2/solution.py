# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None
 
 
class Solution:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def deleteNthNode(self, n):

        temp = self.head
        if self.head == None:
            print("List is Empty")                 
        elif temp.next==None:
            self.head = None
        else:
            lengthCount = 0
            while temp != None:
                lengthCount = lengthCount + 1
                temp = temp.next

            lengthCount = lengthCount - n

            if lengthCount == 0:
                temp = self.head.next
                self.head.next = None

            curr = self.head
            prev = None

            while lengthCount > 0:
                prev = curr
                curr = curr.next
                lengthCount -= 1
            
            prev.next = curr.next
            curr.next = None
 
    def printList(self):
        temp = self.head
        while(temp):
            print(" %d" % (temp.data)),
            temp = temp.next
 
 
# Driver program
l_list = Solution()

number = int(input("Number of elements you want to enter: "))
for i in range(number):
    print("Enter Element "+str(i+1)+" in the Linklist")
    value = int(input())
    l_list.push(value)
    
print("Created Linked List: ")
l_list.printList()

delete_index = int(input("Enter the index you want to delete from end: "))
 
l_list.deleteNthNode(delete_index)
print("\nLinked List after Deletion of:"+str(delete_index))
l_list.printList()
