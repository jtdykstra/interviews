def binarySearch(arr, l, r, x): 
    print(arr) 
    print(x)
    while l <= r: 
  
        mid = l + (r - l) // 2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element 
    # was not present 
    return -1


arr = [9,12,-1,-22,96]
arr.sort()
print(arr)
print("bin serach 12")
print(binarySearch(arr, 0, len(arr) - 1, 12))
print("bin serach 9")
print(binarySearch(arr, 0, len(arr) - 1, 9))
print("bin serach 96")
print(binarySearch(arr, 0, len(arr) - 1, 96)) 
print("bin serach 84")
print(binarySearch(arr, 0, len(arr) - 1, 84)) 
