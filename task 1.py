class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def merge_sort(head):
    if not head or not head.next:
        return head

    def get_middle(node):
        slow = node
        fast = node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    return merge_sorted_lists(left, right)


def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next


if __name__ == "__main__":
    lst = LinkedList()
    for value in [7, 3, 9, 1, 5]:
        lst.append(value)
    print("Original list:")
    lst.print_list()

    lst.head = reverse_linked_list(lst.head)
    print("Reversed list:")
    lst.print_list()

    lst.head = merge_sort(lst.head)
    print("Sorted list:")
    lst.print_list()

    lst2 = LinkedList()
    for value in [2, 4, 6, 8]:
        lst2.append(value)
    lst2.head = merge_sort(lst2.head)
    print("Second sorted list:")
    lst2.print_list()

    merged_list = LinkedList()
    merged_list.head = merge_sorted_lists(lst.head, lst2.head)
    print("Merged sorted list:")
    merged_list.print_list()
