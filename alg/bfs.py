from collections import deque
from tree import TreeNode


def bfs(root: TreeNode, goal):
    path_queue = deque()  # Initialize frontier queue

    initial_path = [root]  # Add root path to the frontier
    path_queue.appendleft(initial_path)

    while path_queue:  # As long as there are paths in the frontier
        current_path = path_queue.pop()  # Get the next path in the frontier
        current_node = current_path[-1]  # Get the visited node

        if current_node.val == goal:  # Check if the goal node is found
            return current_path

        # If node not found yet
        for child in current_node.children:  # Add paths to children to the frontier
            new_path = current_path[:]
            new_path.append(child)
            path_queue.appendleft(new_path)

    return None  # Return None if goal not found
