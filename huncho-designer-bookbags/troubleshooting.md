# Troubleshooting

**Console says it could not detect a supported setup**
Start this resource after your framework and inventory in `server.cfg`, or set them in `config.lua`. For anything unsupported, use the [custom bridge](integrations/custom-scripts.md).

**Bag doesn't show on the player**
F8 will show `Bag model ... is not streamed`. Make sure `stream/` uploaded with all 528 `.ydr` files and `hw_bookbags.ytyp`, then reconnect.

**Items show without images**
Copy `html/images` into your inventory's image folder. See [Installation](getting-started/installation.md).

**Bag sits wrong on some characters**
Use [/bagfix](configuration/prop-positions.md) on that character type and save.

**qs-inventory: bags open empty or won't open**
Try `Config.QsServerOpen = true`. If your qs version stores stashes without a prefix, set `Config.QsStashPrefix = ''`.

**Shop clerk doesn't appear**
Check the ped model under **Ped & blip**. A wrong model falls back to `Config.DefaultPed` and prints a warning in F8. Players can still press **E** at the shop.
