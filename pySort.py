class Btree:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
    def insertLeft(self, value):
        self.left = Btree(value)
        return self.left
    def insertRight(self, value):
        self.right = Btree(value)
        return self.right
    def show(self):
        print(self.data)

def inorder(node):              # 中序檢查
    if node.data:
        if node.left:
            inorder(node.left)
        node.show()
        if node.right:
            inorder(node.right)
        
def rinorder(node):              # 中序檢查, 先檢查右子樹
    if node.data:
        if node.right:
            rinorder(node.right)
        node.show()
        if node.left:
            rinorder(node.left)

def insert(node, value):
    if value > node.data:
        if node.right:
            insert(node.right, value)
        else:
            node.insertRight(value)
    else:
        if node.left:
            insert(node.left, value)
        else:
            node.insertLeft(value)

if __name__ == "__main__":
    l = [3, 5, 7, 20, 43, 2, 15, 30]
    Root = Btree(l[0])
    node = Root
    for i in range(1, len(l)):
        insert(Root, l[i])
    print('*****************************')
    print('           從小到大')
    inorder(Root)
    print('*****************************')
    print('           從大到小')
    rinorder(Root)