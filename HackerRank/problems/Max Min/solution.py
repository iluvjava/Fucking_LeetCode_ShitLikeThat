def solution_failed1(k, arr):
    arr.sort()
    Unfairness = float("+inf")
    for I in range(0, len(arr) - k):
        Subarr = arr[I: I + k]
        Unfairness = min(Unfairness, max(Subarr) - min(Subarr))
    
    return Unfairness

def solution(k, arr):
    import heapq as heap
    heap.heapify(arr)
    KlenMin, KlenMax= [], []
    for I in range(k):
        KlenMin.append(arr[I])
        KlenMax.append(-arr[I])
    heap.heapify(KlenMin)
    heap.heapify(KlenMax)
    # Keeping the running sum. -------------------------------------------------
    RunningSum = - KlenMax - KlenMin
    for I in range(1, len(arr)):
        RunningSum = min(RunningSum, - KlenMax[0] - KlenMin[0])



    pass


def main():
    pass

if __name__ == "__main__":
    pass