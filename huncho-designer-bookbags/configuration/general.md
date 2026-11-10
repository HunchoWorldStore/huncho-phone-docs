# General settings

Everything is in `config.lua`, which stays editable after escrow.

| Setting | Default | What it does |
| --- | --- | --- |
| `Config.Framework` | `'auto'` | `'qbox'`, `'qbcore'`, `'esx'` or `'custom'` |
| `Config.Inventory` | `'auto'` | Inventory name, or `'custom'` |
| `Config.AdminAce` | `'hwbags.admin'` | Ace that can use the shop creator and `/bagfix` |
| `Config.AdminGroups` | `admin`, `god`, `superadmin` | Framework groups that also count as admin |
| `Config.Commands` | see below | Command names |
| `Config.OpenKey` | `'F7'` | Default key to open the worn bag |
| `Config.Capacity` | 20 slots, 25 kg / 8 slots, 10 kg | Starting storage per size. Change it later in the shop creator |
| `Config.MaxPrice` | `15000` | Highest price the shop creator accepts |
| `Config.DefaultPrices` | by tier | Starting prices for new shops |
| `Config.WearStyles` | back, front, one | Labels and straps for each wear style |
| `Config.WearAnimations` | `true` | Short gesture when putting a bag on or taking it off |
| `Config.Offsets` | tuned | Default bag and strap positions. Use `/bagfix` instead of editing by hand |
| `Config.DefaultPed` | `'s_f_y_shop_mid'` | Shop clerk model |
| `Config.QsStashPrefix` | `'Stash_'` | qs-inventory stash prefix |
| `Config.Text` | English | Every message players see |

## Commands

| Command | Default | Who |
| --- | --- | --- |
| Open worn bag | `/bag` or F7 | Everyone |
| Bag menu (open, style, take off) | `/bagstyle` | Everyone |
| Take off bag | `/takeoffbag` | Everyone |
| Shop creator | `/bagshops` | Admins |
| Prop positions | `/bagfix` or `/bagfix mini` | Admins |
