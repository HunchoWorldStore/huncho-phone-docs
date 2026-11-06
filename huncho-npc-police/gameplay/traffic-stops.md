# Traffic stops & citations

## The stop

On ticket-only calls the cruiser follows with its lights on at `followDistance` and parks `parkBehind` meters behind the car once it stops (`Config.TrafficStops`). It doesn't ram or PIT. Drive off and it becomes a [pursuit](pursuits.md).

The officer walks up and says why: "I pulled you over for Speeding", "License and registration, please".

## License, registration & insurance

Checked with your own scripts, auto-detected (`Config.Citations`):

| Check | Setting | Missing = |
| --- | --- | --- |
| Driver's license | `driverLicense` | *Driving Without a License* |
| Registration | `registration` | *Unregistered Vehicle* |
| Insurance | `registration` | *No Proof of Insurance* |

* Insurance and registration use m-Insurance when it runs. Without an insurance script, a car with no owner (NPC / stolen) counts as unregistered and insurance is skipped.
* **Paper items:** put your registration / insurance item names in `registration.items` and the player must carry them. With `metadata.plate` an item only counts for that car (`matchPlate`).
* **Impound:** each check has an `impoundChance` % chance the car is impounded once the ticket is paid.
* **Three strikes:** missing papers are a ticket the first two times. The 3rd time caught, the officer arrests you instead of writing a ticket, and you get bond or community service in the holding cell. He warns you on the 2nd time. Set it in `Config.Citations.repeatOffense` (`arrestAfter`, `charges`, `resetOnArrest`).
* Turn everything off with `Config.Citations.checkDocuments = false`, or one check with its `enabled`.
* Unsupported license or insurance script? Connect it in [Other scripts](../integrations/other-scripts.md).

## The citation

When every charge has a fine, the officer writes a ticket instead of cuffing. It shows on screen with the violations, fines, plate, location and the officer's signature:

* **Sign & Pay:** the fine is taken and they're free to go. Can't pay = arrested.
* **Refuse to sign:** arrested.

`Config.Citations.ticket` sets the time to decide (`decideTime`) and what happens if they don't pick (`onTimeout = 'pay'` or `'refuse'`). `enabled = false` goes back to paying automatically. A signed and paid ticket never searches anyone.

## Crashing into police

Hitting an NPC police car (`Config.Detection.policecrash`) gets you pulled over for **Reckless Driving**. Running turns it into a pursuit.
