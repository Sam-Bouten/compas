from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from uuid import uuid4
from .artist import BaseArtist


__all__ = ['BaseObject']


_ITEM_OBJECT = {}


class BaseObject(object):
    """Base class for all scene objects.

    Parameters
    ----------
    item : :class:`compas.base.Base`
        A COMPAS object.
    scene : :class:`compas.scene.BaseScene`, optional
        A scene object.
    name : str, optional
        The name of the object.
    visible : bool, optional
        Toggle for the visibility of the object.

    Attributes
    ----------
    item : :class:`compas.base.Base`
        A COMPAS object.
    scene : :class:`compas.scene.BaseScene`
        A scene object.
    artist : :class:`compas.scene.BaseArtist`
        The artist matching the type of ``item``.
    uuid : str
        The universaly unique identifier of the object.
    name : str
        The name of the object.
        This is an alias for the name of ``item``.
    visible : bool
        Toggle for the visibility of the object in the scene.

    """

    def __init__(self, item, scene=None, name=None, visible=True):
        super(BaseObject, self).__init__()
        self._item = None
        self._uuid = None
        self._scene = None
        self._artist = None
        self.scene = scene
        self.item = item
        self.name = name
        self.visible = visible

    # ==========================================================================
    # Properties
    # ==========================================================================

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, scene):
        self._scene = scene

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def artist(self):
        if not self._artist:
            self._artist = BaseArtist.build(self.item)
        return self._artist

    @property
    def uuid(self):
        if not self._uuid:
            self._uuid = str(uuid4())
        return self._uuid

    @property
    def name(self):
        return self.item.name

    @name.setter
    def name(self, name):
        self.item.name = name

    # ==========================================================================
    # Methods
    # ==========================================================================

    @staticmethod
    def register(item_type, object_type):
        _ITEM_OBJECT[item_type] = object_type

    @staticmethod
    def registered_object_types():
        return [_ITEM_OBJECT[item_type] for item_type in _ITEM_OBJECT]

    @staticmethod
    def build(item, **kwargs):
        object_type = _ITEM_OBJECT[type(item)]
        return object_type(item, **kwargs)

    def clear(self):
        """Clear all previously created objects."""
        raise NotImplementedError

    def draw(self):
        """Draw the object representing the item."""
        raise NotImplementedError

    def select(self):
        """Select the object representing the item."""
        raise NotImplementedError

    def modify(self):
        """Modify the item represented by the object."""
        raise NotImplementedError

    def move(self):
        """Move the item represented by the object."""
        raise NotImplementedError
