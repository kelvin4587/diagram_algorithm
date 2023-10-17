class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toString(self):
        current = self
        result = ""
        while current:
            result = result + str(current.val)
            if current.next:
                result = result + "->"
            current = current.next
        return result


class Solution(object):
    def reverseList(self, head):
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def reverseListRecurse(self, head):
        if head is None or head.next is None:
            return head
        current = self.reverseListRecurse(head.next)
        head.next.next = head
        head.next = None
        return current


if __name__ == '__main__':
    head = None
    cur = None
    for x in range(1, 6):
        if x == 1:
            cur = ListNode(x)
            head = cur
        else:
            cur.next = ListNode(x)
            cur = cur.next
    print(head.toString())
    solution = Solution()
    result = solution.reverseList(head)
    print(result.toString())
    recurse = solution.reverseListRecurse(result)
    print(recurse.toString())
