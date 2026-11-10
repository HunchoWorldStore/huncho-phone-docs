# Adding a job

1. Copy any file in `config/jobs/` and rename it.
2. Inside, change `Jobs.<name>` and `Uniforms.<name>` to the new name.
3. Restart. New files are picked up automatically.

Most new jobs need no code. Steps are built from these types:

| Step | What happens |
|---|---|
| `action` | Play an animation at the stop. Can place a prop there (a grill, a mailbox) |
| `pickup` | Pick something up from the vehicle or the ground (carry animation and prop) |
| `dropoff` | Put it in the vehicle or at the stop. Can leave a prop behind, like cones |
| `serve` | An NPC customer walks up and you hand them something |
| `handoff` | A customer steps out at the door and takes what you're carrying inside |
| `valet` | A guest car pulls up, you take the keys and park it at `drop` |

A stop can have a `drop` point anywhere on the map (the courier's customer is across town). Steps with `at = 'drop'` route the player there first. Any step can have `count = n` or `{ min, max }`, and `rounds` repeats the whole list.

## Example

```lua
steps = {
    { type = 'pickup', from = 'vehicle', carry = 'box', label = 'Grab materials', icon = 'fa-solid fa-box' },
    { type = 'dropoff', to = 'stop', anim = 'putdown', duration = 1200, label = 'Drop materials' },
    { type = 'action', anim = 'hammer', duration = 10000, label = 'Hammer framing', icon = 'fa-solid fa-hammer' },
},
```
