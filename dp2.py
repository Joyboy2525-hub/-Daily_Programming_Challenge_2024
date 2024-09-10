def arrmiss(arr, n):
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    miss_num = total_sum - arr_sum
    print(miss_num)

arr = [1, 2, 4, 5]
n=5
arrmiss(arr,n)

