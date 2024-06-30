import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.citta=DAO.getCitta()
        self.grafo = nx.DiGraph()
        self._idMap = {}
        self._idMapNome = {}

    def creaGrafo(self, citta, anno):
        self.nodi = DAO.getNodi(citta,anno)
        self.grafo.add_nodes_from(self.nodi)
        for v in self.nodi:
            self._idMap[v. business_id] = v
        for v in self.nodi:
            self._idMapNome[v.business_name] = v
        self.addEdges()
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self):
        self.grafo.clear_edges()
        for nodo1 in self.grafo:
            for nodo2 in self.grafo:
                if nodo1 != nodo2 and self.grafo.has_edge(nodo1, nodo2) == False:
                    peso=nodo1.mediaRecensioni - nodo2.mediaRecensioni
                    if peso>0:
                        self.grafo.add_edge(nodo1, nodo2, weight=abs(peso))
                    if peso<0:
                       self.grafo.add_edge(nodo2, nodo1, weight=abs(peso))
    def migliore(self):
        dizio = {}
        for nodo in self.grafo.nodes:
            entranti=0
            uscenti=0
            for arcoUscente in self.grafo.out_edges(nodo):
                uscenti+=self.grafo[arcoUscente[0]][arcoUscente[1]]["weight"]
            for arcoEntrante in self.grafo.in_edges(nodo):
                entranti+=self.grafo[arcoEntrante[0]][arcoEntrante[1]]["weight"]
                dizio[nodo.business_id]=entranti-uscenti
        dizioOrder=list(sorted(dizio.items(), key=lambda item:item[1], reverse=True))
        return self._idMap[dizioOrder[0][0]]

    def getBestPath(self, miglioramento, nodoInizialeStringa):
        self._soluzione = []
        self._costoMigliore = 0
        nodoIniziale = self._idMapNome[nodoInizialeStringa]
        nodoFinale = self.migliore()
        parziale = [nodoIniziale]
        self._ricorsione(parziale, miglioramento, nodoFinale)
        return self._costoMigliore, self._soluzione

    def _ricorsione(self, parziale, miglioramento, nodoFinale):
        if  parziale[-1] == nodoFinale:
            if len(parziale) > self._costoMigliore:
                self._soluzione = copy.deepcopy(parziale)
                self._costoMigliore =len(parziale)

        for n in self.grafo.neighbors(parziale[-1]):
            if len(parziale)>1:
              if self.grafo[parziale[-1]][n]["weight"]>miglioramento+self.grafo[parziale[-2]][parziale[-1]]["weight"] and n not in parziale:
                  parziale.append(n)
                  self._ricorsione(parziale, miglioramento, nodoFinale)
                  parziale.pop()
            else:
                if n not in parziale:
                    parziale.append(n)
                    self._ricorsione(parziale, miglioramento, nodoFinale)
                    parziale.pop()


