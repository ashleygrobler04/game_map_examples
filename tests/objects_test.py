"""Test the objects example."""

from objects import GameMap
from pytest import raises


class TileType:
    """The base class for all tile types."""

    name: str
    move_cost: int = 5  # The default movement cost.


class DirtTile(TileType):
    """Dirt tile type."""

    name = "dirt"


class SandTile(TileType):
    """A sand type. Takes a little more energy to walk on."""

    name = "sand"
    move_cost = 7


class WaterTile(TileType):
    """A water type. Very hard to swim through."""

    name = "water"
    move_cost = 15


def test_init() -> None:
    """Test initialisation."""
    dirt: DirtTile = DirtTile()
    sand: SandTile = SandTile()
    map: GameMap[TileType] = GameMap(20, 10, dirt)
    assert map.size_x == 20
    assert map.size_y == 10
    assert map.tiles[0][0] is dirt
    map = GameMap(20, 10, sand)
    assert map.size_x == 20
    assert map.size_y == 10
    assert map.tiles[0][0] is sand


def test_get_tile() -> None:
    """Test the `get_tile` method."""
    dirt: DirtTile = DirtTile()
    sand: SandTile = SandTile()
    map: GameMap[TileType] = GameMap(10, 10, dirt)
    assert map.get_tile(0, 0) is dirt
    map.tiles[1][1] = sand
    assert map.get_tile(0, 0) is dirt
    assert map.get_tile(1, 1) is sand
    with raises(IndexError):
        map.get_tile(map.size_x + 1, map.size_y + 1)
    with raises(IndexError):
        map.get_tile(-1, -2)


def test_set_tile() -> None:
    """Test the `set_tile` method."""
    dirt: DirtTile = DirtTile()
    sand: SandTile = SandTile()
    map: GameMap[TileType] = GameMap(10, 10, dirt)
    map.set_tile(1, 2, sand)
    assert map.get_tile(0, 0) is dirt
    assert map.get_tile(1, 2) is sand
    with raises(IndexError):
        map.set_tile(-1, -2, sand)
    with raises(IndexError):
        map.set_tile(map.size_x + 1, map.size_y + 1, sand)
