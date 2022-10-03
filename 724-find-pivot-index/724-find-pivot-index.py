class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # make 2 temp array
        leftArr = nums
        rightArr = nums
        
        for i in range(len(nums)):
            # start with leftArr(0:) then to (0:-1) and so on
            # or with rightArr(:-1) then to (1:-1)
            # print(rightArr[i+1:])
            # print(leftArr[:i])
            if sum(rightArr[i+1:]) == sum(leftArr[:i]):
                # print(i)
                return i
        return -1