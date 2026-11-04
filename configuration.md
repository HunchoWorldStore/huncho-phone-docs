# Configuration

| File | What's in it |
| --- | --- |
| `config.lua` | Language, integrations, items, keybind, calls, camera and video, props, app settings, Mail, voicemail, staff, other-phone support |
| `config_server.lua` | Server only: Fivemanage key and Discord webhooks |
| `config_services.lua` | Police, EMS, mechanics and your own businesses: numbers, jobs, map locations, icons |
| `config_music.lua` | Your music library, speaker and radio settings |
| `locales/*.json` | The phone's text in each language |

All of these stay editable in the escrowed version, and so do both `bridge.lua` files if you want to connect a script that isn't listed.

## Most used settings

| Setting | Default | What it does |
| --- | --- | --- |
| `Config.Locale` | `'en'` | Language: `en`, `es`, `fr`, `de`, `pt-BR` or your own file |
| `Config.OpenKey` | `'F1'` | Opens and puts away the phone. Players can rebind it. `false` = item only |
| `Config.LockOnClose` | `true` | Ask for the passcode every time the phone comes out |
| `Config.WalkWhileOpen` | `true` | Walk and drive with the phone open |
| `Config.Integrations` | `'auto'` | Force a framework, inventory, banking, garage, housing or voice script |
| `Config.Apps.preinstalled` | 11 apps | What a new phone comes with. Everything else is downloaded from the App Store |
| `Config.Mail.domain` | `'hmail.com'` | Email addresses look like `name@hmail.com` |
| `Config.Voicemail.maxSeconds` | `30` | Longest recorded voicemail |
| `Config.Staff.ace` | `'command'` | Who gets the staff tools |
| `Config.Compat.enabled` | `true` | Pick up mail and notifications from scripts made for other phones |
| `Config.Weather.units` | `'F'` | `'F'` or `'C'` |
| `Config.Valet.fee` | `250` | What the Garage app's valet delivery costs |
