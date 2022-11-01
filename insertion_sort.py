class solution:
    def insertionSort1(n, arr):
        j = n-1
        store = arr[j]
        
        for i in range(j, -1, -1):
            if store < arr[i-1] and i >= 1:
                arr[i] = arr[i-1]
                print(' '.join(str(x) for x in arr))
            else: 
                arr[i] = store
                print(' '.join(str(x) for x in arr))
                break 
    