#counting inversion number

#a sorted array may not contain inversion number
# [1,2,3,4,5,6] => no inersion number
"""
"""
testing = [1,5,4,8,10,2,6,9,12,11,3,7]

def inversion(arr, start, end):
  num = 0
  for i in range(start, end):
    temp = arr[i]
    for j in range(i-1, start-1, -1):
      if temp < arr[j]:
        arr[j+1], arr[j] = arr[j], temp
        num += 1
  return num

def merge(arr, start1, end1, start2, end2):
  num = 0
  return num

def count(arr, start, end):
  # print('Counting inversion number in the list')
  length = end - start
  sum = 0
  if length > 2:
    temp = (end - start) // 2
    sum += count(arr, start, end - temp)
    sum += count(arr, start + temp, end)
    sum += merge(arr, start, end-temp, start+temp, end)
    return sum
  else:
    return inversion(arr, start, end)

print(count(testing, 0 , len(testing)))
print(testing)