"""An example of representational maps."""


from typing import Generic, List, TypeVar

T = TypeVar("T")


class GameMap(Generic[T]):
    """A representational tile map.

    This class is a game map which stores a reference to not only the type for each
    tile, but also the possible tile types.
    """

    def __init__(
        self,
        size_x: int,
        size_y: int,
        tile_types: list[T],
        default_type_index: int = 0,
    ) -> None:
        """Create an instance."""
        self.tile_types = tile_types
        self.size_x = size_x
        self.size_y = size_y
        self.tiles = []
        for _ in range(size_x):
            l: List[int] = []
            for _ in range(size_y):
                l.append(default_type_index)
            self.tiles.append(l)

    size_x: int
    size_y: int
    tile_types: list[T]
    tiles: List[List[int]]

    def get_tile(self, x: int, y: int) -> T:
        """Return the tile type at the given coordinates.

        This method will raise RangeError if the coordinates are out of range.
        """
        if x < 0 or y < 0 or x >= self.size_x or y >= self.size_y:
            raise IndexError(x, y)
        index: int = self.tiles[x][y]
        return self.tile_types[index]

    def set_tile(self, x: int, y: int, tile_type: T) -> None:
        """Set the type of the tile at the given coordinates."""
        if x < 0 or y < 0 or x >= self.size_x or y >= self.size_y:
            raise IndexError(x, y)
        index: int = self.tile_types.index(tile_type)
        self.tiles[x][y] = index
