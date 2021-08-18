"""Test the enum example."""

from enums import GameMap, TileType
from pytest import raises


def test_init() -> None:
    """Test game map initialisation."""
    map: GameMap = GameMap(20, 10)
    assert map.size_x == 20
    assert map.size_y == 10
    assert map.tiles[0][0] is TileType.dirt
    map = GameMap(20, 10, default_tile_type=TileType.grass)
    assert map.size_x == 20
    assert map.size_y == 10
    assert map.tiles[0][0] is TileType.grass


def test_get_tile() -> None:
    """Test the `get_tile` method."""
    map: GameMap = GameMap(10, 10)
    assert map.get_tile(0, 0) is TileType.dirt
    map.tiles[1][1] = TileType.grass
    assert map.get_tile(0, 0) is TileType.dirt
    assert map.get_tile(1, 1) is TileType.grass
    with raises(IndexError):
        map.get_tile(map.size_x + 1, map.size_y + 1)
    with raises(IndexError):
        map.get_tile(-1, -2)


def test_set_tile() -> None:
    """Test the `set_tile` method."""
    map: GameMap = GameMap(10, 10)
    map.set_tile(1, 2, TileType.sand)
    assert map.get_tile(0, 0) is TileType.dirt
    assert map.get_tile(1, 2) is TileType.sand
    with raises(IndexError):
        map.set_tile(-1, -2, TileType.grass)
    with raises(IndexError):
        map.set_tile(map.size_x + 1, map.size_y + 1, TileType.grass)
