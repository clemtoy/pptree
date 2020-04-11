# pptree
This package allows to pretty-print a tree of python objects.

### Install
```
pip install pptree
```
or
```
easy_install pptree
```

### Documentation
This package provides:
- a default `Node` implementation
- a `pretty_print` function accepting a default `Node` or custom node as root

#### The Node class
```python
__init__(self, name, parent=None)
```
- the name of the node to print
- the parent `Node` object *(optional)*

#### The pretty-print function
```python
print_tree(current_node, childattr='children', nameattr='name', horizontal=True)
```

- the root node object
- the name of the list containing the children *(optional)*
- the name of the field containing the text to display. If `nameattr` is not filled and the custom node don't have any `name` field, then the `str` function is used.  *(optional)*
- whether to print the tree horizontally or vertically *(optional)*

### Example using provided `Node` class
```python
from pptree import *

shame = Node("shame")

conscience = Node("conscience", shame)
selfdisgust = Node("selfdisgust", shame)
embarrassment = Node("embarrassment", shame)

selfconsciousness = Node("selfconsciousness", embarrassment)
shamefacedness = Node("shamefacedness", embarrassment)
chagrin = Node("chagrin", embarrassment)
discomfiture = Node("discomfiture", embarrassment)
abashment = Node("abashment", embarrassment)
confusion = Node("confusion", embarrassment)
  
print_tree(shame)
```
Output:
```
     ┌conscience
     ├self-disgust
shame┤
     │             ┌self-consciousness
     │             ├shamefacedness
     │             ├chagrin
     └embarrassment┤
                   ├discomfiture
                   ├abashment
                   └confusion
```

### Example using custom node implementation
```python
class Employee:

    def __init__(self, fullname, function, head=None):
        self.fullname = fullname
        self.function = function
        self.team = []
        if head:
            head.team.append(self)

    def __str__(self):
        return self.function
```

```python
jean = Employee("Jean Dupont", "CEO")
isabelle = Employee("Isabelle Leblanc", "Sales", jean)
enzo = Employee("Enzo Riviera", "Technology", jean)
lola = Employee("Lola Monet", "RH", jean)
kevin = Employee("Kevin Perez", "Developer", enzo)
lydia = Employee("Lydia Petit", "Tester", enzo)
```
```python
>>> print_tree(jean, "team")

    ┌Sales
    ├RH
 CEO┤
    │          ┌Developer
    └Technology┤
               └Tester

>>> print_tree(jean, "team", "fullname")

            ┌Isabelle Leblanc
            ├Lola Monet
 Jean Dupont┤
            │            ┌Kevin Perez
            └Enzo Riviera┤
                         └Lydia Petit
```

### Example printing tree vertically
```python
from pptree import *

shame = Node("shame")

conscience = Node("conscience", shame)
selfdisgust = Node("selfdisgust", shame)
embarrassment = Node("embarrassment", shame)

selfconsciousness = Node("selfconsciousness", embarrassment)
shamefacedness = Node("shamefacedness", embarrassment)
chagrin = Node("chagrin", embarrassment)
discomfiture = Node("discomfiture", embarrassment)
abashment = Node("abashment", embarrassment)
confusion = Node("confusion", embarrassment)
  
print_tree(shame, horizontal=False)
```
Output:
```
                       shame                                                                                     
    ┌─────────────┬──────┴─────────────────────────────────────────────┐                                         
conscience   selfdisgust                                             embarrassment                               
                                      ┌─────────────────┬─────────────┬────┴─────┬───────────┬────────────┐      
                              selfconsciousness   shamefacedness   chagrin   confusion   abashment   discomfiture
```
