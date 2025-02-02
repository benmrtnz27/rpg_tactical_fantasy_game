"""
Defines Door class, a non-living entity that eventually could be opened by the living entities
"""

from lxml import etree

from src.game_entities.entity import Entity
from src.gui.position import Position


class Door(Entity):
    """
    A Door is an entity that could be opened by using pick-locking or keys.

    Keyword arguments:
    position -- the position of the door on screen
    sprite -- the relative path to the visual representation of the door
    pick_lock_initiated -- whether the door is currently being pick-locked or not

    Attributes:
    sprite_name -- the relative path to the visual representation of the door
    pick_lock_initiated -- whether the door is currently being pick-locked or not
    """

    def __init__(
        self, position: Position, sprite: str, pick_lock_initiated: bool
    ) -> None:
        super().__init__("Door", position, sprite)
        self.sprite_name: str = sprite
        self.pick_lock_initiated: bool = pick_lock_initiated

    def save(self, tree_name: str) -> etree.Element:
        """
        Save the current state of the door in XML format.

        Return the result of this generation.

        Keyword arguments:
        tree_name -- the name that should be given to the root element of the generated XML.
        """
        tree: etree.Element = super().save(tree_name)

        # Save sprite
        sprite: etree.SubElement = etree.SubElement(tree, "sprite")
        sprite.text = self.sprite_name

        # Save if pick lock has been initiated
        if self.pick_lock_initiated:
            etree.SubElement(tree, "pick_lock_initiated")

        return tree
