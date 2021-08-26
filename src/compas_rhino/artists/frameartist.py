from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import compas_rhino
from compas_rhino.artists._primitiveartist import PrimitiveArtist


__all__ = ['FrameArtist']


class FrameArtist(PrimitiveArtist):
    """Artist for drawing frames.

    Parameters
    ----------
    frame: :class:`compas.geometry.Frame`
        A COMPAS frame.
    layer: str, optional
        The layer containing the Rhino objects.
    scale: float, optional
        Scale factor that controls the length of the axes.
        Default is ``1.0``.

    Attributes
    ----------
    scale : float
        Scale factor that controls the length of the axes.
        Default is ``1.0``.
    color_origin : tuple of 3 int between 0 abd 255
        Default is ``(0, 0, 0)``.
    color_xaxis : tuple of 3 int between 0 abd 255
        Default is ``(255, 0, 0)``.
    color_yaxis : tuple of 3 int between 0 abd 255
        Default is ``(0, 255, 0)``.
    color_zaxis : tuple of 3 int between 0 abd 255
        Default is ``(0, 0, 255)``.

    """

    def __init__(self, frame, layer=None, scale=1.0):
        super(FrameArtist, self).__init__(frame, layer=layer)
        self.scale = scale or 1.0
        self.color_origin = (0, 0, 0)
        self.color_xaxis = (255, 0, 0)
        self.color_yaxis = (0, 255, 0)
        self.color_zaxis = (0, 0, 255)

    def draw(self):
        """Draw the frame.

        Returns
        -------
        guids: list
            The GUIDs of the created Rhino objects.
        """
        points = []
        lines = []
        origin = list(self.primitive.point)
        X = list(self.primitive.point + self.primitive.xaxis.scaled(self.scale))
        Y = list(self.primitive.point + self.primitive.yaxis.scaled(self.scale))
        Z = list(self.primitive.point + self.primitive.zaxis.scaled(self.scale))
        points = [{'pos': origin, 'color': self.color_origin}]
        lines = [
            {'start': origin, 'end': X, 'color': self.color_xaxis, 'arrow': 'end'},
            {'start': origin, 'end': Y, 'color': self.color_yaxis, 'arrow': 'end'},
            {'start': origin, 'end': Z, 'color': self.color_zaxis, 'arrow': 'end'}]
        guids = compas_rhino.draw_points(points, layer=self.layer, clear=False, redraw=False)
        guids += compas_rhino.draw_lines(lines, layer=self.layer, clear=False, redraw=False)
        return guids
