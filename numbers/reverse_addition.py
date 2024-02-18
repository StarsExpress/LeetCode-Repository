from typing import Optional


class ListNode:  # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if len(l1) > len(l2):
        #     l2 += [0] * (len(l1) - len(l2))
        # if len(l1) < len(l2):
        #     l1 += [0] * (len(l2) - len(l1))
        #
        # output_list, inheritance = [], 0
        # for r in range(len(l1)):
        #     intermediate = l1[r] + l2[r] + inheritance
        #     inheritance = intermediate // 10
        #     output_list.append(intermediate % 10)
        #
        # return output_list + [inheritance] if inheritance != 0 else output_list

        return (l1 + l2) % 10


if __name__ == '__main__':
    solution = Solution()
    l1, l2 = [9] * 7, [9] * 4
    # print(solution.addTwoNumbers([9] * 7, [9] * 4))
    # print(solution.addTwoNumbers(l1, l2))
