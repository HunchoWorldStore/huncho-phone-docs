# Installation

{% stepper %}
{% step %}
### Download

Download the pack from [keymaster.fivem.net](https://keymaster.fivem.net) under **Granted Assets**.
{% endstep %}

{% step %}
### Add the resource

Put the `hunchoworld_gamepack` folder in your `resources` folder.

{% hint style="danger" %}
**Keep the folder name `hunchoworld_gamepack`.** The item exports use it, so renaming it stops the items from working.
{% endhint %}
{% endstep %}

{% step %}
### Start it

In `server.cfg`, start it **after** ox\_lib, your framework, your inventory and your target:

```cfg
ensure ox_lib
ensure hunchoworld_gamepack
```
{% endstep %}

{% step %}
### Add the items

Paste the item file for your inventory and copy the images. See [Items](items.md).

Skip this for any game you only run by command.
{% endstep %}

{% step %}
### Restart and check the console

Restart the server. Each game prints what it found, for example:

```
[huncho_cardhub] framework: qbx | inventory: ox_inventory | placing tables by: both
[hunchoworld_ceelo] framework: qbx · inventory: ox_inventory · money: cash
```

If a line shows the wrong framework or inventory, set it by hand in that game's config.
{% endstep %}
{% endstepper %}

## Already running the standalone games?

Stop or remove the old standalone resources before starting the pack (`huncho_cardhub`, `hunchoworld_ceelo`, `sage_dominoes`, `sage_dominoes_props`, `hunchoworld_beerpong`, `sage_slumlords`, `hunchoworld_ohbihplease`, `tumbling_towers`). Running both doubles up every game.

On ox\_inventory and tgiann-inventory, point each item's `export` at `hunchoworld_gamepack` (for example `'hunchoworld_ceelo.useDice'` becomes `'hunchoworld_gamepack.useDice'`). The item files in the pack already do this.

## Next steps

* Open the [admin panel](../admin-panel.md) with `/gamepack` to turn games on or off, set stake limits and place permanent tables.
* Pick a [language](../languages.md).
* Read each game's page for its controls and config.
