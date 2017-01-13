"""Wraps the networkx Graph object"""

import networkx as nx
import json


class Graph(nx.Graph):
    def canonical_form(self):
        raise NotImplementedError('this is for dw_graph only, not yet implemented')

    def toJSON(self):
        raise NotImplementedError('this is for dw_graph only, not yet implemented')

    def add_chimera_structure(self, m, n=None, t=None):
        """adds the edges from a Chimera-strucuted graph defined by (m, n, t)
        see documentation of get_chimera_adjacency from sapi"""
        if n is None:
            n = m
        if t is None:
            t = 4

        hoff = 2 * t
        voff = n * hoff
        mi = m * voff
        ni = n * hoff

        # cell edges
        adj = set((k0, k1)
                  for i in xrange(0, ni, hoff)
                  for j in xrange(i, mi, voff)
                  for k0 in xrange(j, j + t)
                  for k1 in xrange(j + t, j + 2 * t))
        # horizontal edges
        adj.update((k, k + hoff)
                   for i in xrange(t, 2 * t)
                   for j in xrange(i, ni - hoff, hoff)
                   for k in xrange(j, mi, voff))
        # vertical edges
        adj.update((k, k + voff)
                   for i in xrange(t)
                   for j in xrange(i, ni, hoff)
                   for k in xrange(j, mi - voff, voff))

        self.add_edges_from(adj)

if __name__ == '__main__':
    pass