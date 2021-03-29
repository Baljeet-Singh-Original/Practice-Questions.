
def isEmpty(queue):
    if not queue:
        return True
    else:
        return False

def enqueue(queue, n):
    queue.append(n)
    return queue

def dequeue(queue):
    if isEmpty(queue):
        print("queue is empty")
        return False
    else:
        queue.pop(0)
        return queue
