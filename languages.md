# Languages

```lua
Config.Locale = 'es'   -- en, es, fr, de, pt-BR
```

Everything on the phone uses that language: screens, buttons, messages from the server and notifications. Players can also pick their own language in **Settings → Language**, which only changes their screen.

## Add a language

1. Copy `locales/en.json` to `locales/it.json` (any name).
2. Translate the text after each `:`. Keep `{1}`, `{2}` in place: they are names and numbers.
3. Set `Config.Locale = 'it'`. Lines you delete stay in English.

Players' own text (messages, posts, notes, mail) is never translated.
