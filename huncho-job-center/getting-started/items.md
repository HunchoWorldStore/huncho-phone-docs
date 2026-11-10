# Adding the items

Fishing, prospecting and recycling hand out real items (fish, junk, finds and bonus materials). Add them to your inventory and copy every PNG in `install/images/` into its image folder.

| Inventory | Items | Images |
|---|---|---|
| **ox_inventory** | `install/ox_inventory_items.lua` into `ox_inventory/data/items.lua`, plus the newspaper from `install/ox_inventory_weapons.lua` into `ox_inventory/data/weapons.lua` | `ox_inventory/web/images/` |
| **QBCore inventories, qs-inventory** | `install/qb_items.lua` into `qb-core/shared/items.lua` (or `qs-inventory/shared/items.lua`) | Your inventory's image folder (qb-inventory: `html/images/`) |
| **ESX default inventory** | Run `install/esx_items.sql` on your database | none |
| **tgiann, wasabi, ak47 and others** | Add the same item names (see `install/qb_items.lua` for labels and weights) the way your inventory registers items | Your inventory's image folder |

## Item metadata

Each fish has a real weight and each find has an appraised value. That works on ox_inventory, qs-inventory, tgiann-inventory, wasabi_inventory, ak47_inventory and QBCore inventories. The default ESX inventory has no metadata, so the shops pay the average price.

## The newspaper

On ox_inventory the Paperboy's newspaper is a weapon item, so it's counted and protected like any item. On every other inventory it's handed over as a regular GTA throwable with one paper per house, so there's nothing to add.
