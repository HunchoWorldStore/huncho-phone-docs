# Booking & the holding cell

## At the station

The cruiser pulls into the nearest station (`Config.Booking.stations`, `station = 'nearest'`). The suspect is walked through:

1. **Fingerprints** at the scanner, taken by the booking officer (`Config.Booking.officerUnit`).
2. **Mugshot**, posted to Discord with the charges when you set `MugshotWebhook` in `server/config_server.lua` (needs screenshot-basic).
3. **Holding cell** with the arrest paperwork on screen: charges, sentence, fines, items seized. **K** shows and hides it.

Fines are taken in the cell. Then the suspect goes to prison, unless they get out first.

## Bond & Counsel

In the holding cell the suspect presses **B** (`Config.Bail.key`) to open the **Bond & Counsel** screen. It shows the bond amount (or why there's none), the lawyer fee and the chance to beat the case, with a review bar and a stamp for the result.

| Choice | When | What happens |
| --- | --- | --- |
| **Post bond** | Every charge is in `Config.Bail.bondCharges` (minor crimes) | Paid = released out the front of the station, no prison |
| **Call a lawyer** | Serious charges (no bond) | `Config.Lawyer.fee`, one try per arrest. `beatChance`% to have the charges dismissed, fines refunded |
| **Plead guilty** | Any sentence | `Config.Plea.reduction`% off (25 by default), straight to prison. No lawyer after that |
| **Community service** | Minor charges, short sentences | Service tasks instead of prison. See [Community service](community-service.md) |

### Fights

Arrests where every charge is in `Config.Bail.autoBailCharges` (fights) never go to prison. When the holding cell time is up, bail is taken automatically and the suspect walks out (released anyway if they can't pay, noted as unpaid).

### Bond amount

```
base + (sentence x perUnit) + each charge's bond in amounts
then x multiplier, kept between min and max, unpaid fines added
```

Set `autoBailAmount` for a fixed fight bail. Lawyers can also get a shorter sentence when they lose (`reduceChance`, `reduction`).

## Ride to the station

Sirens on, code 3 (`Config.Transport`). After `Config.Transport.skip.after` seconds the suspect can press **G** to skip the ride and be taken out of the car at the station.
