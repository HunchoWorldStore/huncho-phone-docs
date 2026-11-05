# Group crimes & shooting victims

## Accomplices

More than one suspect can be on a call (`Config.Accomplices`):

* Players within `nearbyRadius` of the suspect when units arrive, **only if they act involved** within `watchTime` (gun out, mask on, running or driving off). Bystanders who stay calm are left alone.
* Passengers in the suspect's car once it evades.
* Anyone who shoots or hits an officer during the call.

Each accomplice gets their own smaller response (`units`) and is booked separately. If the main suspect crashes or logs out, the rest of the group gets backup instead.

## Shooting victims

A player being shot at or hit by someone else is the **victim** for a minute (`Config.Victims`, `window`). Any alert that lands on them, like firing back in self-defense or a "shots fired" alert raised from their own game, goes to whoever shot them. If the shooter is gone, the alert is dropped.

* Only another real player counts by default (`npcAttackers = false`). Set it to `true` to count locals (NPC gangs) too.
* Whoever fires first is not a victim (`startedItWindow`).
* Officers (NPC or real) shooting at you never count.
* Victims are never pulled in as the shooter's accomplice.
