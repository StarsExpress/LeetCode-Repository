
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root: TreeNode | None) -> str:  # LeetCode Q.297.
    if root is None:
        return "!0+None!0+"
    return _dfs_serialize_nodes(root, 0)


def deserialize(data: str) -> TreeNode | None:
    left_subtree, root, right_subtree = data.split("!0+")
    if root == "None":
        return None

    tree = TreeNode(int(root))
    tree.left = _dfs_deserialize_subtrees(left_subtree, 1)
    tree.right = _dfs_deserialize_subtrees(right_subtree, 1)
    return tree


def _dfs_serialize_nodes(current_node: TreeNode, level: int):
    serialized_subtrees = ""
    if current_node.left:  # Increment level for child node.
        serialized_subtrees += _dfs_serialize_nodes(current_node.left, level + 1)

    current_node_value = str(current_node.val)

    if not current_node.left and not current_node.right and level != 0:  # Single leaf node.
        serialized_subtrees += f"~{current_node_value}~"

    else:  # Not single leaf node.
        serialized_subtrees += f"!{level}+{current_node_value}!{level}+"

    if current_node.right:  # Increment level for child node.
        serialized_subtrees += _dfs_serialize_nodes(current_node.right, level + 1)

    return serialized_subtrees


def _split_subtrees(subtrees: str, separator: str):
    indices = []
    start_idx = subtrees.find(separator)
    while start_idx != -1:
        indices.append(start_idx)
        start_idx += 1
        start_idx = subtrees.find(separator, start_idx)

    left_idx, right_idx = indices
    left_subtrees = subtrees[:left_idx]

    left_idx += len(separator)
    parent_node_value = subtrees[left_idx: right_idx]

    right_idx += len(separator)
    right_subtrees = subtrees[right_idx:]
    return left_subtrees, parent_node_value, right_subtrees


def _dfs_deserialize_subtrees(serialized_subtrees: str, level: int):
    if len(serialized_subtrees) == 0:  # Empty serialized string.
        return None

    if "!" not in serialized_subtrees:  # Serialized subtree is a single leaf node.
        return TreeNode(int(serialized_subtrees.replace("~", "")))

    left_subtrees, parent_node_value, right_subtrees = _split_subtrees(serialized_subtrees, f"!{level}+")

    subtree = TreeNode(int(parent_node_value))
    level += 1  # Increment level for children nodes.
    subtree.left = _dfs_deserialize_subtrees(left_subtrees, level)
    subtree.right = _dfs_deserialize_subtrees(right_subtrees, level)
    return subtree
