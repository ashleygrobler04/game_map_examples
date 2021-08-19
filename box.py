"""An example of building maps with boxes.

Although this example uses the enum example for its mapping, you could use any of my
methods, or invent your own.
"""
from typing import List, Tuple

from enums import GameMap, TileType


class Box:
    """A class to represent a rectangle of tiles.

    The difference between *tiles* and *boxes* is that tiles are a single square on the
    map. A box represents a collection.

    For example: A box might say that everything from (0, 0) to (10, 5) is water, and
    that would translate into tiles at (0, 0), (1, 0), (2, 0),... (8, 5), (9, 5),
    (10, 5).
    """

    def __init__(
        self,
        start_x: int,
        start_y: int,
        width: int,
        height: int,
        tile_type: TileType,
    ) -> None:
        """Create a box.

        When setting the end coordinates, we will subtract 1 from the width and height.

        This is because a width or height of 1 should result in the relevant coordinate
        remaining unchanged.

        This is to say, if you have a box which runs from (0, 0) to (10, 0), its height
        is still 1, because it is still taking up a square in that direction.
        """
        assert start_x >= 0, "Coordinates cannot be less than 0."
        assert start_y >= 0, "Coordinates cannot be less than 0."
        assert width > 0, "Width must not be less than 1."
        assert height > 0, "Height must not be less than 1."
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = start_x + (width - 1)
        self.end_y = start_y + (height - 1)
        self.width = width
        self.height = height
        self.tile_type = tile_type
        self.corner_sw = (start_x, start_y)
        self.corner_se = (self.end_x, start_y)
        self.corner_ne = (self.end_x, self.end_y)
        self.corner_nw = (start_x, self.end_y)

    start_x: int
    start_y: int
    end_x: int
    end_y: int
    width: int  # Think left to right, or west to east.
    height: int  # Think back to front, or south to north.
    tile_type: TileType
    corner_sw: Tuple[int, int]
    corner_se: Tuple[int, int]
    corner_nw: Tuple[int, int]
    corner_ne: Tuple[int, int]


class BoxManager:
    """A class to hold a collection of boxes.

    You can use this class to create a `GameMap` instance by using the `to_game_map`
    method.
    """

    def __init__(self, boxes: List[Box]) -> None:
        """Create an instance."""
        self.boxes = boxes

    boxes: List[Box]

    def to_game_map(self, default_type: TileType) -> GameMap:
        """Create a game map from this object.

        The way we do this is to find the size of the eventual map. We find this number
        by iterating over all the boxes, and finding the highest `end_x` and `end_y`
        coordinates.

        Next, we create a map of that size, using `default_tile_type`. Then we go
        through the coordinates of each box and set the appropriate tiles.

        It is worth noting that there is almost certainly a better way to do this. I
        just don't know what it is.
        """
        size_x: int = 0
        size_y: int = 0
        box: Box
        # 1. Get the map size from the available boxes.
        for box in self.boxes:
            size_x = max(size_x, box.end_x)
            size_y = max(size_y, box.end_y)
        # 2. Create the game map to use.
        map: GameMap = GameMap(
            size_x + 1, size_y + 1, default_tile_type=default_type
        )
        # 3. Set all the tiles that are *different* from the default tile type.
        # Let's not waste time re-adding tiles that are already st to the right type.
        # This probably doesn't make much of a saving, but we might as well optimise for
        # the extra line of code.
        x: int
        y: int
        for box in self.boxes:
            if box.tile_type is not default_type:
                # We add 1 to the end of the ranges, since the `range` function
                # intentionally misses the end number.
                for x in range(box.start_x, box.end_x + 1):
                    for y in range(box.start_y, box.end_y + 1):
                        map.set_tile(x, y, box.tile_type)
        return map
