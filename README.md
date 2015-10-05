# pptree
Python tree pretty-print.

### Import
```python
from pptree import *
```
### Example
```python
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
### Trick
Think about inheritance to use your own node implementation. For example:
```python
class MyNode(Node):
  def __init__(self, filename, owner, ext='', parent=None):
    self.filename = filename
    self.owner = owner
    self.ext = ext
    Node.__init__(self, filename + ext, parent)
```
