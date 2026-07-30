class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right  = 0, len(nums) - 1 

        while left <= right:
            # Calculating the middle index
            mid = left + (right - left) // 2 

            # Target is found
            if(nums[mid] == target):
                return mid
            # Target is larger
            elif(nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        return -1