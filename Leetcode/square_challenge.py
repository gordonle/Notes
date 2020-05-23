class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Solution:
    def removeDups(self, nums):
        # make it into a linkedlist first
        head = self.makeList(nums, 0)
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                # delete both
                prev = cur.prev
                nxt = cur.next.next
                cur = None
                if prev:
                    prev.next = nxt
                    cur = prev
                else:
                    head = nxt

                if nxt:
                    nxt.prev = prev
                    cur = cur if cur else nxt
            else:
                cur = cur.next

        ans = []
        if not cur:
            return ans

        while head:
            ans.append(head.val)
            head = head.next

        return ans

    def makeList(self, nums, i):
        node = None
        if i < len(nums):
            node = Node(nums[i])
            node.next = self.makeList(nums, i + 1)
            if node.next:
                node.next.prev = node

        return node

soln = Solution()

print(soln.removeDups([1,2,3]) == [1,2,3])
print(soln.removeDups([1,2,2,1]) == [])
print(soln.removeDups([1,2,1,2,1]) == [1,2,1,2,1])
print(soln.removeDups([1,2,3,3,2,2]) == [1,2])
print(soln.removeDups([0,1,2,3,3,2,1,1,5,5,2]) == [0,1,2])
print(soln.removeDups([1,2,2,1,0]) == [0])
print(soln.removeDups([1,2,3,3,2]) == [1])
