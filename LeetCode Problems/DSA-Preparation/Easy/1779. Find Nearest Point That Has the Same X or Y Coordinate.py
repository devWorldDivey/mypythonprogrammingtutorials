"""
You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).



Example 1:

Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
"""
"""
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        res = []
        for point in points:
            print(point)
            if point[0] == x or point[1] == y:
                res.append(point)
        print(res)
        mindis = -1
        minindex = []
        for m_dist in res:
            cur_mindis = abs(m_dist[0] - x) + abs(m_dist[1] - y)
            if mindis <= cur_mindis:
                minindex.append(points.index(m_dist))
        print(min(minindex))
        minindex.sort()
        return min(minindex)
"""






class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        print(arr)
        arr.sort()
        print(arr)
        res = []
        for i in range(len(arr)):
            try:
                res.append(abs(arr[i+1]-arr[i]))
            except:
                print("")
        print(res)
        if len(set(res)) == 1:
            return True

mysol = Solution()
mysol.canMakeArithmeticProgression(arr = [3,5,1])