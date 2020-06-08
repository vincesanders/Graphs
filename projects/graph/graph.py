"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            raise Exception(f"A vertex with vertex id: {vertex_id} already exists.")
        else:
            self.vertices[vertex_id] = set()

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

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        if starting_vertex not in self.vertices:
            raise Exception(f'There is not a vertex with id {starting_vertex} in the graph.')
        visited = {}
        vertices_to_visit = Queue() # TODO change to linked list
        vertices_string = ''
        current = starting_vertex
        while current != None:
            if current in visited:
                if vertices_to_visit.size is 0:
                    current = None
                    break
                current = vertices_to_visit.dequeue()
                continue
            visited[current] = self.vertices[current]
            vertices_string += f'{str(current)}, '
            visited[current] = True
            neighbors = self.get_neighbors(current) # get neighbors
            # if no neighbors
            if len(neighbors) is 0:
                # check vertices_to_visit
                if vertices_to_visit.size is 0:
                    current = None
                    break
                current = vertices_to_visit.dequeue()
            # if 1 or more neighbors
            else:
                for v in neighbors:
                    if v in visited:
                        continue
                    vertices_to_visit.enqueue(v)
                if vertices_to_visit.size is 0:
                    current = None
                    break
                current = vertices_to_visit.dequeue()
        print(vertices_string[:(len(vertices_string) - 2)]) # don't include the last ,_

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        if starting_vertex not in self.vertices:
            raise Exception(f'There is not a vertex with id {starting_vertex} in the graph.')
        visited = {}
        vertices_to_visit = Stack() # TODO change to linked list
        vertices_string = ''
        current = starting_vertex
        while current != None:
            if current in visited:
                if vertices_to_visit.size is 0:
                    current = None
                    break
                current = vertices_to_visit.pop()
                continue
            visited[current] = self.vertices[current]
            vertices_string += f'{str(current)}, '
            visited[current] = True
            neighbors = self.get_neighbors(current) # get neighbors
            # if no neighbors
            if len(neighbors) is 0:
                # check vertices_to_visit
                if vertices_to_visit.size is 0:
                    current = None
                    break
                current = vertices_to_visit.pop()
            # if 1 or more neighbors
            else:
                for v in neighbors:
                    if v in visited:
                        continue
                    vertices_to_visit.push(v)
                if vertices_to_visit.size is 0:
                    current = None
                    break
                current = vertices_to_visit.pop()
        print(vertices_string[:(len(vertices_string) - 2)]) # don't include the last ,_

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
