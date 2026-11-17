# Moving from another phone

Switching from **lb-phone**, **npwd**, **Quasar** (qs-smartphone, Pro or V3) or **YSeries**? Your players keep their phone. Nothing in the old phone's tables is changed or deleted.

## How to move over

1. Back up your database.
2. Stop the old phone (remove its `ensure`) and start `hw_phone`.
3. In the server console run `phonemigrate lb-phone preview` (or `npwd`, `quasar`, `yseries`). It shows how many characters, contacts, texts, calls, photos and notes it found, and writes nothing.
4. Happy with it? Run `phonemigrate lb-phone run`. Staff can also run it in game; the results show in the server console.

## What's copied

| Copied | lb-phone | npwd | Quasar | YSeries |
| --- | --- | --- | --- | --- |
| Phone number | ✓ | ✓ | ✓ | ✓ |
| Contacts, texts, call history | ✓ | ✓ | ✓ | ✓ |
| Group chats | ✓ | ✓ | | |
| Photos, notes | ✓ | ✓ | ✓ | ✓ |
| Blocked numbers | ✓ | | | |
| Instapic → Instashot, Birdy → Bird Box (posts, likes, comments, follows) | ✓ | | | |

## Good to know

* **How players get their phone:** the first time a character uses a phone item that was never used before, it becomes their old phone: same number, everything on it. A phone item the old phone already numbered goes to that exact phone.
* **Players already using Huncho Phone** get their old contacts, texts, photos and notes on the phone they have (`mergeIntoExisting` in `config_migrate.lua`).
* **Old number taken** by someone on Huncho Phone? That character gets a new number, and their texts follow it.
* **Social passwords** can't be copied (they're encrypted). Players stay logged in, and "Forgot password?" mails them a code to set a new one.
* **Running it again** only adds what's new: parts that already ran are skipped (`run force` copies them again).
* **Quasar and YSeries** don't publish their database layout, so the phone looks for their tables and columns itself. The preview lists what it matched. If something says "not found", put the right names in `config_migrate.lua` (from the old phone's `.sql` file) and preview again.

{% hint style="info" %}
Moving over keeps players' data. For job and heist scripts that still send mail or texts through the old phone, see [Scripts made for other phones](other-phones.md).
{% endhint %}
