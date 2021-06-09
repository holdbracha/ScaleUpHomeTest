import heapq

# O(n + k*log(n))
def selectHeap(list, k):
    if k < 1 or k > len(list):
        raise IndexError
    heapq.heapify(list) # O(n)
    for _ in range(k-1): # k times
        heapq.heappop(list) # O(log(n))
    return heapq.heappop(list)

# O(n + k*log(k))
def selectDoubleHeap(list,k):
	minHeap = list[:k]
	for i in range(k, len(list)):
		heapq._heapify_max(minHeap)
		if (minHeap[0] >= list[i]):
			heapq.heappop(minHeap)
			heapq.heappush(minHeap, list[i])
	return max(minHeap)

