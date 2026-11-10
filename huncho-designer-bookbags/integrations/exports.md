# Developer exports

Server-side, for police and search scripts.

## GetCarriedBags

```lua
local bags = exports.hunchoworld_bookbags:GetCarriedBags(src)
```

Returns every bag the player carries, worn or not, with what is inside:

```lua
{
    { bagId = '...', stash = 'hwbag_...', item = 'hwbag_vespucci_01', label = 'Midnight Meridian Bookbag',
      worn = true, items = { { name = 'water', label = 'Water', count = 2, slot = 1, meta = {} } } },
}
```

Returns `nil` when the inventory can't read bag contents (ps-inventory, lj-inventory, qb-inventory before 2.0, or custom without `GetStashItems`).

## RemoveFromBag

```lua
local removed = exports.hunchoworld_bookbags:RemoveFromBag(src, bagId, 'water', 2, slot)
```

Takes items out of one of the player's bags. Returns `true` when they were removed.
