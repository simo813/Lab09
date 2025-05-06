from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.DAO = DAO()


    def buildGraph(self, distanza):
        listaConnessioniFiltrate = self.DAO.getConnections(distanza)
        graph = nx.Graph()
        for connection in listaConnessioniFiltrate:
            graph.add_edge(connection[0], connection[1], weight=connection[2])
        return graph

