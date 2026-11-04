# Commands

## Starting a table

Each game can start with its item, its command, or both. Set it in the [admin panel](../admin-panel.md) or with the setting below. The default is **both**.

| Game | Command | Item | Setting |
| --- | --- | --- | --- |
| Beer Pong | `/beerpong` | `beerpong_kit` | `Config.Setup.method` |
| Card Hub | `/placetable` (or walk up to any card table) | `card_table` | `Config.Placement.method` |
| Cee-lo | `/ceelo` | `ceelo_dice` | `Config.Start.method` |
| Dominoes | `/dominotable` | `domino_table` | `Config.TableItem.method` |
| Oh Bih Please | `/ohbihplease` | `ohbihplease_deck` | `Config.Placement.method` |
| Oh Bih Roulette | `/bihroulette` | `bihroulette_wheel` | `Config.Placement.method` |
| Slumlords | `/slumlordstable` | `slumlords_board` | `Config.TableItem.method` |
| Tumbling Towers | `/tumblingtowers` | `tumbling_towers` | `Config.Item.method` |

## Player commands

| Command | Game | Does |
| --- | --- | --- |
| `/beerpongleave` | Beer Pong | Leave the game |
| `/ceelorules` | Cee-lo | Rules for every game |

## Admin commands

| Command | Game | Does |
| --- | --- | --- |
| `/gamepack` | All | Open the [admin panel](../admin-panel.md) |
| `/cardtable [model]` | Card Hub | Place any prop as a card table |
| `/removecardtable` | Card Hub | Remove the nearest placed table, refunding everyone |
| `/ceeloclose` | Cee-lo | Close the nearest table and refund every bet |
| `/removeobptable` | Oh Bih Please | Remove the nearest player-placed table |
| `/removeobrtable` | Oh Bih Roulette | Remove the nearest player-placed table |
| `/slumlordsadmin` | Slumlords | Place a table anywhere, no item, no limit |
| `/slumlordsremove` | Slumlords | Remove the nearest table, refunding every buy-in |

Command names can be changed in each game's config.
