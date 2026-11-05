# Troubleshooting

<details>

<summary>Police never show up</summary>

Turn on `Config.Debug` and trigger an alert.

* **No log line at all:** your dispatch isn't being heard (an anticheat blocking events, or an unsupported dispatch). Use the `Alert` [export](exports.md) from the crime script, or connect the dispatch in [Other scripts](../integrations/other-scripts.md).
* **`ignored: police on duty`:** more players with a police job are on duty than `Config.MaxPoliceOnDuty` allows (default 0).
* **The call is switched off:** check `enabled` on that `Config.Calls` entry.

</details>

<details>

<summary>The wrong script was picked</summary>

Force it in `Config.Bridge`, for example `Config.Bridge.prison = 'builtin'`. `/npcpolicedetect` shows what was found.

</details>

<details>

<summary>Players end up in walls or under the map</summary>

The locations are for the vanilla map. Move them onto your MLOs with `/npcpolicecoords` ([Locations for your map](../getting-started/locations.md)).

</details>

<details>

<summary>No mugshot photo</summary>

You need `screenshot-basic` (or the `screenshot` fork) running, and a webhook in `server/config_server.lua`. The booking is still posted without a photo.

</details>

<details>

<summary>Officers punch instead of shooting</summary>

An addon weapon isn't streamed. The resource falls back to `Config.FallbackWeapons` and prints a warning.

</details>

<details>

<summary>A jailed player still gets arrested</summary>

They're outside every `Config.PrisonCheck` zone. Add a zone for your prison MLO.

</details>

<details>

<summary>Community service goes to the wrong script</summary>

The console prints the order it uses at start (`community service: ...`). Set `Config.CommunityService.provider` to `'builtin'` or to one script's name. With the Justice System, add `huncho_npcpolice` to its `Config.API.allowedResources` when that list isn't empty.

</details>

<details>

<summary>ak47_drugmanager sales aren't reported</summary>

The built-in drug-sale detection (`Config.Detection.drugsell`) picks them up without ak47. Add your drug items to its `items` list. You can also add `exports.huncho_npcpolice:Alert('drugsell')` in ak47's dispatch function.

</details>

<details>

<summary>Something broke after updating</summary>

`config.lua`, `bridge/` and `locales/` aren't escrowed, so it's easy to keep old copies by mistake. Use the new files and copy your settings back in ([Updating](../getting-started/updating.md)).

</details>

## Still stuck?

Open a ticket in our Discord with your console's start-up lines and the output of `/npcpolicedetect`.
