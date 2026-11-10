# Adding the items

Every design comes as a bookbag and a mini, so there are 176 items. The files are in `install/`, and the images in `html/images`.

## Items

Paste the file for your inventory from `install/`:

| Inventory | File | Paste into |
| --- | --- | --- |
| ox\_inventory | `ox_items.lua` | `ox_inventory/data/items.lua` |
| qb-inventory, ps-inventory, lj-inventory | `qb_items.lua` | `qb-core/shared/items.lua` |
| qs-inventory | `qs_items.lua` | `qs-inventory/shared/items.lua` (ESX, Qbox) or `qb-core/shared/items.lua` (QBCore) |
| wasabi\_inventory | `wasabi_items.lua` | `wasabi_inventory/data/items.lua` |
| tgiann-inventory | `tgiann_items.lua` | `tgiann-inventory/items/items.lua` |
| ak47\_inventory | `ak47_items.lua` | your ak47\_inventory item list |

## Images

Copy every PNG from `html/images` into your inventory's image folder:

| Inventory | Folder |
| --- | --- |
| ox\_inventory | `web/images` |
| qb, ps, lj | `html/images` |
| qs-inventory | its item image folder |
| wasabi\_inventory | `ui/images` |
| tgiann-inventory | `inventory_images/images` |
| ak47\_inventory | its item image folder |

{% hint style="info" %}
The item files and images always include every design, old and new. Paste the whole file again after an update.
{% endhint %}
