class TreeNode(object):
    """
    Represents the node of the custom Tree.

    This tree contains node values as positive integers from 0 -> N-1, where N is the number of nodes.

    The tree is constructed using a list as follows:
    Below is the input list which defines how the nodes in the tree should be connected.
    ex A:  [-1 0 0 1 1]  Here A[i] gives parent node for ith node, where i belongs to 0->N-1,
                         if A[i] == -1, then it is the root node of the tree.
    index:   0 1 2 3 4

    Therefore,
    A[0] is the root node and has value 0
    A[1] & A[2] (Node value 1 and 2) is the child of node A[0] (root node)
    A[3] & A[4] (Node value 3 and 4) is the child of node A[1] (node value 1)


    Note : There will be no duplicates in node values.

    """

    def __init__(self, value: int = 0):
        """
        Initialize tree node with the value, and children.
        """
        self.value = value
        self.children = []

    def add_child(self, child_node):
        """
        Adds child node.
        :param child_node: node to add
        :type child_node: TreeNode
        :return:
        :rtype:
        """
        self.children.append(child_node)

    def delete_child(self, child_node):
        """
        Removes the child node.

        TODO: The API implementation should for create / delete should be same
        :param child_node: deletes a child node given its value
        :type child_node: int
        :return:
        :rtype:
        """
        delete_from_index = None
        for index, node in enumerate(self.children):
            if node.value == child_node:
                delete_from_index = index
                break

        if delete_from_index is not None:
            del self.children[delete_from_index]
        else:
            raise Exception("Element to be deleted not present in Tree")

    def is_leaf(self):
        """
        Checks whether the node is the leaf node.
        :return: Tree if node is a leaf node else false
        :rtype: bool
        """

        if len(self.children) == 0:
            return True
        else:
            return False

    def get_total_leaf_nodes(self, leaf_nodes_count: list):
        """
        Get the number of leaf nodes.
        :param leaf_nodes_count: immutable list containing leaf node count when traversing
        :type leaf_nodes_count: list
        :return:
        :rtype:
        """
        for node in self.children:
            if node.is_leaf():
                print("Traversing node :  ", node.value, "is a leaf node")
                leaf_nodes_count[0] += 1
            else:
                print("Traversing node :  ", node.value, "is not a leaf node")
                node.get_total_leaf_nodes(leaf_nodes_count)











