# Difficulty

One switch at the top of `config.lua`:

```lua
Config.Difficulty = 'normal'   -- 'easy' | 'normal' | 'hard' | 'custom'
```

| | easy | normal | hard |
| --- | --- | --- | --- |
| Damage per hit when officers shoot you | 6-12 | 10-18 | 18-30 |
| Officer accuracy / armour | x0.5 | x0.75 | full |
| Seconds to put hands up / holster a gun | 15 | 12 | 10 |
| PIT chance, roadblocks, spike strips | 25%, 1, no spikes | 40%, 1 | 60%, 2 |
| K9 chance, max units on one player | 35%, 3 | 50%, 5 | 70%, 6 |
| Seconds out of sight to escape | 30 | 40 | 45 |

`hard` is the full-strength police. `custom` ignores the presets and uses the config exactly as written.

## Your own values always win

Change any single setting where it normally lives, for example `Config.PIT.chance = 30`, `Config.K9.chance = 40` or `Config.Units.swat.accuracy = 60`, and the difficulty leaves it alone. A preset only changes settings that are still at their shipped default. The console lists what it kept:

```
[huncho_npcpolice] difficulty: normal (your own values kept: PIT.chance)
```

`Config.DifficultyTweaks` takes single values that are applied last, on top of everything (same names as the presets, for example `['PIT.chance'] = 30`). The presets themselves are plain lists in `Config.DifficultyPresets`.
