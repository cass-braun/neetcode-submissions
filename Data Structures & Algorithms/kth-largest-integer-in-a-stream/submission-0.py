import heapq
class KthLargest:
    class MinHeap:
        def __init__(self):
            self.heap = []

        def __len__(self):
            return len(self.heap)

        def peek(self) -> int:
            """Returns the minimum element without removing it."""
            if not self.heap:
                raise IndexError("Heap is empty")
            return self.heap[0]

        def push(self, val: int):
            """Adds a new value to the heap and restores the heap property."""
            self.heap.append(val)
            self._sift_up(len(self.heap) - 1)

        def pop(self) -> int:
            """Removes and returns the minimum element from the heap."""
            if not self.heap:
                raise IndexError("Heap is empty")
            
            if len(self.heap) == 1:
                return self.heap.pop()
            
            root = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._sift_down(0)
            
            return root

    def _sift_up(self, i: int):
        """Moves a newly added element up to its correct position."""
        parent = (i - 1) // 2
        # While we aren't at the root and the parent is greater than the current node
        while i > 0 and self.heap[parent] > self.heap[i]:
            # Swap them
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            # Move up to the parent's index
            i = parent
            parent = (i - 1) // 2

    def _sift_down(self, i: int):
        """Moves a misplaced root element down to its correct position."""
        n = len(self.heap)
        
        while (2 * i + 1) < n:  # While there is at least a left child
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            
            # Check if left child is smaller than current smallest
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
                
            # Check if right child is smaller than current smallest
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
                
            # If the current node is already smaller than both children, we are done
            if smallest == i:
                break
                
            # Otherwise, swap and continue sifting down
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

        
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        while(len(self.minHeap) > k):
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]