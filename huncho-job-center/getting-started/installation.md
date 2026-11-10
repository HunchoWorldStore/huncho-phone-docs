# Installation

> **Escrow:** don't rename the `hunchoworld_jobcenter` folder, and don't delete the `.fxap` file that comes with the download, or the resource won't start.

1. **Add the resource.** Download it from [keymaster.fivem.net](https://keymaster.fivem.net) (Granted Assets) and put `hunchoworld_jobcenter` in your resources folder. Don't have it yet? Get it on the [Huncho World Store](https://hunchoworldstore.github.io/).
2. **Start order.** Add `ensure hunchoworld_jobcenter` to `server.cfg` **after** your framework, inventory, banking, target, key and fuel scripts, so they're detected.
3. **Restart.** The database tables are created automatically. `hunchoworld_jobcenter.sql` is included if you'd rather run it yourself.
4. **Add the items** for fishing, prospecting and recycling. See [Adding the items](items.md).
5. **Check `config/integrations.lua`.** Everything is on `auto`. If you run two of something (for example ox_target and qb-target), pick one by name.
6. **Optional: Discord logs.** Paste a webhook into `config/server.lua`. See [Discord logs](../configuration/discord-logs.md).
7. **Walk every job once** and adjust anything that's off with `/jclocations`. See [Locations and coordinates](../configuration/locations.md).

## Using ReaperV4?

Uncomment the three ReaperV4 lines near the top of `fxmanifest.lua`.

## Running fully offline

Font Awesome and Google Fonts load from their CDNs. To run without them, download both into `html/` and update the two `<link>` tags in `html/index.html`.
