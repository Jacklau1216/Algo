#counting inversion number

#a sorted array may not contain inversion number
# [1,2,3,4,5,6] => no inersion number


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
  temp = []
  starting = start1
  while start1 < end1 or start2 < end2:
    if start1 == end1:
      temp += arr[start2:end2]
      start2 = end2 + 1
    elif start2 == end2:
      temp.append(arr[start1])
      num += end1-start1
      start1 += 1
    elif arr[start1] < arr[start2]:
      temp.append(arr[start1])
      start1 += 1
    else:
      temp.append(arr[start2])
      start2 += 1
      num += end1 - start1
  arr[starting:end2] = temp
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

testing = [1,5,4,8,10,2,6,9,12,11,3,7]
testing1 = [1,5,4,8,10]

print(count(testing1, 0, len(testing1)))
print(testing1)
"""
print(count(testing, 0 , len(testing)))
print(testing)
"""



"""
temp = len(testing)
print(inversion(testing, 0, temp//2))
print(inversion(testing, temp//2, temp))
print(testing)
print(merge(testing, 0, temp//2, temp//2, temp))
print(testing)

#it can count the inversion as 5 + 8 + 9
"""
