# Custom adapters

Every category can take your own adapter in Lua.

{% stepper %}
{% step %}
### Open the template

`bridge/server/_custom_template.lua`, or `bridge/client/_custom_template.lua` for death, screenshot and prison status.
{% endstep %}

{% step %}
### Fill it in

Uncomment the block for the category and fill in the functions. Each function's inputs and outputs are documented in the template and at the top of each bridge file.
{% endstep %}

{% step %}
### Switch to it

Set that category to `'custom'` in `Config.Bridge`, for example `Config.Bridge.billing = 'custom'`.
{% endstep %}
{% endstepper %}

The `bridge/` folder, `config.lua`, `locales/` and `server/config_server.lua` stay editable on the escrowed version.

## Custom framework example

```lua
Bridge.register('framework', 'custom', {
    getIdentifier = function(src) return MyCore.GetCharId(src) end,
    getCharInfo = function(src)
        local c = MyCore.GetChar(src)
        return { firstname = c.first, lastname = c.last, dob = c.dob, gender = c.male and 'male' or 'female' }
    end,
    isPolice = function(src) return MyCore.GetJob(src) == 'police' and MyCore.OnDuty(src) end,
    policeCount = function() return MyCore.CountOnDuty('police') end,
    getMoney = function(src, account) return MyCore.GetMoney(src, account) end,
    removeMoney = function(src, account, amount, reason) return MyCore.RemoveMoney(src, account, amount) end,
    getSourceFromIdentifier = function(id) return MyCore.GetSourceByChar(id) end,
    onPlayerLoaded = function(cb) AddEventHandler('mycore:charLoaded', cb) end,
})
```

**Custom dispatch:** call the handler from that dispatch's event (example in the server template), or use the `Alert` [export](../reference/exports.md).
