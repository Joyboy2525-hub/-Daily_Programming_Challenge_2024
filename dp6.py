def find_zero_sum_subarrays(arr):
    sum_dict = {}
    result = []
    cum_sum = 0
    for i in range(len(arr)):
        cum_sum += arr[i]
        if cum_sum == 0:
            result.append((0, i))
        if cum_sum in sum_dict:
            for start_idx in sum_dict[cum_sum]:
                result.append((start_idx + 1, i))
        if cum_sum in sum_dict:
            sum_dict[cum_sum].append(i)
        else:
            sum_dict[cum_sum] = [i]
    
    return result


arr =  [1, 2, -3, 3, -1, 2]
zero_sum_subarrays = find_zero_sum_subarrays(arr)
print("Subarrays with sum zero:", zero_sum_subarrays)
