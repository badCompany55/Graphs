"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def bft(self, starting_vertex):

        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)
        size = q.size()
        return_val = []

        while size > 0:
            current_node = q.dequeue()

            if current_node not in visited:
                visited.add(current_node)
                return_val.append(current_node)
                edges = self.vertices[current_node]

                for e in edges:
                    q.enqueue(e)
            size = q.size()

        print(return_val)

        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
    def dft(self, starting_vertex):

        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        size = stack.size()
        return_val = []
        while size > 0:
            current_node = stack.pop()

            if current_node not in visited:
                visited.add(current_node)
                return_val.append(current_node)
                edges = self.vertices[current_node]

                for e in edges:
                    stack.push(e)
            size = stack.size()
        print(return_val)

        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO
    def dft_recursive(self, starting_vertex, path=[]):
        path += [starting_vertex]
        edges = self.vertices[starting_vertex]

        for e in edges:
            if e not in path:
                visited = self.dft_recursive(e, path)


        return path


        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        pass  # TODO
    def bfs(self, starting_vertex, destination_vertex):

        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])
        size = q.size()

        while size > 0:
            current_node = q.dequeue()
            single_value = current_node[-1]

            if single_value not in visited:
                edges = self.vertices[single_value]

                for e in edges:
                    new_path = current_node[:]
                    new_path.append(e)
                    q.enqueue(new_path)
                    if e is destination_vertex:
                        print(new_path)
                        return new_path

                visited.add(single_value)
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
    def dfs(self, starting_vertex, destination_vertex):

        stack = Stack()
        visited = set()
        stack.push([starting_vertex])
        size = stack.size()

        while size > 0:
            current_node = stack.pop()
            single_value = current_node[-1]

            if  single_value not in visited:
                edges = self.vertices[single_value]

                for e in edges:
                    new_path = current_node[:]
                    new_path.append(e)
                    stack.push(new_path)
                    if e is destination_vertex:
                        print(new_path)
                        return new_path

                visited.add(single_value)
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    graph.bft(7)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(graph.dft_recursive(1))

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
