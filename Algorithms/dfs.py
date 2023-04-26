from tree import TreeNode


def dfs(root: TreeNode, goal, path=()):
    path = path + (root,)  # Initial path

    if root.value == goal:  # Base case
        return path

    for child in root.children:
        path_found = dfs(child, goal, path)  # Recursive step

        if path_found is not None:  # Return path if path exists
            return path_found

    return None  # Return None if goal not found
