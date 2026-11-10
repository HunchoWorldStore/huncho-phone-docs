# Job files

Each job has its own file in `config/jobs/` (`garbage.lua`, `taxi.lua`, ...). Everything for that job is in it: on/off, pay, depot, vehicle, blip, work locations, steps and its uniform. `config/jobs/README.txt` explains every field.

## Common fields

| Field | What it does |
|---|---|
| `enabled` | `false` removes the job completely |
| `payPerTask` | Money per finished task. Adds up during the shift and is paid at clock-out |
| `label`, `category`, `icon`, `color` | Name, menu tab, Font Awesome icon and accent color |
| `image` | `'images/<file>.png'` in `html/images/`, or a full URL. `nil` shows an illustrated card. Around 800x400 works best |
| `description`, `tasks` | Text on the job card. `{city}` is filled in |
| `level` | Civilian level needed (ignored with the level system off) |
| `xpPerStop` | Job XP per task |
| `minStopTime` | Minimum seconds between tasks (anti-exploit) |
| `uniform` | Which uniform to wear. Defaults to the one at the bottom of the file, `false` = none |
| `crew` | `true` or a number (e.g. `crew = 2`) to allow crews |
| `depot` | `{ coords, ped, scenario, label, blip }` |
| `vehicle` | `{ model, label, spawn, livery, color, extras, deposit, type }`. Set `type` for bikes, boats and aircraft |

## Modes

| Mode | Used for |
|---|---|
| `work` | Stops with on-foot steps, animations and props |
| `route` | Driving through checkpoints. `ordered = true`, optional NPC `passengers` |
| `passenger` | Taxi style: random pickup and drop-off for each fare |

## Pay

Every job has `payPerTask`. The running total shows on the HUD and is paid in one go at clock-out. Level, crew, job of the day and streak bonuses multiply it, and every bonus is listed on the pay stub. Use `/jcpay` to see the real $/hour of every job and balance them.

## Tasks never run out

Once a shift starts, tasks keep coming until the player clocks out. Random jobs work through every location in a shuffled order, then reshuffle (never the same spot twice in a row). Ordered jobs (bus, tour) loop back to the first stop.
