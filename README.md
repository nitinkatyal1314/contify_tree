# Custom Tree implementation for contify

# Requirements
1. python >=3.8.10 (use conda environment or virtualenv)

# How to run

1. Clone the repo using
```bash
git clone https://github.com/nitinkatyal1314/contify_tree.git
```

2. The input file is present inside input/sample.txt, and used by default to run the sample Edit this file for multiple use cases.

3. Run the program inside python shell
```python
from tree import TreeAPI

// initialize the api
api = TreeAPI()

// parse the input data to execute
api.parse()
```

# Understanding Sample input
The input file located at input/sample.txt contains 3 lines indicating the following:
1. First line tells the number of nodes in the Tree
2. Second line tells which node is the root node and the parent node for other nodes
2. Third line tells the node to be deleted

The program will print the leaf nodes before and after the delete operation.
