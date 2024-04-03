func triangularSum(nums []int) int {
    for i := len(nums) - 1; i > 0; i-- {
        for j := 0; j < i; j++ {
            // sum := nums[j] + nums[j+1]
            // if sum > 9 {
            //     sum = sum %10
            // }
            nums[j] += nums[j+1]
            nums[j] %= 10
        }
    }
    return nums[0]
}
