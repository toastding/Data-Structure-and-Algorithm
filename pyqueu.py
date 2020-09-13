class PyQueue:
    def __init__(self, size = 20):
        self.queue = []         # 佇列
        self.size = size        # 佇列大小
        self.end = -1           # 佇列尾
    def setSize(self, size):
        self.size = size        # 設定佇列大小
    def In(self, element):      # 加入佇列
        if self.end < self.size - 1:
           self.queue.append(element)
           self.end += 1
        else:
            raise QueueException('PyQueueFull')
    def Out(self):              # 移出佇列
        if self.end != -1:
            element = self.queue[0]
            self.queue = self.queue[1:]
            self.end = self.end - 1
            return element
        else:
            raise QueueException('PyQueueEmpty')
    def End(self):              # 輸出佇列尾
        return self.end 
    def empty(self):            # 清除佇列
        self.queue = []
        self.end = -1
class QueueException(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return self.data
    
if  __name__ == "__main__":
    queue = PyQueue()
    for i in range(10):
        queue.In(i)
    print(queue.End())
    for i in range(10):
        print(queue.Out())
    for i in range(20):
        queue.In(i)
    queue.empty()
    for i in range(20):
        print(queue.Out())