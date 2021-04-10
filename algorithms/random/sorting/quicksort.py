def quicksort(nums):
    quicksort_helper(nums, 0, len(nums)-1)

def quicksort_helper(nums, low, high):
    if low < high:
        p = partition(nums, low, high)
        quicksort_helper(nums, low, p-1)
        quicksort_helper(nums, p+1, high)

''' partition implemented iteratively '''
def partition(nums, low, high):
    pivot = nums[high]
    i = low-1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1 

''' 
    partition with list comprehension
    since python hasn't immutable data structures, this will cost much more space.
'''
def partition2(nums):
    pivot = nums[0]
    times = len([x for x in nums if x == pivot])
    return [x for x in nums if x < pivot] + [pivot]*times + [x for x in nums if x > pivot]

if __name__ == '__main__':
    sample = [8, 3, 1, 4, 7, 2, 5]
    sample2 = [1, 2, 3, 4, 5, 6]
    sample3 = [9, 8, 3, 6, 7, 4, 10, 2, 5]
    sample4 = [12,5,2,8,12,12,12,22,34,0,5,12]

    quicksort(sample)
    quicksort(sample2)
    quicksort(sample3)
    quicksort(sample4)
    print(sample)
    print(sample2)
    print(sample3)
    print(sample4)
