class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        sequence = []
        
        def backtrack(index):
            #if we have checked all the elements
            if index == len(nums):
                if len(sequence) >= 2:
                    res.add(tuple(sequence))
                return
            #if the sequence remains increasing after appending nums[index]
            if not sequence or sequence[-1] <= nums[index]:
                sequence.append(nums[index])    #append nums[index] to the sequence
                backtrack(index+1)              #call recursively
                sequence.pop()                  #delete nums[index] from the end of the sequence
            backtrack(index+1)                  #call recursively not appending an element
        backtrack(0)
        return res