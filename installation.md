# Installation

1. **Add the resource.** Download it from [keymaster.fivem.net](https://keymaster.fivem.net) (Granted Assets) and put the `hw_phone` folder in your resources folder. Don't have it yet? Get it on the [Huncho World Store](https://hunchoworldstore.github.io/).
2. **Start it in `server.cfg`**, after your framework, inventory and voice script:

   ```
   ensure ox_lib
   ensure oxmysql
   # ... framework, inventory, voice, banking, garages, housing ...
   ensure hw_phone
   ```
3. **Add the items.** Pick the file for your inventory from `install/`:
   * `ox_inventory_items.lua` → `ox_inventory/data/items.lua`
   * `qb_items.lua` → `qb-core/shared/items.lua` (qb-, ps- and lj-inventory)
   * `qs_items.lua` → `qs-inventory/shared/items.lua`
   * `wasabi_inventory_items.lua` → `wasabi_inventory/data/items.lua`
   * ak47\_inventory, tgiann-inventory, core\_inventory: see `other_inventories.txt`

   Then copy `install/images/*.png` into your inventory's image folder.
4. **Database:** nothing to do. Every table is created on first start. If your database user can't create tables, run `sql/hw_phone.sql` once.
5. **Photos, video and voicemail (optional):** make a free key at [fivemanage.com](https://fivemanage.com) and paste it into `config_server.lua`:

   ```lua
   ServerConfig.FivemanageKey = 'your-key'
   ```

   That file only runs on the server, so players never see the key.
6. **Restart** and give yourself a phone (`hw_phone`, `hw_phone_flip`, `hw_phone_fold` ...). Use it from your inventory or press **F1**.

The console shows what the phone found when it starts:

```
[hw_phone] framework=qbx inventory=ox_inventory banking=renewed garage=qbx_garages housing=ps-housing voice=pma-voice camera=fivemanage
```

{% hint style="warning" %}
**Updating from 1.0.x?** Delete the old `hw_phone_props` folder and its `ensure` line if you still have them. If your Fivemanage key is in `config.lua`, move it to `config_server.lua` and make a new key: `config.lua` is sent to every player's game, so a key there could be read. The console reminds you until it's moved.
{% endhint %}
