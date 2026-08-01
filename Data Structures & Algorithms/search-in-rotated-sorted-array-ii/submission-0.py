class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        leftPointer, rightPointer = 0, len(nums) - 1

        while leftPointer <= rightPointer:
            middlePointer = (leftPointer + rightPointer) // 2

            if target == nums[middlePointer]:
                return True
            
            if nums[leftPointer] == nums[rightPointer] == nums[middlePointer]:
                leftPointer += 1
                rightPointer -= 1
                continue
            
            #left portion
            if nums[leftPointer] <= nums[middlePointer]:
                if target >= nums[leftPointer] and target < nums[middlePointer]:
                    rightPointer = middlePointer - 1
                else:
                    leftPointer = middlePointer + 1
                
            else:
                if target <= nums[rightPointer] and target > nums[middlePointer]:
                    leftPointer = middlePointer + 1

                else:
                    rightPointer = middlePointer - 1

        return False
