class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        hashTable = {}
        dup = 0
        for i in range(len(nums)):
            if nums[i] in hashTable:
                dup = nums[i]
            else:
                hashTable[nums[i]] = i
        return dup