#reverse function
def reverse(arr, start, end):
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    end -= 1
    start += 1


def reverseSentence(A):
    """
    the above function takes in an array of characters, A, and reverses the the "words"
    (not individual characters).
    Example:

    A = ['t','h','i','s',' ','i','s',' ','g','o','o','d'] and
    returns ['g','o','o','d',' ','i','s',' ','t','h','i','s']
    """
    reverse(A, 0, len(A)-1)
    print(A)
    new_start = 0
    new_end = 0
    while new_end < len(A)-1:
        while new_end < len(A)-1 and A[new_end] != ' ':
            new_end += 1
        reverse(A, new_start, new_end)
        new_end += 1
        new_start = new_end
    return A
    print (A)
    
 #still working on a more ideal solution

