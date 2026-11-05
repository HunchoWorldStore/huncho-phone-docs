# Working with real police

| Setting | Does |
| --- | --- |
| `Config.OnlyWhenNoPolice = true` | The NPC police only answer while no real police are on duty (default) |
| `Config.MaxPoliceOnDuty = 0` | Raise it to help a small force: with `2` they keep answering while 0-2 officers are on duty |
| `Config.OnlyWhenNoPolice = false` | Answer no matter how many officers are on |
| `Config.PoliceJobs` / `Config.PoliceJobType` | Which jobs count as police |

## Handing off

When officers clock in mid-call, `Config.Handoff` sends a takeover alert with the suspect's location, charges and plate through your dispatch, notifies on-duty officers and puts a blip on the suspect. The NPC police keep following for `followTime` seconds, or until a real officer is within `closeDistance`, then break off.

## Officer-requested backup

With the [Justice System](../integrations/justice-system.md), real officers can call AI units for backup, cuff and search, chases, checkpoints and an air unit, any time.
