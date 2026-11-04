# Exports

## Client

```lua
exports.hunchoworld_gamepack:IsPlaying()              -- Beer Pong: in a lobby, a game, or watching
exports.hunchoworld_gamepack:IsBeerPongTable(entity)  -- Beer Pong: that entity is a beer pong table
exports.hunchoworld_gamepack:IsNearBeerPongTable(3.0) -- Beer Pong: within 3 m of a table
exports.hunchoworld_gamepack:IsSeatedAtSlumlords()    -- Slumlords: sitting at a table
```

## Server

```lua
exports.hunchoworld_gamepack:IsPlayingSlumlords(source)   -- Slumlords: seated at a table
exports.hunchoworld_gamepack:GetSlumlordsTableId(source)  -- Slumlords: their table id, or nil
```

## Item exports

The item files call these. You only need them if you write your own item entries.

| Export | Item |
| --- | --- |
| `useCardTable` | `card_table` |
| `useDice` | `ceelo_dice` |
| `useTableItem` | `domino_table` |
| `useKit` | `beerpong_kit` |
| `useDeck` | `ohbihplease_deck` |
| `useRouletteWheel` | `bihroulette_wheel` |
| `useBoard` | `slumlords_board` |
| `useTowerSet` | `tumbling_towers` |

## Hooks

Each game has open files for your own code:

| Game | File | Hooks |
| --- | --- | --- |
| Beer Pong | `bridge/client.lua`, `bridge/server.lua` | `OnEnterGame`, `OnLeaveGame`, `OnGameEnd`, `OnTablePlaced`, `OnTableRemoved` |
| Card Hub | `editable/server.lua`, `editable/client.lua` | Framework, money, items, logs, notifications, sit/stand |
| Cee-lo | `custom/server.lua` | Webhook, police dispatch, who may open tables, round end |
| Oh Bih Please / Roulette | `editable/client.lua`, `editable/server.lua` | `OnDrink`, `OnGameEnd`, notifications, sit/stand |
| Dominoes, Slumlords | `bridge/server.lua`, `bridge/client.lua` | Framework, money, items, target, notifications |

{% hint style="info" %}
Every game script starts with `local _ENV = HWGP.env('<game>')`. That keeps each game's globals separate. Leave that line in place when editing the open files.
{% endhint %}
