# Commands

## Staff

| Command | Who | Does |
| --- | --- | --- |
| `/npcpolicetest [call]` | admin | Send a response to yourself (works while police are on duty) |
| `/npcpolicecases` | admin (`Config.StaffCases.aces`) | Every live response: who, what for, how long, what's happening. Mark on map, teleport to, or cancel one (no warrant, charges or jail) |
| `/npcpoliceremovecs [id]` | admin (`Config.CommunityService.removeCommand`) | End a player's [community service](../gameplay/community-service.md) |
| `/npcpoliceclearwarrant [id]` | admin | Clear a player's NPC warrant |
| `/npcpoliceclearrecord [id or citizen id] [yes]` | admin | Wipe everything the NPC police wrote about a character (`yes` also removes the NPC fingerprint). Officer-written records are kept |
| `/npcunjail [id or character id]` | admin + on-duty police | Release someone from the built-in jail early (`Config.Unjail`) |
| `/npcpolicedetect` | admin | Print detected integrations and unsupported scripts that are running |
| `/npcpoliceoutfit` | anyone | Copy your outfit as a uniform block |
| `/npcpolicecoords` | anyone | Print and copy your position as a `vec4` |

## Police

| Command | Does |
| --- | --- |
| `/npcevidence` | Open the evidence stash (ox\_inventory) |
| `/npcreturn [id]` | Give a player their confiscated items back |
| `/npccalls` | Recent calls, pick one to set GPS (built-in dispatch) |
| **Y** | GPS to the latest call (built-in dispatch) |
| `/npcduty` | Toggle duty (standalone with `requireDuty`) |

## Players

| Key / command | Does |
| --- | --- |
| **E** | Surrender (hands up) |
| **G** | Skip the ride to the station (after a while, `Config.Transport.skip`) |
| **B** | Bond & Counsel screen in the holding cell |
| **K** | Show / hide the arrest paperwork in the holding cell |
| `/911 [message]` | Call the police (built-in dispatch) |

{% hint style="info" %}
The keys are rebindable in the game's key bindings (FiveM section).
{% endhint %}
