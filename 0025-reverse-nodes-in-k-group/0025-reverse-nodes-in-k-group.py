class Solution:
    def reverseKGroup(self, head, k):
        # Dummy node initialization
        dummy = jump = ListNode(-1)
        dummy.next = l = r = head
        
        while True:
            count = 0
            while r and count < k:
                count += 1
                r = r.next
            if count == k:
                pre, cur = r, l
                for _ in range(k):
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                jump.next = pre
                jump = l
                l = r
            else:
                return dummy.next