# Phone models

Every model is its own item and its own phone. Drop it and whoever picks it up gets that number, its contacts and its passcode (Face Unlock only works for the owner).

| Model | Item | Interface | What it is | Standard edition |
| --- | --- | --- | --- | --- |
| Island | `hw_phone` | Glass | Classic slab phone | ✓ |
| Edge | `hw_phone_edge` | Flat | Slab with the Flat interface | ✓ |
| Flip | `hw_phone_flip` | Flat | Clamshell with a working cover screen | ✓ |
| Fold | `hw_phone_fold` | Flat | Opens into a tablet with a taskbar | ✓ |
| Duo | `hw_phone_duo` | Glass | Two screens joined by a hinge | ✓ |
| Tri | `hw_phone_tri` | Flat | Three screens, an app on each | |
| Bold | `hw_phone_bold` | Flat | Real QWERTY keyboard and trackpad | |
| Spin | `hw_phone_spin` | Flat | Screen swivels to a keyboard | |
| Snap | `hw_phone_snap` | Glass | Metal flip with a glowing keypad | |
| Snap Max | `hw_phone_snapmax` | Flat | Modern flip, full outside screen | |

The keys on the Bold, Spin and Snap really work: unlock, dial, call and type with them. Each model has its own 3D prop and hand animations. Lids swing, foldables open like a book and the Spin swivels.

## Hand positions

Phones come with their positions in the hand already set (`prop_defaults.json`). To change one, admins use `/phoneprop [model]` in game. Phones that open and close have a separate open and closed position (press **E** to switch). Positions are saved in the database for everyone, and `/phoneprop export` writes them all to `prop_defaults_export.json`.
