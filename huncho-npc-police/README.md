---
description: NPC police for FiveM that answer your calls while no real officers are on duty.
cover: assets/banner.png
coverY: 0
---

# Huncho NPC Police

NPC police that respond to your dispatch alerts **while no real officers are on duty**. They drive to the call and order the suspect to surrender. Runners get tased, drivers get chased with backup, roadblocks, spike strips, PITs and a K9, and shooters get shot back. Then the suspect is searched, cuffed and driven to the station for a full booking (fingerprints, a mugshot to Discord, a holding cell with paperwork, bond and a lawyer) before going to your prison.

Works with **Qbox, QBCore, ESX and standalone servers**. Every integration is **auto-detected**, so in most cases you drop it in and start it.

## What's in it

| | |
| --- | --- |
| [**Responses**](gameplay/response.md) | Units drive to the call, sirens on close in, officers walk right up before cuffing, questioning or ticketing |
| [**Traffic stops**](gameplay/traffic-stops.md) | License, registration and insurance checks, a written citation to sign and pay or refuse |
| [**Pursuits**](gameplay/pursuits.md) | Backup, roadblocks, spike strips, PIT, box-in, K9, a police helicopter, felony stops, searching after losing you |
| [**Evidence**](gameplay/search-and-evidence.md) | Consent questions, GSR tests, body and vehicle searches, an evidence stash, charges only stick with evidence |
| [**Booking**](gameplay/booking.md) | Fingerprints, mugshot, holding cell paperwork, bond, lawyer, plead guilty and [community service](gameplay/community-service.md) |
| [**Jail & warrants**](gameplay/jail-and-warrants.md) | Your prison script or the built-in jail, records, repeat-offender sentences, warrants you can escape |
| [**Built-in dispatch**](setup/built-in-dispatch.md) | For servers without one: alerts, blips, GPS key, recent calls and `/911` |
| [**Justice System**](integrations/justice-system.md) | Records in the Justice MDT, AI units on the board, officer-requested backup, checkpoints, an air unit |

## Every install includes

* Auto-detection of your **framework, inventory, dispatch, prison, garage, banking, billing, MDT, licenses and ambulance** script ([list](integrations/supported-resources.md))
* A [difficulty switch](setup/difficulty.md): easy, normal, hard or custom, and your own single values always win
* [Unsupported scripts connected from the config](integrations/other-scripts.md), no Lua needed
* English and Spanish, easy to [translate](setup/languages.md)
* Open `config.lua`, `locales/`, `bridge/` and `server/config_server.lua` (they stay readable after escrow)

{% hint style="info" %}
New here? Start with [Requirements](getting-started/requirements.md), then [Installation](getting-started/installation.md). Then walk your map once with `/npcpolicecoords` ([Locations for your map](getting-started/locations.md)).
{% endhint %}

## Need help?

Check [Troubleshooting](reference/troubleshooting.md) first. If that doesn't fix it, open a ticket in our Discord with the start-up lines your server console printed (`[huncho_npcpolice] server framework: ...` and the lines after it) and the output of `/npcpolicedetect`.
