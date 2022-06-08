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
    head = l1
    jin = False
    while l1 and l2:
        if jin:
            l1.val = l1.val+l2.val+1
        else:
            l1.val = l1.val+l2.val

        if l1.val >= 10:
            jin = True
            l1.val %= 10
        else:
            jin = False

        if l1.next:
            l1 = l1.next
        else:
            break
        if l2.next:
            l2 = l2.next
        else:
            break

    if l1 is None:
        l1 = l2

    # print("test1")
    while l1:
        # print("test2")
        l1.val %= 10

        if l1.next:
            l1 = l1.next
            if jin:
                l1.val += 1
            else:
                jin = False
        else:
            # print("test3")
            temp = ListNode(1)
            l1.next = temp
            break

    return head


if __name__ == '__main__':
    test1 = [9, 9, 9]
    test2 = [9, 9]
    node1 = createNode(test1)
    node2 = createNode(test2)
    printNode(node1)
    printNode(node2)
    addTwoNumbers(node1, node2)
    printNode(node1)
