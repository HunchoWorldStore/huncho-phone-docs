# Languages

Every game and the admin panel come in five languages:

| Code | Language |
| --- | --- |
| `en` | English |
| `es` | Spanish (Latin American) |
| `pt-br` | Portuguese (Brazil) |
| `fr` | French |
| `de` | German |

This covers notifications, prompts, menus, rules screens and results, plus the Oh Bih Please and Oh Bih Roulette cards, the Slumlords cards and squares, and the wheel slices.

## Set one language for the whole pack

In `games/admin/config.lua`:

```lua
Config.Language = 'es'
```

Restart the pack. Every game and the admin panel switch to Spanish.

## Set a language per game

Leave `Config.Language = nil` and set `Config.Locale` in each game's config instead:

| Game | File |
| --- | --- |
| Beer Pong | `games/beerpong/config/config.lua` |
| Card Hub | `games/cardhub/config.lua` |
| Cee-lo | `games/ceelo/config.lua` |
| Dominoes | `games/dominoes/config/main.lua` |
| Oh Bih Please | `games/ohbihplease/config.lua` |
| Oh Bih Roulette | `games/bihroulette/config.lua` |
| Slumlords | `games/slumlords/config/main.lua` |
| Tumbling Towers | `games/towers/config.lua` |

## Add your own language

1. In a game's `locales/` folder, copy `en.lua` to `<code>.lua` (for example `it.lua`).
2. Change `Locales['en']` to `Locales['it']` at the top.
3. Translate the text on the right of each `=`. Keep every `%s`, `%d`, `{name}` and `~INPUT_...~` exactly as it is.
4. Set `Config.Language = 'it'` (or `Config.Locale` in that game).

Anything you don't translate shows in English, so you can do it a bit at a time.

{% hint style="info" %}
**Cards and boards:** Oh Bih Please and Oh Bih Roulette keep one deck per language in `config_deck.lua` (`Decks['<code>']`). Slumlords translates its squares and cards with a `BoardLocales['<code>']` table at the bottom of each locale file. Copy the English versions to start.
{% endhint %}

Game names (Card Hub, Crazy 8s, Cee-lo, Oh Bih Please and so on) and Los Santos place names stay the same in every language.
