# Locations for your map

{% hint style="warning" %}
**Every location in `config.lua` is set for the vanilla GTA map.** If your server uses custom maps or MLOs (a new Mission Row, Bolingbroke, Sandy or Paleto station...), spots left on vanilla coords can put players inside walls or under the map.
{% endhint %}

Walk to each spot in game, run **`/npcpolicecoords`** (it prints your position and copies it as a `vec4`), and paste it over the matching coords.

| Spots | Where in the config |
| --- | --- |
| Booking stations: drop-off, fingerprints, mugshot, holding cells, release | `Config.Booking.stations` |
| Built-in jail: spawn, release, yard task spots, belongings pickup | `Config.BuiltinJail` |
| Prison zones (a jailed player outside every zone counts as free) | `Config.PrisonCheck` |
| Built-in community service area and release | `Config.CommunityService` |
| Gunshot ignore zones (ranges, gun stores) | `Config.Gunshots` |
| Robbery zones (banks, stores, jewelry) | `Config.Detection.robbery.zones` |
| Ambient patrol areas | `Config.AmbientPatrols` |

## Booking stations

You can add as many stations as you like. `station = 'nearest'` picks the closest one. A station can set its own `officerUnit` (for example `'sheriff'` for Sandy Shores) and its own `release` spot where players walk out after bond or a dismissed case.
