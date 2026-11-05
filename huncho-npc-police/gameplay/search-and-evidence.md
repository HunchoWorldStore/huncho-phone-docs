# Search, evidence & GSR

## Consent

After cuffing, the officer asks for consent to (`Config.Consent`):

* a **gunshot residue test** (gun crimes only)
* a **search**
* a **vehicle search** (for `Config.VehicleSearch` crimes)

Saying no is **Failure to Comply**: it's added to the charges and fines, and the evidence check is skipped, so they stay arrested even if nothing would have been found (`refusalKeepsCharges`). `decideTime` and `onTimeout` set the time to answer.

## What every arrest takes

| | Setting |
| --- | --- |
| Illegal items, whatever the arrest is for | `Config.Search.items` (ships empty: add your drugs, `black_money`...) |
| The crime's evidence items | `Config.Evidence.items` |
| Guns and ammo | Licensed players keep theirs only when it isn't a gun crime **and** the GSR is negative |
| ESX dirty money as an account (no ox\_inventory) | `Config.Search.dirtyMoneyAccount` |

## Charges need evidence

Charges listed in `Config.Evidence.items` only stick if at least one of their items is found (`'@firearm'` = any gun). Shooting charges need a gun found, and firing a firearm also needs a positive GSR (positive for `gsr.window` seconds after firing). Unproven charges are dropped.

If the main charge is dropped and only minor ones are left (Resisting, Evading...), the suspect is fined and released instead of jailed (`Config.Evidence.releaseIfOnlyMinorLeft`, `minorCharges`). Nothing left = uncuffed and let go with no record. Illegal items are still seized first.

## Vehicle searches

For drug, robbery, burglary, gun and car-theft charges (configurable), officers search the trunk and glovebox (ox\_inventory). Crime items go to the evidence stash, are listed on the paperwork and count as evidence. With `searchIfRefused`, refusing still gets the car searched.

## Evidence stash

Seized items go into the `huncho_npcpolice_evidence` stash (ox\_inventory), locked to your police jobs. `Config.Search.evidenceStash.groups` sets a minimum grade, `coords` limits where it can be opened.

| Command | Does |
| --- | --- |
| `/npcevidence` | Open the stash |
| `/npcreturn [id]` | Give a player their items back |

{% hint style="info" %}
Items are **never handed back automatically** by default. Set `Config.Search.returnItems.enabled = true` to return them after bond or a beaten case (`onRelease`), at the built-in jail pickup (`afterBuiltinJail`) or once out of another prison (`afterPrison`). Items in `neverReturn` (`'@weapons'` = every gun) stay in the stash for good.
{% endhint %}
