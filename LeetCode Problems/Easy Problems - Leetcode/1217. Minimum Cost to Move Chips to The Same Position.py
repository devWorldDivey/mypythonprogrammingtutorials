"""
1217. Minimum Cost to Move Chips to The Same Position
"""
class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        d = {"oddnum":0,"evennum":0}
        for i in position:
            if i%2 == 0:
                d["evennum"] += 1
            else:
                d["oddnum"] += 1
        return min(d["oddnum"],d["evennum"])
mysol = Solution()
mysol.minCostToMoveChips(position = [1,2,3])