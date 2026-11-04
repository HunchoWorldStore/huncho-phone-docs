# Requirements

| | |
| --- | --- |
| **ox\_lib** | Required |
| **OneSync** | Required (on by default on modern servers) |
| **Game build** | 2060 or newer. Set `sv_enforceGameBuild 2060` or higher. The casino chairs, card props and seated animations come from the Diamond Casino update. |
| **Framework** | Qbox, QBCore, ESX, or standalone. Cee-lo also supports ox\_core and ND\_Core. |
| **Inventory** | ox\_inventory, qb-inventory, ps-inventory, lj-inventory, qs-inventory, codem-inventory, tgiann-inventory, core\_inventory, origen\_inventory, wasabi\_inventory, or the ESX default inventory |
| **Target** | ox\_target, qb-target, or none (the built-in walk-up prompts) |

Everything is detected automatically. If a game picks the wrong framework, inventory or target, set it by hand in that game's config (`Config.Framework`, `Config.Inventory`, `Config.Target`) instead of `'auto'`.

{% hint style="warning" %}
**Money games on standalone servers** need a money item in ox\_inventory, tgiann-inventory or wasabi\_inventory. Without a framework or one of those, games run as free games only.
{% endhint %}
