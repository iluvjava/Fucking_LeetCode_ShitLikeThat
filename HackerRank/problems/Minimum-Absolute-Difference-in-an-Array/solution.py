def solution(arr):
    arr = sorted(arr)
    return min(abs(I - J) for I, J in zip(arr[:-1], arr[1:]))

  