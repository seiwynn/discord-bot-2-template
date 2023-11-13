

import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Now you can import the module
from utils import message_utils2
# rest of your code


result = message_utils2.split_message("""

Some text before code block
```python\nprint('Hello, world!')
```
```````
more text
```python print('Hello, world!')
```


```python
print('Hello, world!')
```
                                      ``` print('Hello, world!')
```
""")

print(result)
for item in result:
    print(len(item))
    print(item)
