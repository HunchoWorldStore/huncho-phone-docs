# Calls & alerts

There are three ways a crime reaches the NPC police. You can use any mix of them.

## 1. Your dispatch script (automatic)

The resource listens to every [supported dispatch script](../integrations/supported-resources.md) at once. An alert meant for police is matched to a `Config.Calls` entry in this order:

1. The alert's code. ps-dispatch codes like `storerobbery` match `Config.Calls` keys directly.
2. A phrase in its title or message, from `Config.DispatchKeywords` (for example "shots fired" → `shooting`).
3. `Config.DefaultCall`, if you set one.

Alerts containing `Config.IgnoreKeywords` (panic buttons, officer down, EMS) are skipped.

{% hint style="info" %}
Set `Config.Debug = true` to see every alert and what it matched in the server console.
{% endhint %}

## 2. Built-in detection (no dispatch needed)

The resource spots these itself (`Config.Gunshots`, `Config.Detection`), with **any** drug or robbery script:

| Crime | How it's spotted |
| --- | --- |
| Gunshots, fights, carjackings, explosions | Watched on the shooter's / attacker's game |
| Drug sales | The hand-off animation most drug scripts play next to a local, and with ox\_inventory a drug item (`items`) leaving the inventory face to face with a local. `chance` = % of sales called in |
| Car break-ins | Smashing or forcing a locked car while a local can see it (`needWitness`) |
| Robberies | Robbery animations (registers, safes, drills, hacking, jewelry cases, lockpicking), a gun out inside a robbery zone with a local there, or aiming at a store clerk |
| Crashing into a police car | Pulled over for Reckless Driving (`policecrash`) |
| Ambient patrols | Speeding over 85 mph (`speedLimitMph`), brandished guns |

The call follows the place: a vault drill at Pacific becomes a Pacific bank robbery, and the units sent match. Add your scripts' animations to `anims`, your MLO robbery spots to `zones`, and drug labs or job spots to `ignoreZones`.

While officers are on duty, these go to them instead: through the [built-in dispatch](built-in-dispatch.md), or pushed into ps-dispatch, cd\_dispatch, core\_dispatch, rcore\_dispatch or origen\_police (`Config.Dispatch.forwardToExternal`).

## 3. Exports from your own scripts (most reliable)

Some anticheats (for example ReaperV4) stop one resource from hearing another's events, which stops method 1. Exports aren't affected. See [Exports](../reference/exports.md):

```lua
-- server side: src = the player committing the crime
exports.huncho_npcpolice:Alert(src, 'storerobbery', GetEntityCoords(GetPlayerPed(src)))
```

## Turning calls on or off

Every entry in `Config.Calls` has `enabled = true`. Set it to `false` and the NPC police never answer that call, from any source:

```lua
vehicletheft = { enabled = false, charge = 'vehicle_theft', units = { 'patrol' } },
```

| Want to turn off | Call |
| --- | --- |
| Hitting or running over an officer with a car | `officerram` |
| Crashing into a cruiser = pulled over | `policecrash` |
| Speeding | `speeding` |
| Vehicle crimes | `vehicletheft`, `carjack`, `carboosting` |

A switched-off call also stops its keywords: a "house robbery" alert with house robberies off is ignored, not answered as a store robbery. `/npcpolicetest` still works for every call.

## Adding a crime from your own script

```lua
Config.Calls.myrobbery = { charge = 'robbery_store', units = { 'patrol', 'patrol' } }
```

Then send `exports.huncho_npcpolice:Alert(src, 'myrobbery')` from that script. If it checks a **minimum police count** before a robbery can start, add the virtual officers:

```lua
local cops = YourCopCountFunction()
if GetResourceState('huncho_npcpolice') == 'started' then
    cops = cops + exports.huncho_npcpolice:VirtualPoliceCount()
end
```

`VirtualPoliceCount()` returns `Config.CountAsPolice` while no real police are on duty, and `0` once someone clocks in.
