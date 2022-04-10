def shellSort(arr):
  n = len(arr)
  gap = n//2
  while gap > 0:
      for i in range(gap, n):
          temp = arr[i]
          j = i
          while j >= gap and arr[j-gap] > temp:
              arr[j] = arr[j-gap]
              j -= gap
          arr[j] = temp
      gap //= 2
  return arr

def main():
  arr = [21, 32, 17, 2, 51]
  print(shellSort(arr))
main()