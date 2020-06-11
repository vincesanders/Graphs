class Graph:

    def __init__(self):
        self.vertices = {}
        self.parents = []
        self.children = {}

    def add_vertex(self, parent_child):
        """
        Add a vertex to the graph.
        """
        # destructure tuple
        parent, child = parent_child
        if parent in self.vertices:
            self.vertices[parent].add(child)
        else:
            self.parents.append(parent) # parent node only added to parents once
            self.vertices[parent] = {child}
        if child not in self.children:
            self.children[child] = child

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v2 not in self.vertices:
            raise Exception(f'There is not a vertex with id {v2} in the graph.')
        elif v1 not in self.vertices:
            raise Exception(f'There is not a vertex with id {v1} in the graph.')
        else:
            self.vertices[v1].add(v2)

    def get_edges(self, vertex_id):
        """
        Get all edges of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
    
    def get_parents(self):
        """
        Get beginning ancestors.
        """
        return set(self.parents) - set(self.children)

    def get_dfs_paths(self, starting_vertex, destination_vertex, path=None):
        """
        Return a generator containing all the
        paths from the starting to destination
        vertex.
        """
        if path is None:
            path = [starting_vertex]
        if starting_vertex == destination_vertex:
            yield path
        if starting_vertex in self.vertices:
            for v in self.vertices[starting_vertex] - set(path):
                yield from self.get_dfs_paths(v, destination_vertex, path + [v])
    
    def dfs(self, starting_vertex, destination_vertex): # O(v * e)
        """
        Return a list containing the longest path from
        starting_vertex to destination_vertex in
        depth-first order using recursion.
        """
        generator = self.get_dfs_paths(starting_vertex, destination_vertex)
        first_path = True
        longest_path = None
        for path in generator:
            if first_path:
                first_path = False
                longest_path = path
            if (len(path) > len(longest_path)):
                longest_path = path
            elif (len(path) == len(longest_path)):
                if path[0] < longest_path[0]:
                    longest_path = path
        return longest_path

# O(2pve + n) - p = parent nodes, v = total vertices, e = total edges, n = length of ancestors array
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    # add ancestors to graph
    for a in array: # O(n)
        graph.add_vertex(a)
    parents = graph.get_parents()
    paths = []
    for parent in parents: # O(p)
        # find all the paths for each parent
        paths.append(graph.dfs(parent, starting_node))
    longest_path = None
    first_path = True
    # find the longest of the paths
    for path in paths: # O(p)
        if path is None:
            continue
        if first_path:
            first_path = False
            longest_path = path
        if (len(path) > len(longest_path)):
            longest_path = path
        elif (len(path) == len(longest_path)):
            if path[0] < longest_path[0]:
                longest_path = path
    # if length is one, the starting_node has no parent
    if len(longest_path) <= 1:
        return -1
    # return the first node of the longest path
    return longest_path[0]



array = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

graph = Graph()

for a in array:
    graph.add_vertex(a)

print(graph.get_parents())

print(earliest_ancestor(array, 6))

# Pierre's solution code
# def earliest_ancestor(ancestors, starting_node):
#     # Build the graph
#     graph = Graph()
#     for pair in ancestors:
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])
#         # Build edges in reverse
#         graph.add_edge(pair[1], pair[0])
#     # Do a BFS (storing the path)
#     q = Queue()
#     q.enqueue([starting_node])
#     max_path_len = 1
#     earliest_ancestor = -1
#     while q.size() > 0:
#         path = q.dequeue()
#         v = path[-1]
#         # If the path is longer or equal and the value is smaller, or if the path is longer)
#         if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
#             earliest_ancestor = v
#             max_path_len = len(path)
#         for neighbor in graph.vertices[v]:
#             path_copy = list(path)
#             path_copy.append(neighbor)
#             q.enqueue(path_copy)
#     return earliest_ancestor