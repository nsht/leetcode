class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"ListNode{{{self.val} next:{self.next}}}"

class Solution:
    def middleNode(self, head):
        len = 1
        count = 1
        next_head = head.next
        while next_head:
            next_head = next_head.next
            count += 1
        ans = head
        for i in range(0,count//2):
            ans = ans.next
        return ans

def generate_link_list(l):
    f_obj = None
    p_obj = None
    for x in reversed(l):
        x = ListNode(x)
        if f_obj is None:
            x.next = None
            f_obj = x
            p_obj = x
            continue
        else:
            x.next = p_obj
        f_obj = x
        p_obj = x
    return f_obj

link_list = generate_link_list([1,2,3,4,5,6])
print(Solution().middleNode(link_list))


