# Uniforms

Every job can put players in a uniform at clock-in. Their own clothes come back at clock-out. Uniforms work with any clothing script, and rcore_clothing also reloads the player's saved outfit afterwards.

## Set them in game

Admins can set every job's uniform without touching a file: type **`/jcuniforms`** and pick a job.

- **Use what I'm wearing:** dress your character in your clothing menu, then save it as that job's male or female uniform (whichever character you're on). Clothes, hat, glasses, ears, watch and bracelet are all saved.
- **Preview it on me:** try the uniform on. **Take off the preview** gives you your own clothes back.
- **Turn the uniform off / on:** off means players keep their own clothes on that job.
- **Reset to the config file** and **Copy as Lua** work the same as for locations.

Players get the new uniform from their next clock-in. Uniforms are saved in the database (`hunchoworld_jobcenter_uniforms`) and loaded again on every restart, on top of the config files. Every change is logged to Discord (`admin` logs).

## Set them in the files

Clothing IDs shift between game builds and clothing packs, so treat the included ones as a starting point. Dress your character in the clothing menu the way you want the uniform, then run **`/jcoutfit`** (admin). It copies a paste-ready line for `uniforms.lua`. IDs that don't exist on your server are skipped, so a bad ID never makes a ped invisible. Set `uniform = false` on a job to skip it. Or skip the files and use **`/jcuniforms`** in game.

Uniforms set in game sit on top of the files, so you can use both.
