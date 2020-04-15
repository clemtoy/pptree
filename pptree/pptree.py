# -*- coding: utf-8 -*-
"""
Clement Michard (c) 2015
Ettore Forigo (c) 2020
"""

from .utils import *


class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

        if parent:
            self.parent.children.append(self)


def print_tree(current_node, childattr='children', nameattr='name', horizontal=True):
    if hasattr(current_node, nameattr):
        name = lambda node: getattr(node, nameattr)
    else:
        name = lambda node: str(node)

    children = lambda node: getattr(node, childattr)
    nb_children = lambda node: sum(nb_children(child) for child in children(node)) + 1

    def balanced_branches(current_node):
        size_branch = {child: nb_children(child) for child in children(current_node)}

        """ Creation of balanced lists for "a" branch and "b" branch. """
        a = sorted(children(current_node), key=lambda node: nb_children(node))
        b = []
        while a and sum(size_branch[node] for node in b) < sum(size_branch[node] for node in a):
            b.append(a.pop())

        return a, b

    if horizontal:
        print_tree_horizontally(current_node, balanced_branches, name)

    else:
        print_tree_vertically(current_node, balanced_branches, name, children)


def print_tree_horizontally(current_node, balanced_branches, name_getter, indent='', last='updown'):

    up, down = balanced_branches(current_node)

    """ Printing of "up" branch. """
    for child in up:     
        next_last = 'up' if up.index(child) == 0 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', ' ' * len(name_getter(current_node)))
        print_tree_horizontally(child, balanced_branches, name_getter, next_indent, next_last)

    """ Printing of current node. """
    if last == 'up': start_shape = '┌'
    elif last == 'down': start_shape = '└'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '├'

    if up: end_shape = '┤'
    elif down: end_shape = '┐'
    else: end_shape = ''

    print('{0}{1}{2}{3}'.format(indent, start_shape, name_getter(current_node), end_shape))

    """ Printing of "down" branch. """
    for child in down:
        next_last = 'down' if down.index(child) is len(down) - 1 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│', ' ' * len(name_getter(current_node)))
        print_tree_horizontally(child, balanced_branches, name_getter, next_indent, next_last)


def tree_repr(current_node, balanced_branches, name, children):

    sx, dx = balanced_branches(current_node)

    """ Creation of children representation """

    tr_rpr = lambda node: tree_repr(node, balanced_branches, name, children)

    left = branch_left(map(tr_rpr, sx)) if sx else ()
    right = branch_right(map(tr_rpr, dx)) if dx else ()

    children_repr = tuple(
        connect_branches(
            left,
            right
        ) if sx or dx else ()
    )

    current_name = name(current_node)
    
    name_len = len(current_name)
    name_l, name_r = name_len // 2, name_len // 2

    left_len, right_len = blocklen(left), blocklen(right)
    
    current_name = f"{' ' * (left_len - name_l)}{current_name}{' ' * (right_len - name_r)}"

    return multijoin([[current_name, *children_repr]]), (max(left_len, name_l), max(right_len, name_r))


def print_tree_vertically(*args):
    print('\n'.join(tree_repr(*args)[0]))
