# Changelog

## 1.4.1

* **Food Truck Vendor ingredients.** Every hotspot now starts at the truck's storage: grab the ingredients from the back of the taco truck, set them down at the hotspot, then fire up the grill and cook before serving customers. It used to go straight from the grill to serving, with no ingredients.

## 1.4.0

* Inventory support for **tgiann-inventory**, **wasabi_inventory**, **ak47_inventory** and **qb-inventory** through its own exports (`Inventory = 'qb-inventory'`, QBCore with qb-inventory 2.0+). Every inventory now has its own adapter in `bridge/server/inventory.lua`.
* Banking support for **hunchoworld_banking**, **fd_banking**, **okokBanking**, **qs-banking** and **ps-banking**:
  * hunchoworld_banking pays and charges through its own exports, so every payment is logged with its reason.
  * fd_banking shows payments as from / to the employment office with the reason.
  * okokBanking shows a transfer from / to the employment office.
  * qs-banking gets a bank statement for every payment.
  * ps-banking already logs every bank change by itself; it's now detected and shown at start.
* New `bridge/custom.lua`: hook up your own inventory, banking, key, fuel or notification script by filling in one block and setting that part to `'custom'` in `config/integrations.lua`.

## 1.3.0

* Bank statement support for **omes_banking** (QBCore, Qbox and ESX) and **esx_banking** (ESX), next to Renewed-Banking. Paychecks, vehicle deposits and refunds paid through the bank show in the player's transaction history. Detected automatically, or set `Banking` in `config/integrations.lua`.

## 1.2.0

* In-game uniform editor (`/jcuniforms`): save what you're wearing as a job's male or female uniform, preview it, turn it on or off, reset it or copy it as Lua. Saved in the database and loaded again after every restart.
* Location editor: the server now waits for the saved locations to load from the database before sending them to players or accepting changes, and only says "Saved" once the database has the change, so in-game moves always survive a restart.
* A job with only a male or only a female uniform no longer shows a "freemode only" warning to the other gender.
* New **Commands** section in this README listing every command.

## 1.1.0

* In-game location editor (`/jclocations`): move every depot, vehicle spawn, shop, stop, route house, area, shelf and bin by walking there and pressing E, with live previews. Changes apply to everyone without a restart, are saved in the database, and can be reset or copied out as Lua.

## 1.0.2

* Renewed-Fuel now filled through its `SetFuel` export (per its docs).
* Renewed-Banking: paychecks, vehicle deposits and refunds show on the player's bank statement.
* rcore_clothing: the player's saved outfit is reloaded after the uniform comes off.
* Renewed-Vehiclekeys and rcore_fuel checked against their docs.

## 1.0.1

* Key scripts checked against their docs: okokGarage now takes keys back at clock-out, cd_garage keys are sent straight from the server, t1ger_keys shows the vehicle's name in its key menu.

## 1.0.0

* First release of hunchoworld_jobcenter: 30 jobs, crews, job of the day, work streaks, leaderboards, Discord logs, staff tools and the pay overview.
* Runs on Qbox, QBCore and ESX. Target, inventory, vehicle keys, fuel and notifications are detected automatically (`config/integrations.lua`, code in `bridge/`).
* Install files for ox_inventory, QBCore-style inventories / qs-inventory and the default ESX inventory.
