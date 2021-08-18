"""An example of using classes to represent tile types."""
from typing import Generic, List, TypeVar

T = TypeVar("T")


class GameMap(Generic[T]):
    """A game map which uses objects for tile types."""

    def __init__(self, size_x: int, size_y: int, default_tile_type: T) -> None:
        """Create an instance.

        Unlike the other examples, you must explicitly set the default tile type, as the
        code cannot infer a sensible default.
        """
        self.tiles = []
        self.size_x = size_x
        self.size_y = size_y
        for _ in range(size_x):
            l: List[T] = []
            for _ in range(size_y):
                l.append(default_tile_type)
            self.tiles.append(l)

    size_x: int
    size_y: int
    tiles: List[List[T]]

    def get_tile(self, x: int, y: int) -> T:
        """Return the tile type at the given coordinates.

        This method will raise RangeError if the coordinates are out of range.
        """
        if x < 0 or y < 0 or x >= self.size_x or y >= self.size_y:
            raise IndexError(x, y)
        return self.tiles[x][y]

    def set_tile(self, x: int, y: int, tile_type: T) -> None:
        """Get the tile type at the given coordinates."""
        if x < 0 or y < 0 or x >= self.size_x or y >= self.size_y:
            raise IndexError(x, y)
        self.tiles[x][y] = tile_type
