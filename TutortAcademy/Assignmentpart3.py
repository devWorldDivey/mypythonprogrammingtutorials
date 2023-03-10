class Solution:
    def isHappy(self, n: int) -> bool:
        newnum = 0
        res = []
        while (1 not in res):
            for i in str(n):
                newnum += int(i)*int(i)
            if newnum not in res:
                res.append(newnum)
            else:
                return False
            n = newnum
            newnum = 0
        return True

    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            while n != 1:
                if n < 1:
                    return False
                x = n/2
                n = x
        if n == 1:
            return True

    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s)
        b = sorted(t)
        return a == b

    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1:
            if n%2 == 0:
                n=n//2
            elif n%3 == 0:
                n=n//3
            elif n%5 == 0:
                n=n//5
            else:
                return False
        return True

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.append(0)
        return (nums)

    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
            if s[j] not in vowels:
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
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



