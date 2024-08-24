import hashlib

class MerkleTree:
    def __init__(self, data_list):
        self.leaves = [self.hash_data(data) for data in data_list]
        self.tree = self.build_tree(self.leaves)

    def hash_data(self, data):
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def build_tree(self, leaves):
        tree = []
        current_level = leaves

        while len(current_level) > 1:
            tree.append(current_level)
            next_level = []

            # Combine pairs of nodes and hash them to create the parent nodes
            for i in range(0, len(current_level), 2):
                left_child = current_level[i]
                if i + 1 < len(current_level):
                    right_child = current_level[i + 1]
                else:
                    # If there's an odd number of nodes, duplicate the last one
                    right_child = left_child
                combined_hash = self.hash_data(left_child + right_child)
                next_level.append(combined_hash)

            current_level = next_level

        tree.append(current_level)  # The root of the tree
        return tree

    def get_root(self):
        return self.tree[-1][0] if self.tree else None

    def get_tree(self):
        return self.tree

# Example usage
if __name__ == "__main__":
    data_list = ["block1", "block2", "block3", "block4"]
    merkle_tree = MerkleTree(data_list)

    print("Merkle Tree: [")
    for level in merkle_tree.get_tree():
        print(level, end=",\n")
    print("]")

    print("\nRoot of the Merkle Tree:", merkle_tree.get_root())
