# Advanced jobs

These seven have their own mechanics. Each one's settings are in its file in `config/jobs/`.

**Dog Walker** (`dogwalker.lua`): you keep your own clothes. Owners wait at their doors with 1-4 dogs (more unlock as you complete walks). Each leash is tied to your hand and the dog's neck, hangs with a little slack, and every nearby player sees it. Dogs have breeds and personalities, a happiness meter, bathroom breaks you bag up, and they get bored if you stand around. Pet, treat, sit and play fetch from the dog menu (**G**). Off the leash means a bigger tip, but they can bolt. Lose one and the walk pays nothing. The server picks the dogs and walk time and measures how far you actually walked.

**Fisherman** (`fishing.lua`): you keep your own clothes. Face any water and press **E** to cast (time the power meter). You stay facing the water with the rod in hand until the fish is landed, and **Backspace** reels your line back in while you wait (rebindable, so it doesn't clash with hands up on X). Wait out the nibbles (striking early spooks the fish), strike on the bite, then fight it: hold **E** to reel and ease off when tension spikes, without giving slack. 26 species across fresh, salt and deep water, with bites depending on bait, time of day and weather. Rods upgrade with total catches, and each fish has a real weight. Personal records, plus a dinghy rental for deep-sea grounds. Change bait with **G**, and sell at the Fish Market.

**Prospector** (`prospecting.lua`): inside a prospecting area (shown on the map during the shift) the detector comes out. Beeps speed up and the signal meter climbs as you close in. Dig with **E** at full signal. Each area has its own loot, every find has a condition and appraised value, detectors upgrade with total finds, and finds are sold to the Appraiser.

**Paperboy** (`newspaper.lua`): you keep your own clothes. Each route is a random area (Mirror Park, Mirror Park North, Rockford Hills, Vespucci) and you get exactly one throwable newspaper per house. Every house shows on the map with a pink marker; equip a paper and throw it in, any order. Miss and run out and the route is over, no second chances. Ride back to the depot for a new route, or clock out to get paid. The server checks each delivery (distance, that a paper was really thrown, and that you're on the job bike, otherwise it pays $1). Papers can't be put in gloveboxes, trunks or dropped.

**Mover** (`moving.lua`): carry everything to the truck and load it; it sits in the cargo area where everyone can see it. Heavy furniture needs the hand truck from the back of the truck. Drops and crashes damage items (fragile ones more), which lowers the pay.

**Order Picker** (`orderpicker.lua`): uses the large CEO warehouse interior. The shelves only look stocked if your server loads them (`bob74_ipl` does by default). Shelf, bench and dock coordinates are estimates: walk it once and fix them with `/jccoords`.

**Tow Truck Operator** (`tow.lua`): calls come in as breakdowns (the owner waits by the car with the hazards on and tips you), illegally parked cars or accidents (a smashed-up wreck). Back the flatbed up, get out and winch the car on, then haul it to the repair shop or the impound lot and unload it. Pay = base for the call type + a distance bonus - any damage done while it's on your truck.

Fishing and prospecting pay by selling items. The other five pay into the paycheck like the rest of the jobs.

## Recycling Worker

Players start at the depot manager outside on Elysian Island and are taken into the recycling warehouse. They grab a bag off the trash pile and get told which color bin it goes in (yellow, blue or green); a wrong bin is rejected. Each correct sort pays `payPerTask` and has a 50% chance of a bonus item (`metal_scraps`, `plastic`, and `blueprint_glock` from blue bins). They clock out with the floor supervisor inside and are taken back outside.

The server picks each bag's color, so the reward table can't be chosen by the player. Items are given through your inventory (see `config/integrations.lua`) and the item names must exist in it. Everything is in `config/jobs/recycling.lua`.

## Bus and tour passengers

The bus and tour bus carry real NPC riders that every player can see. At each stop a few walk up from the curb and board while you wait, and some get off and walk away. The tour starts with a group already on board. Set it per job with `passengers = { start, board, alight, max, models }` in the job's file, or remove the block to turn it off.
