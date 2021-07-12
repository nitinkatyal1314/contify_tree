from .core import TreeNode
from settings import ROOT_DIR


class TreeAPI(object):
    """
    This is the API class for the contify custom Tree.
    """

    @staticmethod
    def _create_all_nodes(number_of_nodes: int):
        """
        Creates all nodes for the Tree given the number of nodes.
        :param number_of_nodes: the number of nodes in the Tree
        :type number_of_nodes: int
        :return: list of all nodes
        :rtype: list
        """
        all_nodes = []
        for node_value in range(0, number_of_nodes):
            all_nodes.append(TreeNode(value=node_value))

        return all_nodes

    def _find_node_parent_bfs(self, nodes_to_traverse: list, node_value: int):
        """
        Find the node parent using BFS
        :param nodes_to_traverse: queue of nodes to be traversed
        :type nodes_to_traverse: list
        :param node_value: the value of the node
        :type node_value: int
        :return: the node in the Tree which is the parent of the node with given value
        :rtype: TreeNode
        """
        # get the first item from the list
        node = nodes_to_traverse.pop(0)
        child_matched = False

        for child in node.children:
            if child.value == node_value:
                child_matched = True
                break

        if child_matched:
            return node
        else:
            nodes_to_traverse.extend(node.children)
            return self._find_node_parent_bfs(nodes_to_traverse, node_value)

    def delete(self, root_node: TreeNode, node_value: int):
        """
        Deletes a node from the tree with root node and the value of the node (to be deleted)
        :param root_node: The root node of the tree / subtree
        :type root_node: TreeNode
        :param node_value: the value of the node to be deleted
        :type node_value: int
        :return:
        :rtype:
        """
        if node_value == root_node.value:
            raise Exception("Cant delete the root node.")

        parent_node = self._find_node_parent_bfs([root_node], node_value)
        parent_node.delete_child(node_value)
        print("Node deleted.")

    @staticmethod
    def get_leaf_nodes_count(root_node: TreeNode):
        """
        Get the total number of leaf nodes in the tree given its root node.
        :param root_node: The root node of the tree / subtree
        :type root_node: TreeNode
        :return: the total count of leaf nodes in the Tree
        :rtype: int
        """
        count = [0]
        print("Root node is : ", root_node.value)
        root_node.get_total_leaf_nodes(leaf_nodes_count=count)
        return count[0]

    def parse(self, input_file_path: str = "./input/sample.txt"):
        """

        TODO: Not adding error checks here for now (in interest of time)

        Parses the input text data from the file given its path. The data in the input file is assumed to be
        of format:

        first line : contains the number of nodes in the Tree
        second line: contains the relationship between the nodes, and the info about the root node
        third line: contains the item to be deleted

        :param input_file_path: Relative input file path
        :type input_file_path: str
        :return: The count of leaf nodes after deletion
        :rtype: int
        """
        number_of_nodes = 0
        parent_child_mapping = []
        node_to_delete = None
        file = open(input_file_path, "r")

        line_count = 0
        for line in file.readlines():

            if line_count == 0:
                number_of_nodes = int(line)
            elif line_count == 1:
                parent_child_mapping = line.replace("\n", "").split(" ")
            elif line_count == 2:
                node_to_delete = int(line)

            line_count += 1

        parent_child_mapping = list(map(lambda x: int(x), parent_child_mapping))

        print("Number of nodes in the tree : ", number_of_nodes)
        print("Parent child relationship data (with root node) : ", parent_child_mapping)
        print("Node to delete : ", node_to_delete)
        print("==================================\n")

        root = self._parse(number_of_nodes, parent_child_mapping)
        leaf_nodes_before_delete = self.get_leaf_nodes_count(root)
        print("Total leaf nodes before delete : ", leaf_nodes_before_delete)
        print("==================================\n")

        print("Deleting node : ", node_to_delete)
        self.delete(root, node_to_delete)
        leaf_nodes_after_delete = self.get_leaf_nodes_count(root)
        print("Total leaf nodes after delete : ", leaf_nodes_after_delete)

    def _parse(self, number_of_nodes: int, parent_child_mapping: list):
        """
        Parse input data to create tree using number of nodes and parent child mapping list data
        :param number_of_nodes: the number of nodes in the tree
        :type number_of_nodes: int
        :param parent_child_mapping: list of data defining the child-parent relationship between the nodes.
        :type parent_child_mapping:
        :return: The root node of the tree
        :rtype: TreeNode
        """

        all_nodes = self._create_all_nodes(number_of_nodes)
        root_node = None

        for index in range(0, len(parent_child_mapping)):

            node_value = index
            parent_node_value = parent_child_mapping[index]

            # no exception handling required since node value does not duplicate
            node = list(filter(lambda n: n.value == node_value, all_nodes))[0]

            if parent_node_value == -1:
                root_node = node

            else:
                # get the parent node
                # no exception handling required since node value does not duplicate
                parent_node = list(filter(lambda n: n.value == parent_node_value, all_nodes))[0]
                parent_node.add_child(node)

        if root_node is None:
            raise Exception("Could not create tree. No root node found.")
        else:
            return root_node





