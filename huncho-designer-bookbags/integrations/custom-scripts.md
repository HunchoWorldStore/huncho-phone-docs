# Using your own scripts

Use this if your framework or inventory isn't detected.

1. In `config.lua`, set `Config.Framework = 'custom'`, `Config.Inventory = 'custom'`, or both.
2. Open `server/bridge/custom.lua` and fill in the functions for the part you set to custom.
3. Restart. The console prints `Framework: custom` or `Inventory: custom`.

`custom.lua` is never encrypted.

## Framework functions

| Function | Receives | Returns |
| --- | --- | --- |
| `GetPlayer` | `src` | anything when the character is loaded, otherwise `nil` |
| `GetCharId` | `src` | unique character id |
| `GetMoney` | `src, method` (`'cash'` or `'bank'`) | number |
| `RemoveMoney` | `src, method, amount, reason` | `true` when taken |
| `AddMoney` | `src, method, amount, reason` | nothing |
| `GetJob` | `src` | job name |
| `IsAdmin` | `src` | `true` for admins |
| `RegisterUsable` | `item, handler` | call `handler(src, slot, metadata)` when used |

## Inventory functions

| Function | Receives | Returns |
| --- | --- | --- |
| `AddItem` | `src, item, metadata` | `true` on success. Metadata must be saved on the item |
| `GetItems` | `src` | list of `{ name, slot, meta }` |
| `GetSlot` | `src, slot` | `{ name, slot, meta }` or `nil` |
| `SetMetadata` | `src, slot, metadata` | nothing |
| `OpenStash` | `src, id, label, slots, grams` | nothing |
| `RegisterUsable` | optional | same as the framework version |
| `GetStashItems` | optional: `id` | list of `{ name, slot, meta, count, label }` |
| `RemoveFromStash` | optional: `id, item, count, slot` | `true` on success |
| `BlockBagsInBags` | optional: set of bag item names | set up a hook in your inventory |

The optional functions add police searches and keep bags out of bags.

## Example

```lua
CustomInventory.AddItem = function(src, item, metadata)
    return exports['my-inventory']:AddItem(src, item, 1, metadata) == true
end

CustomInventory.OpenStash = function(src, id, label, slots, grams)
    exports['my-inventory']:OpenStash(src, id, { label = label, slots = slots, maxWeight = grams })
end
```
