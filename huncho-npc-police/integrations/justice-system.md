# Justice System

Works with the Justice System (`justice_core`, `sage_justicesystem`, `hunchoworld_justicesystem`, or a renamed copy). It's found **by its exports**, not its name: start it and the NPC police link up on their own:

```
[huncho_npcpolice] Justice System found: hunchoworld_justicesystem (MDT, dispatch, citations, prison)
```

With no Justice System running, nothing changes. Start both; the order doesn't matter.

## What officers see

* **Records in the Justice MDT.** AI arrests become arrest reports (charges mapped to your penal code, booking number, confiscated items as evidence, impounded plate), AI citations become citations, AI warrants become MDT warrants. All with an **AI** badge and the unit as author.
* **AI units on the dispatch board and live map**, with callsigns like `AI-12`.
* **AI activity feed** on the police dashboard.
* **Community service** goes through the Justice System ([Community service](../gameplay/community-service.md)).

## What officers can do

From the duty wheel → **AI units**, or the MDT:

| Order | What happens |
| --- | --- |
| Request backup (1-5 units + reason) | Cruisers come with the posture of the reason (below), attach to the officer's call, then hold formation, follow on foot or escort the officer's car |
| Cuff & search target | The closest backup unit cuffs the person aimed at (in the Justice System's cuffs) and searches them; the officer gets a search report and picks transport, release or hand over. Runners are chased |
| Chase target | On foot or in a vehicle, picked automatically |
| Weapons free / Hold fire / Engage target | Rules of engagement |
| Draw weapons / Holster / Set perimeter | The posture of the units on scene |
| Hold position / Cover me / Follow me | |
| Transport to booking | The cuffed suspect is driven to booking and handed over there |
| Set up checkpoint here | AI officers stop passing drivers and check license, registration, insurance, warrants / BOLO / stolen plates and ankle monitor curfew |
| Air unit | A police helicopter (below) |
| Dismiss units | |

Officer-requested units come **any time**, also while police are on duty.

## Backup postures

| Reason | En route | On scene | Weapons | Engage |
| --- | --- | --- | --- | --- |
| Traffic stop | lights only | parks behind the officer | holstered | return fire |
| Felony stop / high risk | code 3 | fan behind the officer, crews behind their doors | aimed at the vehicle | on command |
| Robbery / armed subject | code 3 | perimeter | aimed at the suspect | on command |
| Shots fired / active shooter | code 3 | fan / moves with the officer | rifles | weapons free |
| Pursuit / foot pursuit | code 3 | joins the pursuit | holstered / taser | return fire |
| Officer down | code 3, fastest | close cover | rifles | return fire |
| Crowd control | lights | fan | baton | return fire |
| Welfare check / medical / transport / checkpoint | calm | parks behind | holstered | return fire |

{% hint style="info" %}
**Units never start a fight.** They never target on-duty police, EMS or corrections, cuffed or surrendered players, or each other. `return_fire` = only whoever hurt the officer or a unit; `on_command` = also the armed person the officer ordered them to engage; `weapons_free` = also anyone armed and shooting or aiming at police.
{% endhint %}

## Air unit

A police helicopter (`polmav`, pilot + spotter, `Config.AirUnit`) is created near the requesting officer and flown by their game. It flies to the area, orbits it (searchlight at night) and climbs away when its flight time is up.

* **With the Justice System:** officers call it from the job menu or MDT; the Justice System handles cooldowns, pings and call notes. Long AI pursuits and escapes request it automatically.
* **Without it:** the same automatic requests for the NPC police's own chases; on-duty police see the helicopter on the map and get the suspect's position (`pingPolice`).

While the helicopter sees the suspect, the NPC police don't lose them.

## No double records, no double fines

`Config.Justice` (bottom of `config.lua`):

| Setting | Does |
| --- | --- |
| `records = 'writethrough'` | Arrests, citations and warrants are only kept in the Justice MDT (default). `'mirror'` also keeps the resource's own tables |
| `jailThroughJustice = true` | Booked and jailed through the Justice System |
| `finesThroughJustice = true` | Fines and citations billed by the Justice System, never taken twice |
| `Config.Bridge.mdt = 'auto'` | The Justice MDT when it runs, else wasabi\_mdt |

## Requirements

* The Justice System with its AI integration turned on. Version 1.4.3 or newer for everything.
* AI checkpoints are placed in the Justice System Staff Console (`/jcadmin` → World → AI checkpoints).
