# Troubleshooting

<details>

<summary>Using the item does nothing</summary>

* Make sure the item is added with the file for your inventory from `install/items/` (see [Items](../getting-started/items.md)).
* The resource folder must be named `hunchoworld_gamepack`. The item exports use that name.
* On ox\_inventory, keep `consume = 0`.
* Check the game is set to **Item** or **Both** in the [admin panel](../admin-panel.md), and that the game is **On**.
* Look at the start-up line the game printed in the server console. If the inventory shows `none`, set `Config.Inventory` by hand in that game's config.

</details>

<details>

<summary>"*Game* is closed right now"</summary>

That game is switched off in the [admin panel](../admin-panel.md). Open `/gamepack`, go to **Games**, pick it and set it to **On**.

</details>

<details>

<summary>I changed item / command / both and nothing changed</summary>

How a game starts is set when the pack starts. Restart it with `ensure hunchoworld_gamepack`. The admin panel shows a yellow notice until you do.

</details>

<details>

<summary>Wrong framework or inventory detected</summary>

Set `Config.Framework` / `Config.Inventory` in that game's config instead of `'auto'`.

</details>

<details>

<summary>Money games are off</summary>

* Each game needs a framework (Qbox, QBCore or ESX) for cash games.
* On standalone servers, buy-ins use a money item in ox\_inventory, tgiann-inventory or wasabi\_inventory.
* Bots are kept off money tables by default. That's on purpose: see each game's `Config.Bots`.

</details>

<details>

<summary>Dominoes shows an old GTA table and flat tiles</summary>

The streamed models didn't load. Make sure the pack's `stream/` folder is intact. The F8 console says `prop pack found` when they load.

</details>

<details>

<summary>Players float above or sink into chairs, or chairs face the wrong way</summary>

| Game | Setting |
| --- | --- |
| Card Hub | `Config.Seating.chairTurn`, `seatHeight`, `sitGap` |
| Dominoes | `chairGap` / `chairHeadingOffset` per style in `config/advanced.lua` |
| Slumlords | `chairTurn`, `seatHeight`, `seatGap` per style in `config/advanced.lua` |
| Tumbling Towers | `Config.ChairHeadingOffset`, `Config.Anims.sceneHeadingOffset`, `/ttsit` then `Config.SitBack` |

</details>

<details>

<summary>Beer Pong cups float or sink into the table</summary>

Set `Config.Debug = true` and place a table. F8 shows how the surface was measured. Nudge it with `Config.Geometry.cupLift`.

</details>

<details>

<summary>No update notice / I want to turn it off</summary>

The notice only shows when a newer version is out. Set `Config.UpdateCheck.debug = true` in `games/admin/config.lua` to also see "up to date". Turn it off with `Config.UpdateCheck.enabled = false`.

</details>

## Still stuck?

Open a ticket in our [Discord](https://discord.gg/hP8VTtwgs5) with:

* your framework, inventory and target
* the start-up lines each game printed in the server console
* any red errors from F8 or the server console
