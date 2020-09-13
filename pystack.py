class PyStack:
    def __init__(self, size = 20):
        self.stack = []             # 堆疊串列
        self.size = size            # 堆疊大小
        self.top = -1               # 堆疊頂位置
    def setSize(self, size):        # 設定堆疊大小
        self.size = size
    def push(self, element):        # 元素放入堆疊
        if self.isFull():
            raise StackException('PyStackOverflow') 
        else:
            self.stack.append(element)
            self.top = self.top + 1
    def pop(self):                  # 元素移出堆疊
        if self.isEmpty():
            raise StackException('PyStackUnderflow')
        else:
            element = self.stack[-1]
            self.top = self.top - 1
            del self.stack[-1]
            return element
    def Top(self):                  # 取得堆疊頂位置
        return self.top
    def empty(self):                # 清空堆疊
        self.stack = []
        self.top = -1
    def isEmpty(self):              # 是否為空堆疊
        if self.top == -1:
            return True
        else:
            return False
    def isFull(self):              # 是否為滿堆疊
        if self.top == self.size - 1:
            return True
        else:
            return False

class StackException(Exception):   # 自訂例外類別
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return self.data

if __name__ == '__main__':
    stack = PyStack()
    for i in range(10):
        stack.push(i)
    print(stack.Top())
    for i in range(10):
        print(stack.pop())
    stack.empty()
    for i in range(21):
        stack.push(i)


    
