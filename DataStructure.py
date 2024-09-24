import time
import math

# Dynamic Array Class with Different Growth Strategies
class DynamicArray:
    def __init__(self, growth_strategy):
        self.array = [None] * 2  # Start with size 2
        self.capacity = 2  # Current capacity of the array
        self.size = 0  # Current number of elements in the array
        self.growth_strategy = growth_strategy  # The chosen growth strategy

    def append(self, value):
        if self.size == self.capacity:
            self._resize()

        # Insert using binary search
        self._binary_insert(value)

    def _resize(self):
        # Implement different growth strategies here
        if self.growth_strategy == 'incremental':
            new_capacity = self.capacity + 10
        elif self.growth_strategy == 'doubling':
            new_capacity = self.capacity * 2
        elif self.growth_strategy == 'fibonacci':
            new_capacity = self.capacity + self._fibonacci(self.capacity)
        else:
            raise ValueError("Invalid growth strategy!")

        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity
        print(f"Resized to: {self.capacity}")

    def _fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return self._fibonacci(n - 1) + self._fibonacci(n - 2)

    def _binary_insert(self, value):
        # Insert while maintaining the array sorted using binary search
        low, high = 0, self.size - 1

        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] is None or self.array[mid] < value:
                low = mid + 1
            else:
                high = mid - 1

        # Shift elements to make space for the new element
        for i in range(self.size, low, -1):
            self.array[i] = self.array[i - 1]

        self.array[low] = value
        self.size += 1

    def print_status(self):
        print(f"Size: {self.size}, Capacity: {self.capacity}")
        if self.size > 0:
            quarter = self.size // 4
            half = self.size // 2
            three_quarters = 3 * self.size // 4
            print(f"Elements: {self.array[0]} -> {self.array[quarter]} -> {self.array[half]} -> {self.array[three_quarters]} -> {self.array[self.size - 1]}")

# Function to load the EOWL dataset
def load_eowl_dataset(file_path):
    with open(file_path, 'r') as f:
        words = [line.strip() for line in f.readlines()]  # Read and strip each line to remove newline characters
    return words

# Function to measure performance of the dynamic array
def measure_performance(array, words):
    start_time = time.time()  # Start time for the entire insertion process
    for i, word in enumerate(words):
        array.append(word)
        if (i + 1) % array.capacity == 0:  # After each resize
            elapsed_time = time.time() - start_time
            print(f"\nInsertions: {i + 1}, Time elapsed: {elapsed_time:.6f} seconds")
            array.print_status()

# Function to measure performance of Python's built-in list
def measure_python_list_performance(words):
    py_list = []
    start_time = time.time()
    for i, word in enumerate(words):
        py_list.append(word)
        if (i + 1) % 10 == 0:  # After every 10 insertions
            elapsed_time = time.time() - start_time
            print(f"\nInsertions: {i + 1}, Time elapsed: {elapsed_time:.6f} seconds")

# MAIN EXECUTION

# Load the dataset
file_path = '/Users/soundarya/Downloads/words.txt' # Correct path to your dataset file
words = load_eowl_dataset(file_path)  # Load the words from the file
print(f"Loaded {len(words)} words from the dataset.")  # Output the number of words

# Test Dynamic Array with Incremental Strategy
array_incremental = DynamicArray('incremental')
print("\n\n -----*****----- Testing Incremental Strategy: -----*****----- ")
measure_performance(array_incremental, words[:50])

# Test Dynamic Array with Doubling Strategy
array_doubling = DynamicArray('doubling')
print("\n\n -----*****----- Testing Doubling Strategy: -----*****----- ")
measure_performance(array_doubling, words[:50])

# Test Dynamic Array with Fibonacci Strategy
array_fibonacci = DynamicArray('fibonacci')
print("\n\n -----*****----- Testing Fibonacci Strategy: -----*****----- ")
measure_performance(array_fibonacci, words[:50])

# Test Python's Built-in List
print("\n -----*****----- Testing Python's Built-in List: -----*****----- ")
measure_python_list_performance(words[:50])

