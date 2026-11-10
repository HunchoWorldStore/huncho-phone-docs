# Updating

{% stepper %}
{% step %}
### Back up your edits

Copy your `config.lua`, `server/config_server.lua`, `locales/` and any custom adapters in `bridge/`.
{% endstep %}

{% step %}
### Replace the resource

Download the new version from keymaster and replace the whole `huncho_npcpolice` folder. Bought it on the [Huncho World FiveM Store](https://huncho-world-fivem-store.tebex.store/)? It shows up in Keymaster under your Cfx account.
{% endstep %}

{% step %}
### Put your settings back

Copy your settings into the **new** `config.lua` rather than dropping your old file in. New versions add settings and bridge functions; an old file can be missing them.
{% endstep %}

{% step %}
### Restart and read the console

Check the detection lines and the difficulty line (`difficulty: normal (your own values kept: ...)`).
{% endstep %}
{% endstepper %}

{% hint style="info" %}
The server checks for updates on start and prints **Update available** with the changelog. Turn it off with `Config.VersionCheck = false`.
{% endhint %}
