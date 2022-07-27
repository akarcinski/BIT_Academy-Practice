class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        curr_node.next = new_node

def Merge_sort(head):
    def Get_middle(head):
        if head == None:
            return head
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def Merge_sorted(left, right):
        if left == None:
            return right
        if right == None:
            return left
        
        if left.data <= right.data:
            result = left
            result.next = Merge_sorted(left.next, right)
        else:
            result = right
            result.next = Merge_sorted(left, right.next)
        return result
#---------------------------------------------------------------------
    if head == None or head.next == None:
        return head

    middle = Get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = Merge_sort(head)
    right = Merge_sort(next_to_middle)

    sorted_list = Merge_sorted(left, right)
    return sorted_list

'''linked = LinkedList()
linked.append(5)
linked.append(3)
linked.append(7)
linked.append(1)
linked.append(2)
linked.append(6)
linked.append(0)

Merge_sort(linked.head)'''