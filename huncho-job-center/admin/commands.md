# Commands

| Command | Who | What it does |
|---|---|---|
| `/endshift` | Players | End your shift from anywhere. A confirm box shows your pay and what happens to the deposit. Default key **F7** (rebind in Settings > Key Bindings > FiveM). Rename or turn off in `Config.EndShift`. |
| `/jcshifts` | Admin | Everyone on shift: job, tasks, earnings, time and crew. Teleport to them, or end their shift with or without pay. |
| `/jcpay` | Admin | Pay overview: real $/hour per job, hours worked, average time per task and total paid out, with **High**/**Low** markers for balancing. |
| `/jcpayreset` | Admin | Clear the pay overview numbers and start fresh. |
| `/jcdaily [job]` | Admin | Set today's job of the day, e.g. `/jcdaily garbage`. No job = back to automatic. |
| `/jclocations` | Admin | Move any depot, spawn, shop, stop, house, area, shelf or bin in game. Saved in the database and kept after restarts. |
| `/jcuniforms` | Admin | Dress any job's uniform in a built-in clothing menu (or save what you're wearing), preview it, or turn it off. Saved in the database and kept after restarts. |
| `/jcjobs` | Admin | Turn any job on or off. A job turned off disappears from the Job Center and the map, and nobody can sign up; players already on shift finish normally. Saved in the database and kept after restarts. |
| `/jcoutfit` | Admin | Copy your current outfit as a paste-ready uniform for the config files. |
| `/jccoords` | Admin | Copy your position as `vec4(x, y, z, heading)` for the config files. |

Who counts as an admin is set in `config/integrations.lua`: the aces in `AdminAces` (`group.admin` by default) on any framework, plus the QBCore permissions or ESX groups in `AdminGroups`.

## Giving someone access to one command

On any framework you can give a group a single command with an ace, for example:

```
add_ace group.mod command.jcshifts allow
```
