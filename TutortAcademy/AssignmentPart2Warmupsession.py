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
                    res.append(nums[i] + res[i - 1])
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
        mindiff = abs(arr[1] - arr[0])
        for j in range(len(arr) - 1):
            mindiff = min(mindiff, abs(arr[j + 1] - arr[j]))
        res = []
        for i in range(len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) == mindiff:
                res.append([arr[i], arr[i + 1]])
        return res

    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(len(arr) - 2):
            if (arr[i] % 2 != 0) and (arr[i + 1] % 2 != 0) and (arr[i + 2] % 2 != 0):
                return True

    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix)
        resultmatrix = [[0] * m for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                resultmatrix[i][j] = matrix[j][i]
        return resultmatrix

    def majorityElement(self, nums: list[int]) -> int:
        counter = 0
        element = 0
        for num in nums:
            if counter == 0:
                element = num
            counter += (1 if num == element else -1)
        return element

    def moveZeroes(self, nums: list[int]) -> None:
        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.append(0)
        return nums

    def isPowerOfTwo(self, n: int) -> bool:
        """        if n == 1:
            return True
        else:
            while n != 1:
                if n < 1:
                    return False
                x = n/2
                n = x
        if n == 1:
            return True """
        return ((n & (n - 1)) == 0)

    def isAnagram(self, s: str, t: str) -> bool:
        return (sorted(s) == sorted(t))

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                return False
        return True

    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
        i = 0
        j = len(s)-1
        s = list(s)
        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels:
                j -= 1
                continue
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        return "".join(s)

    def thirdMax(self, nums: list[int]) -> int:
        nums=set(nums)
        if len(nums)<3:
            return max(nums)
        else:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return max(nums)

    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        for i in s:
            if i in t:
                t.remove(i)
        return "".join(t)

    def addDigits(self, num: int) -> int:
        while num / 10 >= 1:
            sumofnum = 0
            for i in str(num):
                sumofnum += int(i)
            num = sumofnum
        return sumofnum

    def getLucky(self, s: str, k: int) -> int:
        alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7 \
            , "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15 \
            , "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23 \
            , "x": 24, "y": 25, "z": 26}
        answ = ""
        for i in s:
            answ += str(alphabet[i])
        while k != 0:
            answ = sum(int(x) for x in str(answ))
            k -= 1
        return answ

mysol = Solution()
mysol.maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]])
mysol.runningSum(nums=[1, 2, 3, 4])
mysol.numJewelsInStones(jewels="aA", stones="aAAbbbb")
mysol.minimumAbsDifference(arr=[4, 2, 1, 3])
mysol.threeConsecutiveOdds(arr=[1, 2, 34, 3, 4, 5, 7, 23, 12])
mysol.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mysol.majorityElement(nums=[1, 2, 1])
mysol.moveZeroes(nums=[0, 1, 0, 3, 12])
mysol.isPowerOfTwo(n=16)
mysol.isAnagram(s="anagram", t="nagaram")
mysol.isUgly(n=14)
mysol.reverseVowels("Leetcode")
mysol.thirdMax([1,2,3])
mysol.findTheDifference(s = "a", t = "aa")
mysol.addDigits(10)
mysol.getLucky(s = "leetcode", k = 2)

