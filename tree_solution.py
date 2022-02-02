
def find_internal_nodes_num(tree):
    if not isinstance(tree, list):
        raise ValueError('Expected tree to be of tyle list(int)')
    
    records = {} # {node: has_children? }
    for node, _ in enumerate(tree):
        for _, parent in enumerate(tree):
            has_children = False
            if node == parent:
                has_children = True
                break
        records.update({node: has_children})
    
    records_internal_nodes = dict(filter(lambda record: record[1], records.items())) # dict of nodes that have child(ren)
    return list(records_internal_nodes.keys())  


if __name__ == '__main__':
    my_tree = [4, 4, 1, 5, -1, 4, 5]
    print('Given tree: ', my_tree)
    print('internal nodes: ', find_internal_nodes_num(my_tree))

    tree2 = [7, 0, 3, 7, 5, 7, 4, -1, 0]
    print('Another tree: ', tree2)
    print('internal nodes: ', find_internal_nodes_num(tree2))
