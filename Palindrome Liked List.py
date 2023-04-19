# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         half_1 = head[0:(len(head) // 2)]
#         half_2 = head[-1::-1]


head = [1, 2, 3, 4, 8908, 4, 3, 2, 1]



def isPalindrome(head):
    if len(head) % 2 != 0:
        del head[len(head) // 2]
    half_1 = head[0:len(head) // 2]
    half_2 = head[-1:len(head) // 2 - 1:-1]

    if half_1 == half_2:
        return True
    else:
        return False

print(isPalindrome(head))