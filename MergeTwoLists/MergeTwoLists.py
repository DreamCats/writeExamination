
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    temp = ListNode(0)
    res = temp
    while l1 and l2:
        if l1.val < l2.val:
            res.next = l1
            res = res.next
            l1 = l1.next
        else:
            res.next = l2
            res = res.next
            l2 = l2.next
    if l1 == None:
        res.next = l2
    elif l2 == None:
        res.next = l1
    return temp.next


if __name__ == "__main__":
    l1 = ListNode(-2)
    l1.next = ListNode(5)
    # l1.next.next = ListNode(4)
    l2 = ListNode(-9)
    l2.next = ListNode(-6)
    l2.next.next = ListNode(-3)
    
    res = mergeTwoLists(l1, l2)
    

    while res.next:
        print(res.val)
        res = res.next
    print(res.val)

