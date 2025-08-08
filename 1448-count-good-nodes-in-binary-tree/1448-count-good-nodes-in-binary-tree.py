class Solution(object):
    def goodNodes(self, root):
        def dfs(node, biggest):
            if node is None:
                return 0  # no node here

            # Is this node good?
            if node.val >= biggest:
                count = 1  # yes, it's good
            else:
                count = 0  # no, it's not good

            # Update biggest value so far
            biggest = max(biggest, node.val)

            # Check left and right sides
            count += dfs(node.left, biggest)
            count += dfs(node.right, biggest)

            return count

        return dfs(root, root.val)  # start with root's value

