def median(arr1, arr2):
  # Approach using merge, O(n) time and O(n) extra space.
  merged = merge(arr1, arr2)
  k = len(merged)
  if k % 2 == 0:
    return (merged[k//2] + merged[(k//2) -1])/2
  return merged[k//2]

def merge(arr1, arr2):
  i = 0
  j = 0
  merged = []

  while i < len(arr1) and j < len(arr2):
    if arr1[i] > arr2[j]:
      merged.append(arr2[j])
      j += 1
    else:
      merged.append(arr1[i])
      i += 1    
  
  while i < len(arr1):
    merged.append(arr1[i])
    i += 1

  while j < len(arr2):
    merged.append(arr2[j])
    j += 1
  
  return merged


if __name__ == '__main__':
  assert median([1,4,7], [2,3,5,6]) == 4
  assert median([10,20,30,40,50],[20,30,40,50,60]) == 35.0
  assert median([1,3,5],[2,4,6]) == 3.5
