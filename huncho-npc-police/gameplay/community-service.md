# Community service

Offered in the holding cell ([Bond & Counsel](booking.md)) as a swap for prison, for minor charges only (`Config.CommunityService`).

## Who can get it

* **Every charge** has to be in `charges`. One charge that isn't (a drug sale, a robbery...) rules it out, and the screen names the charge that blocked it.
* The sentence for those charges is `maxSentence` or less (15 by default). The repeat-offender boost isn't counted, so priors don't rule it out.
* Not after pleading guilty. Fight arrests get it next to the automatic bail (`fights = true`).

The sentence becomes `tasksPerUnit` tasks per month, between `minTasks` and `maxTasks`.

| Default charges | |
| --- | --- |
| Assault & Battery, Resisting Arrest, Vandalism, Suspicious Activity, Speeding, Reckless Driving | Driving Without a License, Unregistered Vehicle, No Proof of Insurance, Failure to Comply, Poaching, Evading Police |

## Your community service script is used

With `provider = 'auto'`, the first script in `order` that's running and takes the player gets them. If none do, the built-in one runs.

| Script | How |
| --- | --- |
| **Justice System** | `AssignCommunityService`. It runs the service with whatever community service its own config uses, and keeps it in its MDT |
| **sleezy\_coms** | `AssignService` |
| **randol\_service** | Needs three exports added (below) |
| **bc\_communityservice** | `GivePlayerCommunityservice` |
| **esx\_communityservice**, **mh-communityservice** | Their server events |
| **rcore\_prison** COMS | `StartCOMS`. Skipped when rcore refuses (COMS turned off) |

The console shows what it found at start:

```
[huncho_npcpolice] community service: justice > rcore_prison > built-in
```

| `provider` | Does |
| --- | --- |
| `'auto'` | The first script of `order` that's running (default) |
| `'builtin'` | Always the built-in one |
| `'sleezy_coms'` (any name from the list) | Only that script |

Your own script instead: `external = function(src, tasks, booking) ... return true end`.

{% hint style="info" %}
**Handed to another script:** its own task spots are used, so set them up in that script. For example, the Justice System's are in its Staff Console (World → Community service). With none set there, players get no markers. To always use the built-in one (markers, map blip, GPS, `/npcpolicecsedit`), set `provider = 'builtin'`.
{% endhint %}

{% hint style="warning" %}
**Justice System:** if its `Config.API.allowedResources` isn't empty, add `huncho_npcpolice` to it. Otherwise it refuses, and the next script in `order` is used.
{% endhint %}

## Built-in community service

The player is taken to the **aircraft carrier** and sweeps up at its task spots (the ones sleezy\_coms uses; sleezy\_coms itself isn't needed and the carrier map is loaded for them). Each spot gets a marker, a blip and a GPS waypoint. When they're done they're released at LSIA (`release`).

* Leaving the area (`radius` around `center`) puts them back.
* Logging out, or not finishing within `maxMinutes`, means prison after all.
* Somewhere else: set it up in game (below), or change `location`, `center`, `radius`, `release` and `spots` in the config. No spots = random spots around the area.

### Setting it up in game

Run **`/npcpolicecsedit`** (admin, `editCommand`) and stand where each thing should be:

| Option | Does |
| --- | --- |
| Set start point here | Where players arrive |
| Set area here | The area around you (radius you pick); leaving it puts them back |
| Set release point here / No release point | Where they're let go when done, or stay where they finish |
| Add task spot here | A task spot where you stand, with an optional name ("Sweep the walkway") |
| Show spots | Markers, names and map blips for every spot for 2 minutes |
| A spot in the list | Teleport to it, or remove it |
| Reset to config.lua | Remove everything set in game and use the config again |

It's saved on the server and survives restarts and updates.

## Ending it early (staff)

`/npcpoliceremovecs [id]` (`removeCommand`, `group.admin`) ends a player's community service:

| Where they are | |
| --- | --- |
| Built-in, sleezy\_coms, randol\_service, esx\_ / mh-communityservice | Ended by the command |
| Justice System | Its release export when it has one, otherwise through the script it sent them to |
| rcore\_prison, bc\_communityservice | No way for another script to end it: the command tells staff to use their own command (rcore: `/removecs`) |

## randol\_service exports

randol\_service only has police commands, so another script can't start it. Add these at the bottom of its `sv_service.lua`:

```lua
exports('AssignService', function(src, tasks)
    local Player = GetPlayer(src) if not Player then return false end
    local cid = GetPlyIdentifier(Player)
    tasks = math.min(maxTasks, math.floor(tonumber(tasks) or 0))
    if tasks < 1 or players[cid] then return false end
    players[cid] = { tasksleft = tasks }
    MySQL.insert.await('INSERT INTO randol_cs (cid, tasksleft) VALUE (?, ?)', {cid, tasks})
    TriggerClientEvent('randol_cs:client:sendtoService', src, tasks, true)
    return true
end)

exports('RemoveService', function(src)
    local Player = GetPlayer(src) if not Player then return false end
    local cid = GetPlyIdentifier(Player)
    if not players[cid] then return false end
    players[cid] = nil
    MySQL.query.await('DELETE FROM randol_cs WHERE cid = ?', {cid})
    TriggerClientEvent('randol_cs:client:finishService', src)
    return true
end)

exports('GetService', function(src)
    local Player = GetPlayer(src) if not Player then return nil end
    local e = players[GetPlyIdentifier(Player)]
    return e and e.tasksleft or nil
end)
```
