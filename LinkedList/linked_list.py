class Node():
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
    
    def append(self, dataval):
        node = self
        while node.nextval:
            node = node.nextval
        
        node.nextval = Node(dataval)
    
    def link_end_to_first(self):
        node = self
        while node.nextval:
            node = node.nextval
        
        node.nextval = self

def get_node(head, val):
    node = head
    while node.nextval and id(node.nextval) != id(head) and node.dataval != val:
        node = node.nextval

    if node.dataval == val:
        return node
    
    return None

# O(n)
def check_circular_list(head):
    node = head
    while node.nextval and id(node.nextval) != id(head):
        node = node.nextval

    return node.nextval is not None

# O(n + m)
def check_lists_merging(head1, head2):
    last_node = head1
    while last_node.nextval and id(last_node.nextval) != id(head1):
        last_node = last_node.nextval
    
    node2 = head2
    while True:
        if id(node2) == id(last_node):
            return True

        if not node2.nextval or id(node2.nextval) == id(head2):
            return False

        node2 = node2.nextval



        
