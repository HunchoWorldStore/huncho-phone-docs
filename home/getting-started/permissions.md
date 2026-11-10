---
description: Give staff access to admin commands and panels with aces.
---

# Permissions

Admin tools in our scripts are locked behind **aces**. You set them in `server.cfg`.

## The basics

```cfg
# Put a player in the admin group (their identifier from txAdmin or the server console)
add_principal identifier.fivem:1234567 group.admin

# Give a group one permission
add_ace group.admin command.gamepack allow
```

Restart the script (or the server) after changing aces. Players may need to reconnect.

{% hint style="info" %}
On **Qbox** and **QBCore**, players with admin permissions are usually already in `group.admin`, so most admin tools work out of the box.
{% endhint %}

## Per script

| Script | Where to look |
| --- | --- |
| Huncho Designer Bookbags | `Config.AdminAce` (default `hwbags.admin`) in [General settings](https://huncho-world-store.gitbook.io/huncho-world-store-docs/huncho-designer-bookbags/configuration/general) |
| Huncho Job Center | [Commands](https://huncho-world-store.gitbook.io/huncho-world-store-docs/huncho-job-center/admin/commands) |
| Huncho NPC Police | [Commands](https://huncho-world-store.gitbook.io/huncho-world-store-docs/huncho-npc-police/reference/commands) |
| Huncho Phone | `Config.Staff.ace` in [Staff tools & Discord logs](https://huncho-world-store.gitbook.io/huncho-world-store-docs/huncho-phone/staff-and-logs) |
| Huncho World Game Pack | [Permissions](https://huncho-world-store.gitbook.io/huncho-world-store-docs/huncho-world-game-pack/reference/permissions) |
