# Units, uniforms & sheriff

## Units

The defaults are vanilla GTA: `police` / `police2` / `police3`, sheriff cars, and the `riot` van for SWAT. Officers are the vanilla cop and sheriff peds with a combat pistol and stun gun, carbine rifles for SWAT.

Each unit in `Config.Units` (patrol, sheriff, SWAT) has its own `vehicles`, `livery`, `extras`, `outfits`, weapons, `accuracy` and `armour`. Addon cars, EUP and addon weapons all work. The K9 handler uses the patrol unit's car, uniform and weapons (`Config.K9`).

{% hint style="info" %}
A car or ped model that fails to load is skipped and the stock one is used. A weapon that isn't streamed falls back to `Config.FallbackWeapons` with a console warning.
{% endhint %}

## Your own uniform

{% stepper %}
{% step %}
### Dress up

Put an MP character in the uniform in game.
{% endstep %}

{% step %}
### Copy it

Run **`/npcpoliceoutfit`**. A ready-to-paste block is copied.
{% endstep %}

{% step %}
### Paste it

Paste it as that unit's `male = { ... }`, and `female = { ... }` from a female character. For female SWAT, also raise SWAT's `femaleChance`.
{% endstep %}
{% endstepper %}

The booking officer at the fingerprint scanner wears the uniform of `Config.Booking.officerUnit` (or the station's own `officerUnit`).

## Sheriff territory

Calls in Sandy Shores, Grapeseed and Paleto Bay are answered by the **sheriff** (`Config.SheriffAreas`): the first response, backup, roadblocks, the transport car, ambient patrols and the K9 handler. SWAT calls don't change. Sheriff cars carry `BCSO` plates (`platePrefix`).

Add more of Blaine County with GTA zone names in `zones` (Harmony `HARMO`, Alamo Sea `ALAMO`, Grand Senora Desert `DESRT`, Stab City `SLAB`, ...), or turn it off with `enabled = false`.

## Sirens

Units drive to a call without sirens and switch them on within `Config.Sirens.responseDistance`. Sirens are always on in pursuits and on the ride to the station (`Config.Transport`).
