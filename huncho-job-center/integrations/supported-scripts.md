# Supported scripts

Everything is detected automatically. To force one, set it by name in `config/integrations.lua`. To turn a part off, set it to `'none'`. Not listed? See [Using your own scripts](custom-scripts.md).

| Part | Supported | Setting |
|---|---|---|
| **Framework** | Qbox, QBCore, ESX Legacy | `Framework` |
| **Target** | ox_target, qb-target, interact, or none (walk up and press E) | `Target` |
| **Inventory** | ox_inventory, qs-inventory, tgiann-inventory, wasabi_inventory, ak47_inventory, qb-inventory, or the framework's own items (ps-inventory, lj-inventory, codem-inventory and others on QBCore; the default ESX inventory) | `Inventory` |
| **Vehicle keys** | qs-vehiclekeys, qbx_vehiclekeys, qb-vehiclekeys, wasabi_carlock, MrNewbVehicleKeys, Renewed-Vehiclekeys, vehicles_keys, cd_garage, okokGarage, t1ger_keys | `Keys` |
| **Fuel** | ox_fuel, LegacyFuel, cdn-fuel, ps-fuel, lj-fuel, qs-fuelstations, okokGasStation, Renewed-Fuel, ti_fuel, x-fuel, BigDaddy-Fuel, rcore_fuel, myFuel | `Fuel` |
| **Banking** | hunchoworld_banking, Renewed-Banking, fd_banking, okokBanking, qs-banking, ps-banking, omes_banking, esx_banking (ESX) | `Banking` |
| **Clothing** | Any clothing script for uniforms; rcore_clothing also reloads the saved outfit after a shift | `Clothing` |
| **Notifications** | ox_lib, QBCore, ESX, okokNotify, mythic_notify, wasabi_notify, brutal_notify, pNotify | `Notify` |
| **Admin access** | ace permissions, QBCore permissions or ESX groups | `AdminAces`, `AdminGroups` |

## config/integrations.lua

```lua
Integrations = {
    Framework = 'auto',   -- 'qbx' | 'qb' | 'esx'
    Target    = 'auto',
    Inventory = 'auto',   -- 'qb-inventory' = qb-inventory 2.0+ exports (QBCore), 'framework', 'custom'
    Keys      = 'auto',
    Fuel      = 'auto',
    Banking   = 'auto',
    Clothing  = 'auto',
    Notify    = 'ox_lib',

    AdminAces   = { 'group.admin', 'command' },
    AdminGroups = { 'admin', 'superadmin', 'god' },

    Accounts = { cash = 'cash', bank = 'bank' },  -- rename if your server's accounts differ
    Announce = true,                               -- print what was picked at start
}
```

## Good to know

* **Start order matters.** Ensure the job center after the scripts it should detect.
* **Two of the same kind running?** `auto` picks the first one it finds. Name the one you want.
* **qb-inventory on auto** uses the framework's own item functions, which work with every qb-inventory version. Pick `'qb-inventory'` to use the 2.0+ exports directly.
