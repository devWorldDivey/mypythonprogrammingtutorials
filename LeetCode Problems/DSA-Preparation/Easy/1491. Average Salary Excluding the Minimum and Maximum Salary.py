"""You are given an array of unique integers salary where salary[i] is the salary of the ith employee. Return the
average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will
be accepted. Example 1: Input: salary = [4000,3000,1000,2000] Output: 2500.00000 """
class Solution:
    def average(self, salary: list[int]) -> float:
        salary.pop(salary.index(max(salary)))
        salary.pop(salary.index(min(salary)))
        print(sum(salary)/len(salary))
mysol = Solution()
mysol.average(salary = [4000,3000,1000,2000])
