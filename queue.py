class Queue:

    def __init__(self):
        self.queue = list()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            tmp = self.queue[0]
            del (self.queue[0])
            return tmp
        else:
            return None

    def front(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None

    def rear(self):
        if len(self.queue) > 0:
            return self.queue[len(self.queue) - 1]
        else:
            return None

    def __str__(self):
        return str(', '.join(self.queue))


queue = Queue()
for x in "aeiou": queue.enqueue(x.upper())
print(queue)
print(queue.dequeue())
print(queue.front())
print(queue.rear())
print(queue)
