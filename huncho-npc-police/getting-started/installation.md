# Installation

{% stepper %}
{% step %}
### Download

Download the resource from [keymaster.fivem.net](https://keymaster.fivem.net) under **Granted Assets**.
{% endstep %}

{% step %}
### Add the resource

Put the `huncho_npcpolice` folder in your `resources` folder.

{% hint style="danger" %}
**Keep the folder name `huncho_npcpolice`.** Other scripts call its exports by that name.
{% endhint %}
{% endstep %}

{% step %}
### Start it

In `server.cfg`, start it **after** your framework and the scripts it uses:

```cfg
ensure ox_lib
ensure oxmysql
ensure qbx_core        # or qb-core / es_extended
# ... your inventory, dispatch, prison, garage, banking, mdt ...
ensure huncho_npcpolice
```

The database tables (`huncho_npcpolice_records`, `huncho_npcpolice_warrants`, `huncho_npcpolice_jail`) are created automatically.
{% endstep %}

{% step %}
### Add your illegal items

Add your server's illegal items (drugs, `black_money`, ...) to `Config.Search.items` in `config.lua`. The list ships **empty** on purpose. Every arrest takes these items. See [Search, evidence & GSR](../gameplay/search-and-evidence.md).
{% endstep %}

{% step %}
### Mugshots to Discord (optional)

Paste a Discord webhook into `MugshotWebhook` in `server/config_server.lua`. That file only runs on the server, so players never see it.
{% endstep %}

{% step %}
### Restart and check the console

About 3 seconds after the resource starts, the console prints what it found:

```
[huncho_npcpolice] server framework: qbx
[huncho_npcpolice] server inventory: ox_inventory
[huncho_npcpolice] server prison: rcore_prison
[huncho_npcpolice] community service: rcore_prison > built-in
```

If a line shows the wrong script, force it in `Config.Bridge` (for example `Config.Bridge.prison = 'builtin'`).
{% endstep %}

{% step %}
### Test it

In game, run `/npcpolicetest` (admin). Units are sent to you, even while police are on duty.
{% endstep %}
{% endstepper %}

## Next steps

* [Locations for your map](locations.md): move the stations and jail spots onto your MLOs
* [Difficulty](../setup/difficulty.md): how tough the police are
* [Calls & alerts](../setup/calls-and-alerts.md): which crimes they answer
