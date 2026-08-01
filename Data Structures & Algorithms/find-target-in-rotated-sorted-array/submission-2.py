class Solution:
    def search(self, nums: List[int], target: int) -> int:

        leftPointer, rightPointer = 0, len(nums) - 1

        while leftPointer <= rightPointer:
            middlePointer = (leftPointer + rightPointer) // 2

            if nums[middlePointer] == target:
                return middlePointer
            
            # Left Portion [4,5,6,7]
            if nums[leftPointer] <= nums[middlePointer]:
                if target < nums[leftPointer]:
                    leftPointer = middlePointer + 1
                elif target > nums[middlePointer]:
                    leftPointer = middlePointer + 1
                else:
                    rightPointer = middlePointer - 1
            #Right Portion [0,1,2]
            else:
                if target < nums[middlePointer]:
                    rightPointer = middlePointer - 1
                elif target > nums[rightPointer]:
                    rightPointer = middlePointer - 1
                else:
                    leftPointer = middlePointer + 1

        return -1


