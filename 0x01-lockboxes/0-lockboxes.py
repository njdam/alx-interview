#!/usr/bin/python3
# Alx-interview for determining if all the boxes can be opened


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes: A list of lists representing the boxes and their corresponding keys.

    Returns:
    - True if all boxes can be opened, else False.
    """
    canUnlockAll = False
    keys = {0: True}


    n_boxes = len(boxes)
    while(True):

        n_keys = len(keys)

        # Iterate to check boxes if have all keys which can unlock all
        for i in range(len(boxes)):
            if boxes[i] and keys.get(i, False):
                for j in boxes[i]:
                    if j < n_boxes:
                        keys[j] = True
                    boxes[i] = None

        if not(len(keys) > n_keys):
            break

    if n_keys == len(boxes):
        canUnlockAll = True

    # If all boxes have been visited, return True.
    return canUnlockAll
