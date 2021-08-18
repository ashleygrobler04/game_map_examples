# Game Map Examples

The question comes up a lot about the different ways of representing game maps. While I am no expert in this field, I feel I am at a stage where I can demonstrate working prototype, without so much complexity that they baffle the user.

Please see below for an outline of the different types of game map storage that I know about.

## Enums

### Description

This example uses [enums]([URL](https://en.wikipedia.org/wiki/Enumerated_type)) for tile types.

### For

* Less code, easier to understand at a glance.
* Pretty obvious what tile types do what.

### Against

* Tile type specifics need to be stored away from the tile types themselves, thus breaking [single source of truth]([URL](https://en.wikipedia.org/wiki/Single_source_of_truth)).
* Not particularly flexible.
* Will end up with lots of if statements.
* Tile type implementation will likely need to be done in different places, and Python has no notion of a [switch statement]([URL](https://en.wikipedia.org/wiki/Switch_statement#:~:text=In%20computer%20programming%20languages%2C%20a,execution%20via%20search%20and%20map.)).
* Adding more tile types requires potentially more work.
* Not obvious at a glance what the effects of a particular tile type are.

## Representational

### Description

This method allows you to specify a [set]([URL](https://en.wikipedia.org/wiki/Set_(abstract_data_type)#:~:text=In%20computer%20science%2C%20a%20set,concept%20of%20a%20finite%20set.)) of tile types, then reference them with pure numbers.

For this example, I used a python list. The data type isn't necessarily important, so long as you can index it.

It has to be said, this is my least favourite method. Just because your possible tile types are `['sand', 'grass', 'water', 'lava']`, doesn't stop you from accidentally setting a tile to `12345678`. Because of the way Python deals with negative integers (-1 is the last element in a list), you might not even notice you were messing stuff up if you were setting the indices wrong.

Honestly, this isn't a style I'm familiar with. See [this post]([URL](https://forum.audiogames.net/post/660539/#p660539)) on audiogames.net for explanation.

### For

* It would be trivial to dump these maps to JSON.
* According to the post linked above: This data structure meshes well with using paint tools to draw maps to easily load into your game.

### Against

* Same problems as with enums.
* Impossible to do meaningful type checking.

## Objects

### Description

This is probably the most advanced method here. It uses [generics]([URL](https://mypy.readthedocs.io/en/stable/generics.html)), to set the type of your tiles.

If you create a base `TileType` class to work from, you can use that as your type argument.

### For

* Very flexible.
* You can save all the data associated with tile types on the type classes themselves.
* It is easy to see at a glance what each tile type does.
* Adding new tile types is as easy as subclassing the base `TileType` class.

### Against

* Would be moderately difficult to dump maps to JSON.
* Generics might be confusing.
* Involves a bit more code.
* Probably requires a bit more memory to hold instances. Of course you should be reusing instances, so there you go.
