def kthElement(Arr1, Arr2, k):
    Arr1 += Arr2 

    sortedArray = merge_sort(Arr1)

    if k-1 >0 and k <= len(sortedArray):
        return sortedArray[k-1]


def merge_sort(arr):

    if len(arr)<=1:     
        return arr

    mid = len(arr)//2

    leftArray = merge_sort(arr[:mid])
    rightArray = merge_sort(arr[mid:])

    return merge(leftArray, rightArray)
    

def merge(left, right):
    i = 0
    j = 0 

    mergedArray = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            mergedArray.append(left[i])
            i += 1
        else:
            mergedArray.append(right[j])
            j += 1
    
    mergedArray += left[i:]
    mergedArray += right[j:]

    
    return mergedArray

