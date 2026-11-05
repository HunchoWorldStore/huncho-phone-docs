# Exports

## Server

### Alert

Start a response on a player.

```lua
-- src = the player committing the crime, callKey = a Config.Calls key, coords optional
if GetResourceState('huncho_npcpolice') == 'started' then
    exports.huncho_npcpolice:Alert(src, 'storerobbery', GetEntityCoords(GetPlayerPed(src)))
end
```

### VirtualPoliceCount

```lua
local extra = exports.huncho_npcpolice:VirtualPoliceCount()
```

Returns `Config.CountAsPolice` while no real police are on duty, `0` once someone clocks in. Add it to a robbery script's police count so robberies can start while the NPC police cover.

### IsNPCActive

```lua
local covering = exports.huncho_npcpolice:IsNPCActive()
```

`true` while the NPC police are covering (no officers on duty).

### HasActiveCase

```lua
local busy = exports.huncho_npcpolice:HasActiveCase(src)
```

`true` if NPC police are currently on that player.

## Client

### Alert

The player running the code is the suspect.

```lua
if GetResourceState('huncho_npcpolice') == 'started' then
    exports.huncho_npcpolice:Alert('houserobbery')
end
```

### SetPlayerDowned / SetPlayerJailed

```lua
exports.huncho_npcpolice:SetPlayerDowned(true)   -- false when revived
exports.huncho_npcpolice:SetPlayerJailed(true)   -- false when released
```

Tell the NPC police the player is down or in jail, for ambulance or prison scripts that aren't [supported](../integrations/supported-resources.md).

{% hint style="info" %}
Vehicle cleanup scripts can skip NPC police vehicles: every one carries the state bag `npcpolice` (`Entity(vehicle).state.npcpolice`).
{% endhint %}
