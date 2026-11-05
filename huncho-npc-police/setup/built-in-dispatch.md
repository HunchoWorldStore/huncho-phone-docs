# Built-in dispatch

If none of the supported dispatch scripts is running, the resource turns on its own dispatch (`Config.Dispatch.enabled = 'auto'`; `true` forces it on, `false` turns it off).

Every call (built-in detection, exports from your scripts, ambient patrol sightings) is also sent to on-duty **real** officers:

* A notification with the 10-code, call type, street and area, and the suspect (gender, on foot or vehicle + plate)
* A flashing blip with a search-area circle that fades after `blip.time` seconds
* **Y** (`waypointKey`, rebindable) sets GPS to the latest call
* `/npccalls` lists recent calls to pick from
* `/911 <message>` lets players call the police themselves (caller name + location, `call911`)

The NPC police still answer calls while no officers are on duty. Change the codes, titles and blip icons per call in `Config.Dispatch.calls`.
