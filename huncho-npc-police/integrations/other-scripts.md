# Other scripts (no code)

Running a script that isn't supported? Connect it in `config.lua` (`Config.Integrations`) by naming what it uses. No Lua needed, and it works on the escrowed version.

```lua
Config.Integrations = {
    -- your prison has an export
    prison = { resource = 'my_prison', call = { type = 'export', name = 'JailPlayer', args = { 'src', 'minutes', 'reason' } } },
    -- your garage only needs a database change
    garage = { resource = 'my_garage', call = { type = 'sql', query = 'UPDATE owned_vehicles SET stored = 2 WHERE plate = ?', args = { 'plate' } } },
    -- your ambulance script sets a state bag
    death = { resource = 'my_ambulance', check = { type = 'statebag', key = 'isDead' } },
    -- your dispatch fires an event: say where coords / title / message are
    dispatch = {
        { resource = 'my_dispatch', event = 'my_dispatch:server:alert', args = { 'data' },
          fields = { coords = 'data.coords', title = 'data.title', message = 'data.message' } },
    },
}
```

| | |
| --- | --- |
| **Call types** | `export`, `event` (server event), `clientEvent` (sent to the player), `command` (console command, e.g. `'jail {src} {minutes}'`), `sql`, and `statebag` for client checks |
| **Placeholders in `args`** | `src`, `identifier`, `minutes`, `seconds`, `reason`, `plate`, `fee`, `netid`, `amount`, `society`... (full list in the config). Anything else is passed as written |
| **Categories** | `prison`, `garage`, `billing`, `banking`, `license`, `insurance`, `death`, `prisonstatus`, `dispatch` |

A configured integration wins over auto-detection while its resource runs.

## From your own scripts

* `exports.huncho_npcpolice:SetPlayerDowned(true/false)` and `SetPlayerJailed(true/false)` (client) tell the NPC police the player is down or in jail.
* `exports.huncho_npcpolice:Alert(playerId, 'storerobbery', coords)` (server) starts a response.

## `/npcpolicedetect`

Prints what was detected, and any running scripts that look like a prison, garage, ambulance, dispatch, billing, banking or inventory script but aren't supported.

Need more? Write a [custom adapter](custom-adapters.md).
