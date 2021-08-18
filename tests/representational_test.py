"""Test the representational system."""
from pytest import raises
from representational import GameMap

tile_types: list[str] = ["grass", "dirt", "sand"]


def test_init() -> None:
    """Test game map initialisation."""
    map: GameMap[str] = GameMap(20, 10, tile_types)
    assert map.size_x == 20
    assert map.size_y == 10
    assert map.get_tile(0, 0) == tile_types[0]
    map = GameMap(20, 10, tile_types, default_type_index=2)
    assert map.size_x == 20
    assert map.size_y == 10
    assert map.tiles[0][0] == 2


def test_get_tile() -> None:
    """Test the `get_tile` method."""
    map: GameMap[str] = GameMap(10, 10, tile_types)
    assert map.get_tile(0, 0) == tile_types[0]
    map.tiles[1][1] = 2
    assert map.get_tile(0, 0) == tile_types[0]
    assert map.get_tile(1, 1) == tile_types[2]
    with raises(IndexError):
        map.get_tile(map.size_x + 1, map.size_y + 1)
    with raises(IndexError):
        map.get_tile(-1, -2)


def test_set_tile() -> None:
    """Test the `set_tile` method."""
    map: GameMap[str] = GameMap(10, 10, tile_types)
    map.set_tile(1, 2, tile_types[1])
    assert map.get_tile(0, 0) == tile_types[0]
    assert map.get_tile(1, 2) == tile_types[1]
    with raises(IndexError):
        map.set_tile(-1, -2, tile_types[2])
    with raises(IndexError):
        map.set_tile(map.size_x + 1, map.size_y + 1, tile_types[2])
