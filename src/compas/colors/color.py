from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import colorsys
from compas.data import Data


class Color(Data):
    """Class for working with colors.

    Parameters
    ----------
    red : float
        The red component in the range of 0-1.
    green : float
        The green component in the range of 0-1.
    blue : float
        The blue component in the range of 0-1.
    alpha : float, optional
        Transparency setting.
        If ``alpha = 0.0``, the color is fully transparent.
        If ``alpha = 1.0``, the color is fully opaque.

    Other Parameters
    ----------------
    **kwargs : dict, optional
        See :class:`Data` for more information.

    Attributes
    ----------
    rgb : tuple[float, float, float]
        RGB1 color tuple, with components in the range 0-1.
    rgba : tuple[float, float, float, float]
        RGB1 color tuple, with transparency, and components in the range 0-1.
    rgb255 : tuple[int, int, int]
        RGB255 color tuple, with components in the range 0-255.
    rgba255 : tuple[int, int, int, int]
        RGB255 color tuple, with transparency, and components in the range 0-255.
    hls : tuple[float, float, float]
        Hue, luminance, saturation values in the range 0-1.
    yuv : tuple[float, float, float]
        Luma and chroma components, with chroma defined by the blue and red projections.
    luma : float
        The brightness of a yuv signal.
    chroma : tuple[float, float]
        The color of a yuv signal.
    is_light : bool
        If True, the color is considered light.

    Examples
    --------
    >>> Color(1, 0, 0)
    Color(1.0, 0.0, 0.0, 1.0)
    >>> Color.red()
    Color(1.0, 0.0, 0.0, 1.0)
    >>> Color(1, 0, 0) == Color.red()
    True

    >>> Color.magenta()
    Color(1.0, 0.0, 1.0, 1.0)
    >>> Color.lime()
    Color(0.5, 1.0, 0.0, 1.0)
    >>> Color.navy()
    Color(0.0, 0.0, 0.5, 1.0)
    >>> Color.olive()
    Color(0.5, 0.5, 0.0, 1.0)

    >>> Color.lime().is_light
    True
    >>> Color.navy().is_light
    False

    """

    def __init__(self, red, green, blue, alpha=1.0, **kwargs):
        super(Color, self).__init__(**kwargs)
        self.r = red
        self.g = green
        self.b = blue
        self.a = alpha

    # --------------------------------------------------------------------------
    # data
    # --------------------------------------------------------------------------

    @property
    def data(self):
        return {'red': self.r, 'green': self.g, 'blue': self.b, 'alpha': self.a}

    @data.setter
    def data(self, data):
        self.r = data['red']
        self.g = data['green']
        self.b = data['blue']
        self.a = data['alpha']

    @classmethod
    def from_data(cls, data):
        return cls(data['red'], data['green'], data['blue'], data['alpha'])

    # --------------------------------------------------------------------------
    # properties
    # --------------------------------------------------------------------------

    @property
    def rgb(self):
        r = self.r
        g = self.g
        b = self.b
        return r, g, b

    @property
    def rgba(self):
        r = self.r
        g = self.g
        b = self.b
        a = self.a
        return r, g, b, a

    @property
    def rgb255(self):
        r = int(self.r * 255)
        g = int(self.g * 255)
        b = int(self.b * 255)
        return r, g, b

    @property
    def rgba255(self):
        r = int(self.r * 255)
        g = int(self.g * 255)
        b = int(self.b * 255)
        a = int(self.a * 255)
        return r, g, b, a

    @property
    def hls(self):
        return colorsys.rgb_to_hls(* self.rgb)

    @property
    def yuv(self):
        y = self.luma
        u, v = self.chroma
        return y, u, v

    @property
    def luma(self):
        return 0.299 * self.r + 0.587 * self.g + 0.114 * self.b

    @property
    def chroma(self):
        y = self.luma
        u = 0.492 * (self.b - y)
        v = 0.877 * (self.r - y)
        return u, v

    @property
    def is_light(self):
        L = 0.2126 * self.r + 0.7152 * self.g + 0.0722 * self.b
        return L > 0.179

    # --------------------------------------------------------------------------
    # customization
    # --------------------------------------------------------------------------

    def __repr__(self):
        return 'Color({}, {}, {}, {})'.format(self.r, self.g, self.b, self.a)

    def __len__(self):
        return 3

    def __iter__(self):
        return iter(self.rgb)

    def __eq__(self, other):
        return all(a == b for a, b in zip(self, other))

    # --------------------------------------------------------------------------
    # constructors
    # --------------------------------------------------------------------------

    @classmethod
    def from_hls(cls, h, l, s):  # noqa: E741
        """Construct a color from Hue, Luminance, and Saturation.

        Parameters
        ----------
        h : float
            Hue.
        l : float
            Luminance.
        s : float
            Saturation.

        Returns
        -------
        :class:`compas.colors.Color`

        See Also
        --------
        For more information, see https://en.wikipedia.org/wiki/HSL_and_HSV

        """
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return cls(r, g, b)

    @classmethod
    def from_hsv(cls, h, s, v):
        """Construct a color from Hue, Saturation, and Value.

        Parameters
        ----------
        h : float
            Hue.
        s : float
            Saturation.
        v : float
            Value.

        Returns
        -------
        :class:`compas.colors.Color`

        See Also
        --------
        For more information, see https://en.wikipedia.org/wiki/HSL_and_HSV

        """
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return cls(r, g, b)

    @classmethod
    def from_yiq(cls, y, i, q):
        """Construct a color from components in the YIQ color space.

        Parameters
        ----------
        y : float
            Luma.
        i : float
            Orange-blue chroma.
        q : float
            Purple-green chroma.

        Returns
        -------
        :class:`compas.colors.Color`

        See Also
        --------
        For more information see https://en.wikipedia.org/wiki/YIQ

        """
        r, g, b = colorsys.yiq_to_rgb(y, i, q)
        return cls(r, g, b)

    @classmethod
    def from_yuv(cls, y, u, v):
        """Construct a color from components in the YUV color space.

        Parameters
        ----------
        y : float
            Luma.
        u : float
            Blue projection chroma.
        v : float
            Red projection chroma.

        Returns
        -------
        :class:`compas.colors.Color`

        See Also
        --------
        For more information see https://en.wikipedia.org/wiki/YUV

        """
        r = y + 1.140 * v
        g = y - 0.395 * u - 0.581 * v
        b = y + 2.032 * u
        return cls(r, g, b)

    @classmethod
    def from_i(cls, i):
        """Construct a color from a single number in the range 0-1.

        Parameters
        ----------
        i : float
            Number in the range 0-1, representing the color.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        if i == 0.0:
            r, g, b = 0, 0, 255
        elif 0.0 < i < 0.25:
            r, g, b = 0, int(255 * (4 * i)), 255
        elif i == 0.25:
            r, g, b = 0, 255, 255
        elif 0.25 < i < 0.5:
            r, g, b = 0, 255, int(255 - 255 * 4 * (i - 0.25))
        elif i == 0.5:
            r, g, b = 0, 255, 0
        elif 0.5 < i < 0.75:
            r, g, b = int(0 + 255 * 4 * (i - 0.5)), 255, 0
        elif i == 0.75:
            r, g, b = 255, 255, 0
        elif 0.75 < i < 1.0:
            r, g, b,  = 255, int(255 - 255 * 4 * (i - 0.75)), 0
        elif i == 1.0:
            r, g, b = 255, 0, 0
        else:
            r, g, b = 0, 0, 0
        return cls(r / 255.0, g / 255.0, b / 255.0)

    # --------------------------------------------------------------------------
    # presets
    # --------------------------------------------------------------------------

    @classmethod
    def white(cls):
        """Construct the color white.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(1.0, 1.0, 1.0)

    @classmethod
    def black(cls):
        """Construct the color black.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.0, 0.0, 0.0)

    @classmethod
    def grey(cls):
        """Construct the color grey.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.5, 0.5, 0.5)

    @classmethod
    def red(cls):
        """Construct the color red.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(1.0, 0.0, 0.0)

    @classmethod
    def orange(cls):
        """Construct the color orange.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(1.0, 0.5, 0.0)

    @classmethod
    def yellow(cls):
        """Construct the color yellow.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(1.0, 1.0, 0.0)

    @classmethod
    def lime(cls):
        """Construct the color lime (or chartreuse green).

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.5, 1.0, 0.0)

    @classmethod
    def green(cls):
        """Construct the color green.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.0, 1.0, 0.0)

    @classmethod
    def mint(cls):
        """Construct the color mint (or spring green).

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.0, 1.0, 0.5)

    @classmethod
    def cyan(cls):
        """Construct the color cyan.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.0, 1.0, 1.0)

    @classmethod
    def azure(cls):
        """Construct the color azure.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.0, 0.5, 1.0)

    @classmethod
    def blue(cls):
        """Construct the color blue.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.0, 0.0, 1.0)

    @classmethod
    def violet(cls):
        """Construct the color violet.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.5, 0.0, 1.0)

    @classmethod
    def magenta(cls):
        """Construct the color magenta.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(1.0, 0.0, 1.0)

    @classmethod
    def pink(cls):
        """Construct the color pink.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(1.0, 0.0, 0.5)

    # --------------------------------------------------------------------------
    # other presets
    # --------------------------------------------------------------------------

    @classmethod
    def maroon(cls):
        """Construct the color maroon.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.5, 0.0, 0.0)

    @classmethod
    def brown(cls):
        """Construct the color brown.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.5, 0.25, 0.0)

    @classmethod
    def olive(cls):
        """Construct the color olive.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.5, 0.5, 0.0)

    @classmethod
    def teal(cls):
        """Construct the color teal.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.0, 0.5, 0.5)

    @classmethod
    def navy(cls):
        """Construct the color navy.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.0, 0.0, 0.5)

    @classmethod
    def purple(cls):
        """Construct the color purple.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.5, 0.0, 0.5)

    @classmethod
    def silver(cls):
        """Construct the color silver.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        return cls(0.75, 0.75, 0.75)

    # ochre
    # beige
    # bordeaux
    # hotpink
    # steel
    # midnight
    # salmon

    # --------------------------------------------------------------------------
    # methods
    # --------------------------------------------------------------------------

    # desaturate

    def lighten(self, factor=10):
        """Lighten the color.

        Parameters
        ----------
        factor : float, optional
            Percentage of lightness increase.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the percentage of lightness increase is not in the range 0-100.

        """
        if factor > 100 or factor < 0:
            raise ValueError('Percentage of increased lightness should be in the range 0-100.')

        factor = 1.0 + factor / 100

        h, l, s = self.hls
        r, g, b = colorsys.hls_to_rgb(h, min(1.0, l * factor), s)
        self.r = r
        self.g = g
        self.b = b

    def lightened(self, factor=10):
        """Return a lightened copy of the color.

        Parameters
        ----------
        factor : float, optional
            Percentage of lightness increase.

        Returns
        -------
        :class:`compas.colors.Color`

        Raises
        ------
        ValueError
            If the percentage of lightness increase is not in the range 0-100.

        """
        color = self.copy()
        color.lighten(factor=factor)
        return color

    def darken(self, factor=10):
        """Darken the color.

        Parameters
        ----------
        factor : float, optional
            Percentage of lightness reduction.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the percentage of lightness reduction is not in the range 0-100.

        """
        if factor > 100 or factor < 0:
            raise ValueError('Percentage of reduced lightness should be in the range 0-100.')

        factor = 1.0 - factor / 100

        h, l, s = self.hls
        r, g, b = colorsys.hls_to_rgb(h, max(0.0, l * factor), s)
        self.r = r
        self.g = g
        self.b = b

    def darkened(self, factor=10):
        """Return a darkened copy of the color.

        Parameters
        ----------
        factor : float, optional
            Percentage of lightness reduction.

        Returns
        -------
        :class:`compas.colors.Color`

        Raises
        ------
        ValueError
            If the percentage of lightness reduction is not in the range 0-100.

        """
        color = self.copy()
        color.darken(factor=factor)
        return color

    def invert(self):
        """Invert the current color wrt to the RGB color circle.

        Returns
        -------
        None

        """
        self.r = 1.0 - self.r
        self.g = 1.0 - self.g
        self.b = 1.0 - self.b

    def inverted(self):
        """Return an inverted copy of the color.

        Returns
        -------
        :class:`compas.colors.Color`

        """
        color = self.copy()
        color.invert()
        return color

    def desaturate(self, factor=10):
        """Desaturate the color by a given percentage.

        Parameters
        ----------
        factor : float, optional
            Percentage of lightness reduction.

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the percentage of desaturation is not in the range 0-100.

        """
        if factor > 100 or factor < 0:
            raise ValueError('Percentage of desaturation should be in the range 0-100.')

        factor = 1.0 - factor / 100

        h, l, s = self.hls
        r, g, b = colorsys.hls_to_rgb(h, l, max(0.0, s * factor))
        self.r = r
        self.g = g
        self.b = b

    def desaturated(self, factor=10):
        """Return a desaturated copy of the color.

        Parameters
        ----------
        factor : float, optional
            Percentage of lightness reduction.

        Returns
        -------
        :class:`compas.colors.Color`

        Raises
        ------
        ValueError
            If the percentage of desaturation is not in the range 0-100.

        """
        color = self.copy()
        color.desaturate(factor=factor)
        return color
