#O(n), linear memory
def single_number(nums):
  seen = {}
  for num in nums:
    seen[num] = seen.get(num, 0) + 1

  for num in nums:
    if seen[num] == 1:
      return num

#O(n^2), constant memory
def single_number_q(nums):
  for i in range(len(nums)):
    found = False
    for j in range(i+1, len(nums)):
      if nums[i] == nums[j]:
        found = True
    if not found:
      return nums[i]

if __name__ == '__main__':
  assert single_number([4, 1, 2, 3, 4, 3, 2]) == 1
  assert single_number_q([4, 1, 2, 3, 4, 3, 2]) == 1
