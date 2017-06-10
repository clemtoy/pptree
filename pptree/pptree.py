# -*- coding: utf-8 -*-
"""
Clement Michard (c) 2015
"""

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

        if parent:
            self.parent.children.append(self)


def print_tree(current_node, childattr='children', nameattr='name', indent='', last='updown'):

    if hasattr(current_node, nameattr):
        name = lambda node: getattr(node, nameattr)
    else:
        name = lambda node: str(node)

    children = lambda node: getattr(node, childattr)
    nb_children = lambda node: sum(nb_children(child) for child in children(node)) + 1
    size_branch = {child: nb_children(child) for child in children(current_node)}

    """ Creation of balanced lists for "up" branch and "down" branch. """
    up = sorted(children(current_node), key=lambda node: nb_children(node))
    down = []
    while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
        down.append(up.pop())

    """ Printing of "up" branch. """
    for child in up:     
        next_last = 'up' if up.index(child) is 0 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', ' ' * len(name(current_node)))
        print_tree(child, childattr, nameattr, next_indent, next_last)

    """ Printing of current node. """
    if last == 'up': start_shape = '┌'
    elif last == 'down': start_shape = '└'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '├'

    if up: end_shape = '┤'
    elif down: end_shape = '┐'
    else: end_shape = ''

    print('{0}{1}{2}{3}'.format(indent, start_shape, name(current_node), end_shape))

    """ Printing of "down" branch. """
    for child in down:
        next_last = 'down' if down.index(child) is len(down) - 1 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│', ' ' * len(name(current_node)))
        print_tree(child, childattr, nameattr, next_indent, next_last)

class Employee:

    def __init__(self, fullname, function, head=None):
        self.team = []
        self.fullname = fullname
        self.function = function
        if head:
            head.team.append(self)

    def __str__(self):
        return self.function

if __name__ == "__main__":
    jean = Employee("Jean Dupont", "CEO")
    isabelle = Employee("Isabelle Leblanc", "Sales", jean)
    enzo = Employee("Enzo Riviera", "Technology", jean)
    lola = Employee("Lola Monet", "RH", jean)
    kevin = Employee("Kevin Perez", "Developer", enzo)
    lydia = Employee("Lydia Petit", "Tester", enzo)

    print_tree(jean, "team", "fullname")
