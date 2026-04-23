class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
    def delete_at_index(self, index):
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        prev = self.head
        count = 0
        while prev and count < index - 1:
            prev = prev.next
            count += 1
        if not prev or not prev.next:
            raise IndexError("索引超出链表范围")
        to_delete = prev.next
        prev.next = to_delete.next
        to_delete.next = None
    def print_list(self):
        cur = self.head
        res = []
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        print(" -> ".join(res))
if __name__ == "__main__":
    ll = LinkedList()
    ll.append("a")
    ll.append("b")
    ll.append("c")
    ll.append("d")
    print("删除前：")
    ll.print_list()
    ll.delete_at_index(2)
    print("删除后：")
    ll.print_list()