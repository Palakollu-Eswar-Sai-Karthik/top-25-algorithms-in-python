def search(arr,n):
    
    start = 0
    end = len(arr)-1
    mid = round((start + end)/2)
    while start <= end:
        if arr[mid] == n:
            return True
        elif arr[mid] < n:
            start = mid + 1
            end = end
            mid = round((start + end)/2)
        elif arr[mid] > n:
            start = start
            end = mid - 1
            mid = round((start + end)/2)
    return False


arr = [2,7,9,11,20,25,27,50,51,60]
n = int(input("Enter element you want to search"))
if search(arr,n):
    print("Element found")
else:
    print("element not found")