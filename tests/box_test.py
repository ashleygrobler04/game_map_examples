"""Test the box example."""

from typing import List

from box import Box, BoxManager
from enums import GameMap, TileType
from pytest import raises


def test_box_init() -> None:
    """Test box initialisation."""
    box: Box = Box(1, 2, 3, 4, TileType.grass)
    assert box.start_x == 1
    assert box.start_y == 2
    assert box.width == 3
    assert box.height == 4
    assert box.end_x == 3  # box.start_x + (box.width - 1).
    assert box.end_y == 5  # box.start_y + (box.height - 1`).
    assert box.tile_type == TileType.grass
    assert box.corner_sw == (box.start_x, box.start_y)
    assert box.corner_se == (box.end_x, box.start_y)
    assert box.corner_ne == (box.end_x, box.end_y)
    assert box.corner_nw == (box.start_x, box.end_y)
    with raises(AssertionError):
        box = Box(-1, 0, 1, 1, TileType.dirt)
    with raises(AssertionError):
        box = Box(0, -1, 1, 1, TileType.dirt)
    with raises(AssertionError):
        box = Box(0, 0, -1, 1, TileType.dirt)
    with raises(AssertionError):
        box = Box(0, 0, 1, -1, TileType.dirt)


def test_box_collection_init() -> None:
    """Test BoxCollection initialisation."""
    west_field: Box = Box(0, 0, 10, 20, TileType.grass)
    path: Box = Box(*west_field.corner_se, 5, west_field.height, TileType.sand)
    east_field: Box = Box(
        *path.corner_se,
        west_field.width,
        west_field.height,
        west_field.tile_type
    )
    boxes: List[Box] = [west_field, path, east_field]
    box_manager: BoxManager = BoxManager(boxes)
    assert box_manager.boxes == [west_field, path, east_field]


def test_to_game_map() -> None:
    """Test that we can convert a box manager to a game map.

    We do that by creating 2 fields which have a split in between them. We can pretend
    the split is a path or something.
    """
    west_field: Box = Box(0, 0, 10, 20, TileType.grass)
    x, y = west_field.corner_se
    east_field: Box = Box(
        x + 5, y, west_field.width, west_field.height, west_field.tile_type
    )
    boxes: List[Box] = [west_field, east_field]
    box_manager: BoxManager = BoxManager(boxes)
    game_map: GameMap = box_manager.to_game_map(TileType.dirt)
    assert isinstance(game_map, GameMap)
    assert game_map.size_x == east_field.end_x + 1
    assert game_map.size_y == east_field.end_y + 1
    assert game_map.get_tile(*west_field.corner_sw) is west_field.tile_type
    assert game_map.get_tile(*west_field.corner_ne) is west_field.tile_type
    assert game_map.get_tile(*east_field.corner_sw) is east_field.tile_type
    assert game_map.get_tile(*east_field.corner_ne) is east_field.tile_type
    assert game_map.get_tile(x + 1, y) is TileType.dirt
    assert (
        game_map.get_tile(east_field.start_x - 1, east_field.end_y)
        is TileType.dirt
    )
