class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
   # make temp array
        tempArr = []
        # make sum var
        sumVar = 0
        # loop as much as much times as nums length
        for i in range(len(nums)):
            # sum the number in sum variable with the num[x] 
            sumVar += nums[i]
            # push sum number into temp array
            tempArr.insert(i, sumVar)
        return tempArr
            