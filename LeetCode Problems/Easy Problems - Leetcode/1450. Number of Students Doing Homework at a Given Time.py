"""
Given two integer arrays startTime and endTime and given an integer queryTime.
The ith student started doing their homework at the time startTime[i] and finished it at
time endTime[i].
Return the number of students doing their homework at time queryTime. More formally,
return the number of students
where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1
"""
class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        arrlen = len(startTime)
        counter = 0
        for i in range(arrlen):
            if startTime[i] <= queryTime <= endTime[i]:
                counter += 1
        return counter

mysol = Solution()
mysol.busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4)
