# event_ordering_vector_clock.py
# ----------------------------------------------
# Mini Project: Event Ordering in Distributed Social Media Platforms
# SDG 9 - Industry, Innovation, and Infrastructure
# ----------------------------------------------

from collections import defaultdict

class VectorClock:
    """A simple implementation of a vector clock for distributed systems."""
    def __init__(self, node_name):
        self.node = node_name
        self.clock = defaultdict(int)

    def tick(self):
        """Increment this node's clock when a local event occurs."""
        self.clock[self.node] += 1

    def update(self, received_clock):
        """Merge another node's clock to maintain event ordering."""
        for node, time in received_clock.items():
            self.clock[node] = max(self.clock[node], time)

    def send_message(self):
        """Return a copy of this node's current clock (simulating a message)."""
        return dict(self.clock)

    def __repr__(self):
        """Readable string representation of the vector clock."""
        return f"{self.node}: {dict(self.clock)}"


# --- Simulation of event ordering in a social media-like system ---

# Initialize three nodes (A, B, C)
A = VectorClock('A')  # e.g., User A posts
B = VectorClock('B')  # e.g., User B likes
C = VectorClock('C')  # e.g., User C comments

# Step 1: Local events occur independently
A.tick()  # A posts something
print("A after post:", A)

B.tick()  # B likes something
print("B after like:", B)

C.tick()  # C comments
print("C after comment:", C)

print("\n--- Message passing (synchronization) begins ---\n")

# Step 2: A sends message to B
B.update(A.send_message())
print("B after receiving from A:", B)

# Step 3: B sends message to C
C.update(B.send_message())
print("C after receiving from B:", C)

# Step 4: C sends message to A
A.update(C.send_message())
print("A after receiving from C:", A)

print("\n--- Final synchronized clocks ---\n")
print(A)
print(B)
print(C)
