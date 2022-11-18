"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to
visit all the points in the order given by points.
You can move according to these rules:
In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.
"""
points = [[1,1],[3,4],[-1,0]]
class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        steps = 0
        for i in range(len(points) - 1):
            point = points[i]
            #print(point,"--",point[0])
            next_point = points[i + 1]
            #print(next_point,"--",next_point[0])
            steps += max(abs(next_point[0] - point[0]), abs(next_point[1] - point[1]))
            print(steps)
        return steps

my_sol = Solution()
print(my_sol.minTimeToVisitAllPoints(points))