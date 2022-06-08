class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createNode(lst: list) -> ListNode:
    node = ListNode()
    head = node
    for i in lst:
        tem = ListNode(i)
        node.next = tem
        node = node.next
    return head.next


def printNode(node: ListNode):
    while node.next:
        print(node.val, end=',')
        node = node.next
    print(node.val)


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    cur = ListNode(0)
    head = cur
    remainder = 0
    while l1 or l2:
        if l1 is None:
            l1 = ListNode(0)
        elif l2 is None:
            l2 = ListNode(0)

        if remainder > 0:
            remainder, cur.val = divmod(l1.val+l2.val+1, 10)
        else:
            remainder, cur.val = divmod(l1.val+l2.val, 10)

        l1 = l1.next
        l2 = l2.next
        if l1 or l2 or remainder > 0:
            cur.next = ListNode(remainder)
            cur = cur.next
        else:
            break
        
    return head


if __name__ == '__main__':
    test1 = [9, 9, 9, 9, 9, 9, 9]
    test2 = [9, 9, 9, 9]
    # test1 = [9, 2]
    # test2 = [9, 1]
    # test1 = [1,1,1]
    # test2 = [9]
    # test1 = [0]
    # test2 = [0]
    node1 = createNode(test1)
    node2 = createNode(test2)
    printNode(node1)
    printNode(node2)
    result = addTwoNumbers(node1, node2)
    printNode(result)
