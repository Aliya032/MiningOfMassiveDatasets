class SimpleBloomFilter():
    def __init__(self, size=1000, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def add(self, item):
        hashes = [(hash(item) + i) % self.size for i in range(self.hash_count)]
        for h in hashes:
            self.bit_array[h] = 1

    def check(self, item):
        hashes = [(hash(item) + i) % self.size for i in range(self.hash_count)]
        return all(self.bit_array[h] for h in hashes)

# Example usage
bloom = SimpleBloomFilter()
bloom.add("hello")
print(bloom.check("hello"))  # True
print(bloom.check("world"))  # False (probably)