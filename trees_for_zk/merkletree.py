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

    def get_proof(self, data):
        """Get the proof (Merkle path) for a given piece of data."""
        index = self.leaves.index(self.hash_data(data))
        proof = []

        for level in self.tree[:-1]:  # Exclude the root level
            if index % 2 == 0:  # Even index
                # Pair with the next element
                sibling_index = index + 1 if index + 1 < len(level) else index
            else:  # Odd index
                # Pair with the previous element
                sibling_index = index - 1

            proof.append((level[sibling_index], 'left' if index % 2 == 1 else 'right'))
            index = index // 2

        return proof

    def verify(self, data, proof, root):
        """Verify a piece of data against the given Merkle root."""
        current_hash = self.hash_data(data)

        for sibling_hash, direction in proof:
            print(current_hash)
            if direction == 'left':
                current_hash = self.hash_data(sibling_hash + current_hash)
            else:
                current_hash = self.hash_data(current_hash + sibling_hash)
                
        print(current_hash)
        return current_hash == root

# Example usage
if __name__ == "__main__":
    data_list = ["block1", "block2", "block3", "block4"]
    merkle_tree = MerkleTree(data_list)

    print("Merkle Tree: [")
    for level in merkle_tree.get_tree():
        print(level, end=",\n")
    print("]")

    our_root = merkle_tree.get_root()
    if our_root is not None:
        print("\nRoot of the Merkle Tree:", our_root, "\n")
        print("Length of the Root of the Merkle Tree:", len(our_root), "\n")
    else:
        print("Merkle Tree is empty; no root exists.")

    # Example of verifying a leaf
    data_to_verify = "block2"
    proof = merkle_tree.get_proof(data_to_verify)
    is_valid = merkle_tree.verify(data_to_verify, proof, merkle_tree.get_root())

    print(f"\nIs '{data_to_verify}' in the tree? {'Yes' if is_valid else 'No'}")

