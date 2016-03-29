
# Tree definition
def tree(node, children=[]):
    return lambda dispatch: node if dispatch == 'node' else children

def datum(tree):
    return tree('node')

def children(tree):
    return tree('children')

t = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.
    >>> print_tree(t)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(datum(t)))
    for child in children(t):
        print_tree(child, indent + 1)


def size_of_tree(t):
    """Return the number of entries in the tree.

    >>> print_tree(t)
    1
      2
      3
        4
        5
      6
        7
    >>> size_of_tree(t)
    7
    """
    "*** YOUR CODE HERE ***"
    if children(t) == []:
        return 1
#    else:
#        return 1 + sum([ size_of_tree(child) for child in children(t) ])
    else:
        count = 0
        for child in children(t):
            count += size_of_tree(child)
        return 1 + count
print(size_of_tree(t))


def flatten(t):
    """Return a list of the entries in this tree in the order that they 
    would be visited by a preorder traversal (see problem description).

    >>> flatten(t)
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    if children(t) == []:
        return [datum(t)]
    flattened_children = []
    for child in children(t):
        flattened_children += flatten(child)
    return [datum(t)] + flattened_children
print(flatten(t))



def tree_map(fn, t):
    """Maps the function fn over the entries of tree and returns the 
    result in a new tree.

    >>> print_tree(tree_map(lambda x: 2**x, t))
    2
      4
      8
        16
        32
      64
        128
    """
    "*** YOUR CODE HERE ***"
    if children(t) == []:
        return tree(fn(datum(t)))
    else:
        mapped_children = []
        for child in children(t):
            mapped_children += [ tree_map(fn, child) ]
        return tree(fn(datum(t)), mapped_children)

def tree_map_brillient(fn, t):
    return tree(fn(datum(t)), [ tree_map_brillient(fn, child) for child in children(t) ])
print_tree(tree_map_brillient(lambda x: 2**x, t))
