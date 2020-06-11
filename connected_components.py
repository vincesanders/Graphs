islands = [
    [0, 1, 0, 1, 0], 
    [1, 1, 0, 1, 1], 
    [0, 0, 1, 0, 0], 
    [1, 0, 1, 0, 0], 
    [1, 1, 0, 0, 0]
]

'''
Conected Components
-------------------
Parts of the graph that are connected, but not connected to other parts of the graph

for each node:
    if node not visited:
        traverse from that node
        increment counter
'''

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def get_neighbors(row, col, matrix):
    neighbors = []
    # check north
    if row > 0 and matrix[row - 1][col] is 1:
        neighbors.append((row - 1, col))
    # check south
    if row < len(matrix) - 1 and matrix[row + 1][col] is 1:
        neighbors.append((row + 1, col))
    # check east
    if col < len(matrix[row]) - 1 and matrix[row][col + 1] is 1:
        neighbors.append((row, col + 1))
    # check west
    if col > 0 and matrix[row][col - 1] is 1:
        neighbors.append((row, col - 1))
    return neighbors

def dft(row, col, matrix, visited):
    s = Stack()
    s.push((row, col)) # tuple

    while s.size() > 0:
        row, col = s.pop() # destructured tuple
        if not visited[row][col]:
            visited[row][col] = True
            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)

def island_counter(matrix):
    island_count = 0
    # Create a visited matrix
    visited = []
    for i in range(len(matrix)): # create a matrix of False values that is same size as islands matrix
        visited.append([False] * len(matrix[i]))
    # walk through each cell in matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
        #If it's not visited
            if not visited[row][col]:
            # If it's not a '1'
                if matrix[row][col] is 1:
                # Do DFT and mark them as visited
                    dft(row, col, matrix, visited)
                # increment counter by 1
                    island_count += 1
    # return counter
    return island_count

print(island_counter(islands))