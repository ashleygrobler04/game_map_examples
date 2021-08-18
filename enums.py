"""An example of using enums to construct game maps."""

from enum import Enum, auto
from typing import List


class TileType(Enum):
    """The various tile types."""

    dirt = auto()
    grass = auto()
    water = auto()
    sand = auto()


class GameMap:
    """A game map.

    This map holds a list of tile types.
    """

    def __init__(
        self,
        size_x: int,
        size_y: int,
        default_tile_type: TileType = TileType.dirt,
    ) -> None:
        """Create a map."""
        self.tiles = []
        self.size_x = size_x
        self.size_y = size_y
        for _ in range(size_x):
            l: List[TileType] = []
            for _ in range(size_y):
                l.append(default_tile_type)
            self.tiles.append(l)

    size_x: int
    size_y: int
    tiles: List[List[TileType]]

    def get_tile(self, x: int, y: int) -> TileType:
        """Return the tile type at the given coordinates.

        This method will raise RangeError if the coordinates are out of range.
        """
        if x < 0 or y < 0 or x >= self.size_x or y >= self.size_y:
            raise IndexError(x, y)
        return self.tiles[x][y]

    def set_tile(self, x: int, y: int, tile_type: TileType) -> None:
        """Set the tile type at the given coordinates."""
        if x < 0 or y < 0 or x >= self.size_x or y >= self.size_y:
            raise IndexError(x, y)
        self.tiles[x][y] = tile_type
