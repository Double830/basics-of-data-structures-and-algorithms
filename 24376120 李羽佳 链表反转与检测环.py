class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


def reverse(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def reverse_recursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head


def print_linked_list(head):
    vals = []
    curr = head
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))


if __name__ == "__main__":
    print("===== 测试 1：链表反转 =====")
    arr = [1, 2, 3, 4, 5]
    head = create_linked_list(arr)
    print("原链表：")
    print_linked_list(head)

    reversed_head = reverse(head)
    print("迭代反转后：")
    print_linked_list(reversed_head)

    reversed_head_rec = reverse_recursive(reversed_head)
    print("递归反转后（恢复原样）：")
    print_linked_list(reversed_head_rec)

    print("\n===== 测试 2：判断链表是否有环 =====")
    head1 = create_linked_list([1, 2, 3, 4])
    print("无环链表 has_cycle:", has_cycle(head1))

    head2 = create_linked_list([1, 2, 3, 4])
    curr = head2
    while curr.next:
        curr = curr.next
    curr.next = head2.next
    print("有环链表 has_cycle:", has_cycle(head2))