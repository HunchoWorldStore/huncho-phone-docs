# Discord logs

Logs are set in `config/server.lua`. That file only loads on the server, so players never receive your webhook URL.

1. In Discord: **Edit Channel → Integrations → Webhooks → New Webhook**, then copy its URL.
2. Paste it into `webhook` and set `enabled = true`.

```lua
ServerConfig.Logs = {
    enabled  = true,
    webhook  = 'https://discord.com/api/webhooks/...',
    username = 'Job Center',
    avatar   = '',

    bigPaycheck = 4000,   -- clock-outs at or above this are highlighted
    bigSale     = 4000,   -- shop sales at or above this are highlighted
    mention     = '',     -- pinged on flags, e.g. '<@&123456789012345678>'

    events = {
        clockIn  = true,  -- shift started
        clockOut = true,  -- pay, tasks, time, deposit, bonuses
        crew     = true,  -- joined / left a crew
        sale     = true,  -- sold catches or finds
        flag     = true,  -- failed server checks
        admin    = true,  -- admin actions, job of the day, new records, location and uniform changes
    },
}
```

**Flags** are failed server checks: a task handed in away from the job site, a fish landed faster than possible, a paper "delivered" without one being thrown, someone leaving mid-shift. They can ping a staff role with `mention`.

Messages are batched so Discord's rate limit isn't hit.
