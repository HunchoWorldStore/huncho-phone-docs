# Updating

## Update notice

When the pack starts, and every 6 hours after, it checks whether a newer version is out. If there is one, the server console shows the new version, what changed and where to download it:

```
================================================================
[hunchoworld_gamepack] Update available: 1.16.0 (you have 1.15.0)
    Released: 2026-11-20
    - ...
    Download: https://keymaster.fivem.net/asset-grants
================================================================
```

The settings are in `games/admin/config.lua`:

```lua
Config.UpdateCheck = {
    enabled    = true,
    everyHours = 6,       -- 0 = only when the pack starts
    debug      = false,   -- also print "up to date" and failed checks
}
```

## Installing an update

1. Download the new version from [keymaster.fivem.net](https://keymaster.fivem.net) (Granted Assets). Bought it on the [Huncho World FiveM Store](https://huncho-world-fivem-store.tebex.store/)? It shows up there under your Cfx account.
2. Back up the files you changed: configs, `locales/`, `config_deck.lua`, `shared/board.lua` and anything in `bridge/` or `editable/`.
3. Replace the `hunchoworld_gamepack` folder, then copy your changes back in. Check the [changelog](../changelog.md) for new config options first.
4. Restart the server.

{% hint style="success" %}
**What you set in the [admin panel](../admin-panel.md)** (on/off, start method, stake limits, permanent tables) is kept in the server's resource storage, not in the folder, so it survives updates.
{% endhint %}

{% hint style="warning" %}
**Player-placed tables** for Card Hub (`games/cardhub/data/tables.json`), Oh Bih Please and Oh Bih Roulette are saved inside the folder. Copy those files across if you want to keep them.
{% endhint %}
