import node


def inorder(tree):
    assert isinstance(tree, node.Node)
    if tree.left is not None:
        inorder(tree.left)
    # Do something
    print(tree.val)
    if tree.right is not None:
        inorder(tree.right)


def preorder(tree):
    assert isinstance(tree, node.Node)
    # Do something
    print(tree.val)
    if tree.left is not None:
        preorder(tree.left)
    if tree.right is not None:
        preorder(tree.right)


def postorder(tree):
    assert isinstance(tree, node.Node)
    if tree.left is not None:
        postorder(tree.left)
    if tree.right is not None:
        postorder(tree.right)
    # Do something
    print(tree.val)


def level_traversal(tree):
    assert isinstance(tree, node.Node)
    for i in range(1, 4):
        one_level(tree, i)


def one_level(tree, level):
    assert isinstance(tree, node.Node)
    if tree is not None:
        if level == 1:
            # Do something
            print(tree.val)
        elif level > 1:
            one_level(tree.left, level - 1)
            one_level(tree.right, level - 1)
