# How a response plays out

{% stepper %}
{% step %}
### The call

A crime reaches the NPC police ([Calls & alerts](../setup/calls-and-alerts.md)). After `Config.ResponseDelay`, units spawn out of sight and drive in. The suspect gets a notice that police are on the way (`Config.NotifySuspect`).
{% endstep %}

{% step %}
### On scene

Officers get out, draw and order the suspect to surrender. The suspect has `Config.ComplyTime` seconds to put their hands up (**E**, `Config.SurrenderKey`) and holster any gun. Officers say what's going on over their heads ("You're being stopped for Armed Robbery. Hands up!", `Config.Speech`).
{% endstep %}

{% step %}
### Running or fighting

Runners are chased on foot (officers vault low fences, climb ladders and drop off ledges, `Config.OfficerMovement`) and tased within `Config.TaserRange`. Drivers get a [pursuit](pursuits.md). Shooting or ramming an officer means they shoot back.
{% endstep %}

{% step %}
### Cuffed

An officer walks right up (`Config.CloseRange`) and cuffs them. Nothing is done from across the street, through a wall or from another floor.
{% endstep %}

{% step %}
### Questions and search

Consent questions, a GSR test, the body search and a vehicle search ([Search, evidence & GSR](search-and-evidence.md)). Charges without evidence are dropped.
{% endstep %}

{% step %}
### Transport and booking

A code 3 ride to the nearest station (the suspect can press **G** to skip after a while), then fingerprints, a mugshot and the holding cell ([Booking](booking.md)).
{% endstep %}

{% step %}
### Prison or release

Prison through your script or the built-in jail, or out on bond, a lawyer, community service or a fine ([Jail, warrants & release](jail-and-warrants.md)).
{% endstep %}
{% endstepper %}

## Going down

* `Config.JailOnDeath = true`: after the revive an officer comes to the player and arrests them. They have to actually walk there; police can't get into locked areas or houses.
* `Config.JailOnDeath = false`: going down ends the response.
* `Config.DownedWarrant = true` (default): a downed player who isn't arrested gets a [warrant](jail-and-warrants.md#warrants) instead.

## Logging out

Logging out mid-arrest (`Config.JailOnDisconnect`) means jail on the next login.

## Players at home

Alerts that don't come from the suspect never pick a player in another instance (house routing bucket) or on another level (`Config.SuspectMaxHeight`, house shells).
