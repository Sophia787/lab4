def n_nums(nums):
    n = 0
    for i in nums:
        n += 1
    return n
       
def is_monotonic(nums):
    k = 0

    bool = True
    while k < (n_nums(nums) - 2):
        if bool == True:
            if nums[k] <= nums[k+1] <= nums[k+2]:
                k += 1                
            else:
                if nums[k] >= nums[k+1] >= nums[k+2]:
                    k += 1
                else:
                    bool = False
                    k += 1
        else:
            break
    return bool
