def checkPossibility(nums):
  count = 0
  for index in range(len(nums)-1):
    if nums[index] > nums[index+1]:
      count += 1

      if index > 0:
        if nums[index-1] <= nums[index+1]:
          nums[index] = nums[index-1]
        else:
          nums[index+1] = nums[index]
                        
    if count > 1:
      return False
        
  return True


if __name__ == '__main__':
  assert checkPossibility([4, 2, 3])
  assert not checkPossibility([3, 4, 2, 3])
  assert checkPossibility([13, 4, 7])
  assert not checkPossibility([5, 1, 3, 2, 5])

'''
Steps of this algorithm:
  [5, 1, 3, 2, 5]
  count = 0

index = 0
[5_, 1, 3, 2, 5]
  5 > 1 ? yes
    count = 1

index = 1
[5, 1_, 3, 2, 5]
  1 > 3 ? no
    count = 1

index = 2
[5, 1, 3_, 2, 5]
  3 > 2 ? yes
    
    count = 2

count > 1 ? yes
  return False

'''
