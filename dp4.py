def merge(arr1, arr2, m, n):
    for i in range(m-1, -1, -1):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            first = arr2[0]
            k = 1
            while k < n and arr2[k] < first:
                arr2[k-1] = arr2[k]
                k += 1
            arr2[k-1] = first
            
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
m = len(arr1)
n = len(arr2)

merge(arr1, arr2, m, n)
arr1.sort()
arr2.sort()

print("Merged arr1:", arr1)
print("Merged arr2:", arr2)
