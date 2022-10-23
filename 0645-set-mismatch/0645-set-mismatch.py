class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = n*(n+1)//2
        given_sum = sum(nums)
        distinct_given_sum = sum(set(nums))
        return [given_sum - distinct_given_sum, s-distinct_given_sum]