class Graph:
    def __init__(self):
        
        self.vertices = {}
    
    def add_vertex(self, value):
       
        if value not in self.vertices:
            self.vertices[value] = []
    
    def add_edge(self, vertex1, vertex2, weight=None):
       
        if vertex1 in self.vertices and vertex2 in self.vertices:
            if vertex1 == vertex2:
                self.vertices[vertex1].append((vertex2, weight))
            else:
                self.vertices[vertex1].append((vertex2, weight))
                self.vertices[vertex2].append((vertex1, weight))
    
    def get_vertices(self):
      
        return list(self.vertices.keys())
    
    def get_neighbors(self, vertex):
       
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return []
    
    def size(self):
       
        return len(self.vertices)