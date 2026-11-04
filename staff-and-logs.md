# Staff tools & Discord logs

Players with the `Config.Staff.ace` permission (default `command`, which is admins on Qbox and txAdmin) get staff tools right in the social apps:

* A shield button on every post and comment to remove it.
* A **Staff** box on profiles: ban the account from posting for 1 hour, 24 hours, 7 days or for good, in one app or all social apps, with a reason the player sees. Bans also cover new accounts the same character makes.
* **End this live** on any UPoppin stream.

## Discord logs

Paste a webhook link for each category in `config_server.lua`. Empty means off, and `default` is used for every category you leave empty.

```lua
ServerConfig.Logs = {
    enabled = true,
    default = '',
    webhooks = {
        social  = '',   -- posts and comments
        live    = '',   -- UPoppin lives
        money   = '',   -- transfers, gifts, subscriptions
        mail    = '',   -- mail between players
        staff   = '',   -- removals, bans, ended lives
        airdrop = '',   -- shared photos and videos
    },
}
```

Each line names the character, the player, their server id, citizen id and phone number.
