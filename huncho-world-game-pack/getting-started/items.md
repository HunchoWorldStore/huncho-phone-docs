# Items

Each game has one item that sets up a table. The item files and images are in the pack's `install/` folder.

| Item | Label | Game |
| --- | --- | --- |
| `beerpong_kit` | Beer Pong Kit | [Beer Pong](../games/beer-pong.md) |
| `card_table` | Card Table | [Card Hub](../games/card-hub.md) |
| `ceelo_dice` | Dice | [Cee-lo](../games/cee-lo.md) |
| `domino_table` | Domino Table | [Dominoes](../games/dominoes.md) |
| `ohbihplease_deck` | Oh Bih Please Deck | [Oh Bih Please](../games/oh-bih-please.md) |
| `bihroulette_wheel` | Oh Bih Roulette Wheel | [Oh Bih Roulette](../games/oh-bih-roulette.md) |
| `slumlords_board` | Slumlords Board Game | [Slumlords](../games/slumlords.md) |
| `tumbling_towers` | Tumbling Towers Set | [Tumbling Towers](../games/tumbling-towers.md) |

## Add them to your inventory

{% tabs %}
{% tab title="ox_inventory" %}
Paste the entries from `install/items/ox_inventory.lua` into `ox_inventory/data/items.lua`, inside the `return { ... }` table. This file is also the one to use on Qbox and ox\_core, and on ESX or QBCore servers running ox\_inventory.

Copy everything in `install/images/` to `ox_inventory/web/images/`.

{% hint style="warning" %}
Keep `consume = 0` on every item. The games take the item when a table goes down and give it back when it's packed up.
{% endhint %}

Example entry:

```lua
['card_table'] = {
    label = 'Card Table',
    weight = 5000,
    stack = false,
    close = true,
    consume = 0,
    description = 'Fold-out table for a card game.',
    server = { export = 'hunchoworld_gamepack.useCardTable' },
},
```
{% endtab %}

{% tab title="qb-core" %}
Paste the entries from `install/items/qb-core.lua` into `qb-core/shared/items.lua`. The file has both the new format and the older `['bracket']` format.

This covers qb-inventory, ps-inventory, lj-inventory, and inventories that read qb-core's item list (core\_inventory, origen\_inventory, most codem and tgiann setups on QBCore).

Copy everything in `install/images/100x100/` (or `install/images/`) to your inventory's image folder, for example `qb-inventory/html/images/`.
{% endtab %}

{% tab title="ESX" %}
Run `install/items/esx.sql` once on your database. This is for the default ESX inventory and inventories that read ESX's items table (core\_inventory, origen\_inventory, qs-inventory or codem-inventory on ESX).

Copy everything in `install/images/` to your inventory's image folder.
{% endtab %}

{% tab title="Other" %}
| Inventory | File |
| --- | --- |
| qs-inventory | `install/items/qs-inventory.lua` |
| codem-inventory | `install/items/codem-inventory.lua` |
| tgiann-inventory | `install/items/tgiann-inventory.lua` |
| wasabi\_inventory | `install/items/wasabi_inventory.txt` |

Each file says where to paste it. Copy the images from `install/images/` to that inventory's image folder.
{% endtab %}
{% endtabs %}

## Item, command or both

Every game can be started with its item, its command, or both. You choose per game, in the [admin panel](../admin-panel.md) or in that game's config. See [Commands](../reference/commands.md) for each game's command and setting.

{% hint style="info" %}
Selling the sets in a shop? Add the item names above to your shop script like any other item.
{% endhint %}
