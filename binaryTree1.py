class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_min(self):
        if self.left != None:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right != None:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        return sum(self.in_order_traversal)

    def post_order_traversal(self):
        elements: list[Any] = []
        self.left.post_order_traversal()
        self.right.post_order_traversal()

    def pre_order_traversal(self):
        pass


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    '''
    1. find_min(): finds minimum element in entire binary tree
    2. find_max(): finds maximum element in entire binary tree
    3. calculate_sum(): calcualtes sum of all elements
    4. post_order_traversal(): performs post order traversal of a binary tree
    5. pre_order_traversal(): perofrms pre order traversal of a binary tree
    '''

    print(f'\n1. Minimum: {numbers_tree.find_min()}')
    print(f'\n2. Maximum: {numbers_tree.find_max()}')
    print(f'\n3. Sum: {numbers_tree.calculate_sum()}')
    print(f'\n4. Post-Order: {numbers_tree.post_order_traversal()}')
    print(f'\n5. Pre-Order: {numbers_tree.pre_order_traversal()}')
