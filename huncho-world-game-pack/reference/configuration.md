# Config Files

Each game is configured in its own folder under `games/`. Nothing is shared, so changing one game never affects another. Every file listed here stays readable after escrow.

| Game | Main config | Text | Other |
| --- | --- | --- | --- |
| Admin panel | `games/admin/config.lua` | `games/admin/locales/` | |
| Beer Pong | `games/beerpong/config/config.lua`, `config/advanced.lua` | `locales/` | `config/server.lua` (webhook) |
| Card Hub | `games/cardhub/config.lua` | `locales/` | `config_server.lua` (webhook), `editable/` |
| Cee-lo | `games/ceelo/config.lua` | `locales/` | `custom/server.lua` (webhook, dispatch) |
| Dominoes | `games/dominoes/config/main.lua`, `tables.lua`, `modes.lua`, `advanced.lua` | `locales/` | |
| Oh Bih Please | `games/ohbihplease/config.lua` | `locales/` | `config_deck.lua` (cards), `config_server.lua` (webhook) |
| Oh Bih Roulette | `games/bihroulette/config.lua` | `locales/` | `config_deck.lua` (cards), `config_server.lua` (webhook) |
| Slumlords | `games/slumlords/config/main.lua`, `config/advanced.lua` | `locales/` | `shared/board.lua` (squares and cards), `config/server.lua` (webhook) |
| Tumbling Towers | `games/towers/config.lua` | `locales/` | |

## Settings most servers change

| What | Where |
| --- | --- |
| Item, command or both | The [admin panel](../admin-panel.md), or each game's method setting (see [Commands](commands.md)) |
| Stake limits | The admin panel, or each game's money settings |
| Language | `Config.Language` in `games/admin/config.lua` (see [Languages](../languages.md)) |
| Money account (cash / bank) | Each game's money section |
| Bots on money tables | Each game's `Config.Bots` (off by default: bots can't pay, so a player could win money that never existed) |
| Framework / inventory / target | `'auto'` in each game; set by hand if it detects the wrong one |
| Discord logs | Each game's server config or webhook file |

{% hint style="warning" %}
Back up your changed files before [updating](../getting-started/updating.md). Admin panel settings don't need a backup: they're saved on the server.
{% endhint %}
