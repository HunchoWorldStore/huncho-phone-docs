# Jail, warrants & release

## Prison

Sentences go to your prison script, auto-detected ([Supported resources](../integrations/supported-resources.md)). If jailing through it fails, the built-in jail takes over.

{% hint style="info" %}
**Jailed players are only ignored inside a prison.** A player a prison script calls jailed, but who is outside every `Config.PrisonCheck` zone (Bolingbroke by default; add your prison MLO), is treated as free.
{% endhint %}

## Built-in jail

Used when there's no prison script. It holds the player inside Bolingbroke for the sentence, keeps their time through relogs, and releases them outside the gate. `Config.BuiltinJail.secondsPerUnit` sets how long one sentence unit lasts.

* **Prison tasks:** marked spots in the yard, press **E**, `tasks.reduceSeconds` off per task.
* **Belongings:** players go in with nothing; their items are handed back at a pickup outside the gate. Items in `belongings.keep` (for example `'phone'`) stay with them. `belongings.enabled = false` turns it off.
* `/npcunjail [id]` releases someone early (`Config.Unjail`).

## Records

Every arrest and citation is recorded (your MDT, the [Justice System](../integrations/justice-system.md), or the resource's own tables). Repeat offenders get longer sentences: `boostPerPrior` per prior arrest, up to `maxBoost` (`Config.Records`).

`/npcpoliceclearrecord [id] [yes]` wipes everything the NPC police wrote about a character. Officer-written records are kept.

## Warrants

Escaping after police arrived gives a warrant (`Config.Warrants`, `durationHours`), as does going down without being arrested (`Config.DownedWarrant`).

* **Getting away works** (`patrolsArrest = false`, default): patrols that see a wanted player leave them alone. The warrant's charges are added the next time they're caught for a new crime, so they're jailed for both.
* `patrolsArrest = true`: patrols arrest wanted players on sight, if they still match the [description](pursuits.md#descriptions).

`/npcpoliceclearwarrant [id]` clears one.

## Release cooldown

After serving time the NPC police leave that character alone for 15 minutes (`Config.ReleaseCooldown.afterJail`), and for 10 minutes after walking out on bond, a lawyer or auto-bail (`afterBail`). Release is detected for any prison script.
