## Usage

1_Add the following text to introduce the code snippet:_

```python
def canUnlockAll(boxes):
    # Create a list to keep track of visited boxes
    visited = [False] * len(boxes)
    visited[0] = True  # Mark the first box as visited
    
    # Create a queue to perform BFS
    queue = [0]  # Start with the first box
    
    # Perform BFS
    while queue:
        current_box = queue.pop(0)
        # Check all the keys in the current box
        for key in boxes[current_box]:
            if key >= 0 and key < len(boxes) and not visited[key]:
                visited[key] = True
                queue.append(key)
    
    # Check if all boxes have been visited
    return all(visited)

```

2_Add the example usage below the code snippet:_

```python
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False


```

