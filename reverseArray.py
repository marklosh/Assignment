def reverseArray(A):
    """
    the above function takes in an array as an argument
    then reverses it in-place
    return type: reversed array
    """
    pointer1=0
    pointer2=len(A)-1
    while pointer2>pointer1:
        A[pointer1], A[pointer2] = A[pointer2], A[pointer1]
        pointer2 -= 1
        pointer1 += 1
    return A
##output
print(reverseArray[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
        
