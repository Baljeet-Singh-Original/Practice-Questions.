
import queue
q = queue.PriorityQueue()

q.put(10)
q.put(5)
q.put(76)
q.put(3)
print(q.get())    # Output : 3
print(q.get())    #Output : 5


