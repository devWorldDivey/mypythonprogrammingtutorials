"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.



Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
"""
from collections import defaultdict


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trustedby =defaultdict(int)

        candidates = set(i for i in range(1,n+1))
        for i in trust:
            candidates.discard(i[0])
            trustedby[i[1]] += 1
        print(trustedby)
        for c in candidates:
            if trustedby[c] == n-1:
                return c
        return -1
mysol = Solution()
mysol.findJudge(n = 2, trust = [[1,3],[2,3]])
trustdict = {}
