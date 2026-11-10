# Troubleshooting

**The resource won't start.**
Don't rename the `hunchoworld_jobcenter` folder or delete its `.fxap` file. Make sure `ox_lib` and `oxmysql` start first, and that your Cfx account owns the asset.

**It picked the wrong script (or none).**
Check the server console at start: it prints what was picked for each part. Ensure the job center **after** those scripts in `server.cfg`, or name the one you want in `config/integrations.lua`.

**Players don't get items / "give failed" in the console.**
The item names must exist in your inventory. See [Adding the items](getting-started/items.md).

**A depot, stop or spawn is in the wrong place.**
Use `/jclocations` and move it where you stand. See [Locations and coordinates](configuration/locations.md).

**A uniform looks wrong or a ped is missing clothes.**
Clothing IDs differ between game builds and clothing packs. Dress how you want and save it with `/jcuniforms`. IDs that don't exist on your server are skipped.

**Work vehicles get deleted.**
Your cleanup script may ignore the `noDelete` state bag. Add whatever state it checks to `Config.ProtectVehicleStates`.

**Payments don't show in the banking app.**
Check which banking script was picked at start, and see [Banking](integrations/banking.md) for what each one records. ps-banking writes its own generic description.

**No keys for the work vehicle.**
Check the `Keys` line at start. Not supported? Use [your own scripts](integrations/custom-scripts.md#vehicle-keys-server).

**The Order Picker warehouse is empty.**
The shelves only look stocked if your server loads the interior's props. `bob74_ipl` does by default.

**Something else.**
Set `Config.Debug = true`, reproduce it, and send the F8 and server console output in a ticket on our [Discord](https://discord.gg/hP8VTtwgs5).
