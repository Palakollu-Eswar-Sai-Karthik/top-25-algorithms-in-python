def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            return True
        i = i+1
    return False


list = [21,5,74,12,49,88]
n = int(input("Enter searching element"))
if search(list,n):
    print("Element found")
else:
    print("element not found")