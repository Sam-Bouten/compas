from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_rhino.artists._shapeartist import ShapeArtist


class PolyhedronArtist(ShapeArtist):

    def draw(self):
        vertices = [list(vertex) for vertex in self.shape.vertices]
        faces = self.shape.faces
        return compas_rhino.draw_mesh(vertices,
                                      faces,
                                      layer=self.layer,
                                      name=self.shape.name,
                                      color=self.color,
                                      disjoint=True,
                                      clear=False,
                                      redraw=False)
