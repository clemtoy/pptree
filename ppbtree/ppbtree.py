# -*- coding: utf-8 -*-
"""
based on Clement Michard (c) 2015
Vladyslav Khardel (c) 2017
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def add(node, value):
    if node.value is None:
        node.value = value
    else:
        if value <= node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                add(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                add(node.right, value)

def print_tree(current_node, nameattr='value', left_child='left', right_child='right', indent='', last='updown'):

    if hasattr(current_node, nameattr):
        name = lambda node: getattr(node, nameattr)
    else:
        name = lambda node: str(node)

    up = getattr(current_node, left_child)
    down = getattr(current_node, right_child)

    if up is not None:
        next_last = 'up'
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '|', ' ' * len(str(name(current_node))))
        print_tree(up, nameattr, left_child, right_child, next_indent, next_last)

    if last == 'up': start_shape = '┌'
    elif last == 'down': start_shape = '└'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '├'

    if up is not None and down is not None: end_shape = '┤'
    elif up: end_shape = '┘'
    elif down: end_shape = '┐'
    else: end_shape = ''

    print('{0}{1}{2}{3}'.format(indent, start_shape, name(current_node), end_shape))

    if down is not None:
        next_last = 'down'
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '|', ' ' * len(str(name(current_node))))
        print_tree(down, nameattr, left_child, right_child, next_indent, next_last)


if __name__ == "__main__":
    from random import randint
    root = Node()
    for _ in range(15):
        add(root, randint(10, 99))

    print_tree(root)