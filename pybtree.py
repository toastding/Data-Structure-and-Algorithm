class BTree:                        # 二元樹節點
    def __init__(self, value):      # 初始化函數
        self.left = None            # 左子樹
        self.data = value           # 節點值
        self.right = None           # 右子樹
    
    def insertLeft(self, value):    # 向左子樹插入節點
        self.left = BTree(value)
        return self.left
    
    def insertRight(self, value):   # 向右子樹插入節點
        self.right = BTree(value)
        return self.right
    
    def show(self):                 # 輸出節點資料
        print(self.data)
    

if __name__ == "__main__":
    Root = BTree('Root')            # 根節點
    A = Root.insertLeft('A')        # 像根節點中插入A節點
    C = A.insertLeft('C')
    D = A.insertRight('D')
    F = D.insertLeft('F')
    G = D.insertRight('G')
    B = Root.insertRight('B')
    E = B.insertRight('E')
    Root.show()                     # 輸出節點資料
    Root.left.show()
    Root.right.show()
    A = Root.left
    A.left.show()
    Root.left.right.show()