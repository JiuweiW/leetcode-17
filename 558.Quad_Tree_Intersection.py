# https://leetcode.com/problems/generate-random-point-in-a-circle/description/
#
# algorithms
# Easy (35.42%)
# Total Accepted:    1.7k
# Total Submissions: 4.8k
# beats 100.0% of python submissions

"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, q1, q2):
        if q1.isLeaf:
            return q1.val and q1 or q2
        elif q2.isLeaf:
            return q2.val and q2 or q1
        else:
            tLeft = self.intersect(q1.topLeft, q2.topLeft)
            tRight = self.intersect(q1.topRight, q2.topRight)
            bLeft = self.intersect(q1.bottomLeft, q2.bottomLeft)
            bRight = self.intersect(q1.bottomRight, q2.bottomRight)
            if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                node = Node(tLeft.val, True, None, None, None, None)
            else:
                node = Node(False, False, tLeft, tRight, bLeft, bRight)
        return node
