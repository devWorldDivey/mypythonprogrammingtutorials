"""1672. Richest Customer Wealth"""
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        res = []
        for i in accounts:
            res.append(sum(i))

        return max(res)

    def runningSum(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(len(nums)):
            try:
                if i == 0:
                    res.append(nums[i])
                else:
                    res.append(nums[i]+res[i-1])
            except:
                print("Error")
        return res


    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = list(jewels)
        counter = 0
        for i in jewels:
            if i in list(stones):
                counter += list(stones).count(i)
        return counter

    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        mindiff = abs(arr[1]-arr[0])
        for j in range(len(arr)-1):
            mindiff = min(mindiff,abs(arr[j+1]-arr[j]))
        res = []
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i]) == mindiff:
                res.append([arr[i],arr[i+1]])
        return res

    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(len(arr)-2):
            if (arr[i] % 2 != 0) and (arr[i+1] % 2 != 0) and (arr[i+2] % 2 != 0):
                return True

    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix)
        resultmatrix = [[0]*m for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                resultmatrix[i][j] = matrix[j][i]
        return resultmatrix

    def majorityElement(self, nums: list[int]) -> int:
        m = len(nums)//2
        mydict = {}
        for i in nums:
            mydict[i]: nums.count(i)




mysol = Solution()
mysol.maximumWealth(accounts = [[1,2,3],[3,2,1]])
mysol.runningSum(nums = [1,2,3,4])
mysol.numJewelsInStones(jewels = "aA", stones = "aAAbbbb")
mysol.minimumAbsDifference(arr = [4,2,1,3])
mysol.threeConsecutiveOdds(arr = [1,2,34,3,4,5,7,23,12])
mysol.transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]])
mysol.majorityElement(nums = [3,4,3])