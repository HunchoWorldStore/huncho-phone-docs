# Permissions

Add these to `server.cfg` as needed.

```cfg
# Admin panel (/gamepack). ox_lib adds this for group.admin automatically.
add_ace group.admin command.gamepack allow

# Cee-lo: close a table and refund
add_ace group.admin command.ceeloclose allow

# Beer Pong
add_ace group.admin hunchoworld_beerpong.admin allow   # pack up anyone's table
add_ace group.vip   hunchoworld_beerpong.place allow   # only if Config.Setup.commandAce = true
add_ace group.vip   hunchoworld_beerpong.bots  allow   # only if Config.Bots.ace = true

# Slumlords: place / remove tables anywhere
add_ace group.admin sage_slumlords.admin allow
```

| Game | Who counts as admin |
| --- | --- |
| Admin panel | `Config.Ace` in `games/admin/config.lua` |
| Card Hub | `Config.Admin.ace` plus `Config.Admin.groups` in `games/cardhub/config.lua` |
| Oh Bih Please / Oh Bih Roulette | `Config.Admin.ace` in each game's `config.lua` |
| Slumlords | The `sage_slumlords.admin` ace or `Config.Admin.groups` |
| Dominoes | `Config.TableItem.commandAce = true` limits `/dominotable` to the `command.dominotable` ace |
