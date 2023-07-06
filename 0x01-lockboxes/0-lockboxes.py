#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
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
