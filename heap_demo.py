import heapq

data = [10, 20, 41, 4, 5, 65, 32, 71, 1, 3]
print(sorted(data))

# why heap if above is sufficient
#because if we insert new data, we have to go through sorting again and that will increase run time complexity

#in heap , element is inserted at the end and then heapify operation is performed which has logrithmic complexity
#so we convert this data to heap

heapq.heapify(data)
#in first glance it will not make sense howevere the heapified data looks like
# child are decided as below
#if i is the index of the node
#first child node-2*i +1
#when pasted heapified data , with left to right order, it will make min heap structure
print(data)
#this is also priority queue as when I look for data , i will get it in order of priority
#removing an element from the heap
print(heapq.heappop(data))
#after this structure would be heapified again
print(data)

#adding the value to heap
print(heapq.heappush(data,2))
#element is pushed and structure is heapified again

print(data)
print(heapq.heappush(data,19))
print(data)

#this i s all a min heap and how do I turn into a max heap as heapq offers minheap

heapq._heapify_max(data)
print(data)


