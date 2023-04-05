"""
886. Possible Bipartition
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may
dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled
ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in
this way.
Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].

"""

class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        groupa = []
        groupb = []

            #groupa.append(i[0[0]])
            #groupb.append(i[0][1])

            #print(dislikes[i])


mysol = Solution()
mysol.possibleBipartition(n = 4 , dislikes = [[1,2],[1,3],[2,4]])