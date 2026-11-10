# Locations and coordinates

**The coordinates are starting points, not verified in-game.** Work stops snap to the ground automatically, but some will need moving.

Stand where you want something and run **`/jccoords`** (admin). It copies `vec4(x, y, z, heading)` to your clipboard. Use the full vec4 for peds and vehicle spawns, and drop the heading for stops: `vec3(x, y, z)`.

Turn on `Config.Debug = true` to see target zones while you tune.

## Move them in game

Admins can move every location without touching a file: type **`/jclocations`**.

1. Pick the Job Center or a job, then the spot: depot supervisor, vehicle spawn, shops, warehouse points, tow drop-offs, boat rental, or a list (work stops, taxi pickups and drop-offs, paper-route houses, fishing and prospecting areas, warehouse shelves, recycling bins).
2. **Move it to where I am:** walk or drive to the new spot, face the way it should face and press **E** (Backspace cancels). A see-through ped or vehicle shows exactly where it will stand and which way it faces, with the old spot marked in red.
3. Lists can also **add a spot where you stand**, **delete** a spot, and **show them all on the map** with numbered markers and blips. **Teleport there** jumps to any spot.

Changes apply to everyone right away, with no restart. Peds, blips and markers move on the spot. Players on a shift finish the stop they're on, then get the new spots, and a paper route already in progress keeps its houses.

Changes are saved in the database (`hunchoworld_jobcenter_locations`), on top of the config files. Updating the script never wipes them, and **Reset to the config file** puts any spot back. To keep them in the files instead, use **Copy every change as Lua**: it copies a ready-to-paste block for each file. Paste each at the bottom of the file named above it, then reset those spots. Every move is logged to Discord (`admin` logs).
