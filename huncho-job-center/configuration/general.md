# General settings

Everything lives in `config/`. The core scripts are encrypted; everything you'd want to change is open.

| File | What's in it |
|---|---|
| `main.lua` | Job Center location, deposit, damage fee, levels and pay multipliers, crews, job of the day, streak, leaderboard |
| `integrations.lua` | Which framework, target, inventory, banking, key, fuel and notification scripts to use (all `auto`) |
| `server.lua` | Server-only: Discord webhook and log settings (never sent to players) |
| `jobs/` | One file per job. See [Job files](job-files.md) |
| `uniforms.lua` | Clothing ID reference |
| `animations.lua` | Named animations, scenarios and props, plus carry animations |
| `bridge/` | The code that talks to other scripts. See [Using your own scripts](../integrations/custom-scripts.md) |
| `html/` | The menus and HUD (style, text, layout) |

## City name

The menu title, pay stub and job text use `Config.Branding`:

```lua
Config.Branding = {
    city           = 'Chicago',
    office         = '{city} Employment Office',
    centerLocation = 'downtown',
    thanks         = 'Thanks for keeping {city} running.',
}
```

Write `{city}` anywhere in a job's `description`, `tasks` or a tour stop's `info` and it's filled in.

## Level system

```lua
Config.LevelSystem = false
```

* `true`: players earn XP for every task. Their civilian level unlocks higher jobs (`level` on each job) and their level in a job adds a pay bonus (`Config.Levels`).
* `false`: no XP or levels. Every enabled job is open to everyone and each task pays exactly `payPerTask`.

## Deposit and vehicles

```lua
Config.Deposit         = 250     -- default vehicle deposit (a job can set its own)
Config.DepositAccount  = 'bank'
Config.ReturnDistance  = 35.0    -- how close to its spawn the vehicle must be at clock-out
Config.DamageFeeScale  = 1.0     -- 1.0 = a wrecked vehicle costs the whole deposit
Config.WarpIntoVehicle = false
```

## Doing tasks

Tasks are done by walking to the yellow marker and pressing **E**. `Config.TaskInteraction` sets the prompt distance, where the prompt shows and the marker's look. Set `useTarget = true` to use the target eye for tasks instead. `Config.InteractKey` changes the key.

## Blips

Each depot blip can be set in its job's `depot.blip` (`sprite`, `color`, `scale`, `label`, `shortRange`, `display`). Anything left out uses `Config.BlipDefaults`. `Config.ShowAllDepotBlips = false` only shows the depot for the job the player signed up for.

## Selling

Fish and finds are sold into `Config.SellAccount` (`cash` by default), each sale +/- `Config.SellVariance` %.

## Vehicle cleanup scripts

Every vehicle this script spawns gets the state bags in `Config.ProtectVehicleStates` (`noDelete = true` by default), so most `/dv` and cleanup scripts leave them alone.
