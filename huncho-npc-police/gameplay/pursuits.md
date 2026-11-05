# Pursuits, felony stops & escaping

## Pursuit tactics

| | Setting |
| --- | --- |
| Backup units join the chase | `Config.PursuitBackup` |
| Roadblocks, with spike strips | `Config.Roadblocks` |
| PIT maneuver from the rear quarter | `Config.PIT` |
| Boxing in a car that slows down or stops | `Config.BoxIn` |
| K9 on runners | `Config.K9` |
| Police helicopter on long chases | `Config.AirUnit` |

## Felony stops

A suspect wanted for more than a ticket who stops their car with officers on scene gets a high-risk stop (`Config.FelonyStop`):

1. Cruisers stop back (`standOff`), officers take cover behind their doors with guns on the car.
2. Orders, `stepTime` seconds each: engine off and step out, then walk back with hands up.
3. Reaching the officers hands over to the normal arrest.

Staying in the car gets them pulled out by an officer at the door, plus **Resisting**. Driving off restarts the chase.

## Losing sight

Once officers can't see the suspect, they search around where they were last seen and the way they were heading (`Config.LostSuspect`): on foot for a runner, along the roads for a driver. They don't head straight for the suspect's real position, and PITs, roadblocks and gunfire pause until they're seen again. The helicopter seeing them guides officers in.

## Escaping

Out of sight for `Config.EscapeTime` seconds = escaped. The timer doesn't run while an officer is right next to them on the same level (`closeRange`). Escaping gives a [warrant](jail-and-warrants.md#warrants).

## Descriptions

Officers note what the suspect wears (top, pants, shoes, mask, hat) and drives (`Config.Descriptions`). A suspect who changed clothes, put on or took off a mask, or switched cars is only recognised up close (`recognizeDistance`). The description goes on the warrant: *suspect: male, masked, last seen in a Sultan (ABC123)*.
