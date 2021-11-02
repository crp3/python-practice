def twoSum(nums, target):
	seen = {}
	for i in range(len(nums)):
    	num = nums[i]
    	if target - num in seen:
       		return True
    	seen[num] = i
  	return False
