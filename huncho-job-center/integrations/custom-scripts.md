# Using your own scripts

Running an inventory, banking, key, fuel or notification script that isn't [supported](supported-scripts.md)? Hook it up in one file, with no other changes:

1. Open **`bridge/custom.lua`**. It's never encrypted.
2. Fill in the block for that part. Each block has a working example in its comments.
3. In `config/integrations.lua`, set that part to `'custom'`:

```lua
Inventory = 'custom',  Banking = 'custom',  Keys = 'custom',  Fuel = 'custom',  Notify = 'custom'
```

Only the blocks you switch to `'custom'` are used. Errors in your functions are caught and printed to the console, so a mistake can't break a shift.

## Inventory (server)

All four functions are needed.

```lua
Custom.Inventory = {
    metadata = true, -- can items hold metadata (fish weight, find value)? false = shops pay a flat price

    give = function(source, item, count, metadata)
        if not exports.my_inventory:CanCarryItem(source, item, count) then return false end
        return exports.my_inventory:AddItem(source, item, count, metadata) == true
    end,

    -- every stack of the item: { { slot = 3, count = 2, metadata = {...} }, ... }
    search = function(source, item)
        local out = {}
        for _, s in pairs(exports.my_inventory:GetItemsByName(source, item) or {}) do
            out[#out + 1] = { slot = s.slot, count = s.amount, metadata = s.info }
        end
        return out
    end,

    remove = function(source, item, count, metadata, slot)
        return exports.my_inventory:RemoveItem(source, item, count, slot) == true
    end,

    label = function(item)
        local d = exports.my_inventory:Items(item)
        return d and d.label or item
    end,
}
```

## Banking (server)

Money always comes from the framework's bank account. Use whichever option fits your banking script. `kind` is `'deposit'` (money in) or `'withdraw'` (money out), and `text` is the readable reason.

```lua
Custom.Banking = {
    -- A) write a history line after the framework paid
    statement = function(source, amount, text, kind)
        exports.my_banking:AddTransaction(source, amount, text, kind)
    end,

    -- B) your banking script logs every framework money change itself: change the reason it sees
    -- reason = function(text, kind) return text end,

    -- C) your banking script holds the money: move it there instead of the framework
    -- pay    = function(source, amount, text) return exports.my_banking:AddMoney(source, amount, text) end,
    -- charge = function(source, amount, text) return exports.my_banking:RemoveMoney(source, amount, text) end,
}
```

`charge` must return `false` when the player can't afford it.

## Vehicle keys (server)

```lua
Custom.Keys = {
    give = function(source, vehicle, plate, model) exports.my_keys:GiveKeys(source, plate) end,
    take = function(source, vehicle, plate, model) exports.my_keys:RemoveKeys(source, plate) end,
}
```

## Fuel (client)

GTA's fuel level and the `fuel` state bag are already set to full before this runs.

```lua
Custom.Fuel = {
    set = function(vehicle, level) exports.my_fuel:SetFuel(vehicle, level) end,
}
```

## Notifications (client)

```lua
Custom.Notify = {
    send = function(message, kind, duration) -- kind: 'inform' | 'success' | 'error' | 'warning'
        exports.my_notify:Notify('Job Center', message, kind, duration)
    end,
}
```

## Adding it properly

To make `auto` find your script, add it to the bridge file for that part instead. Each file has a list of adapters, one per script:

| Part | File | Add |
|---|---|---|
| Inventory | `bridge/server/inventory.lua` | An entry in `ADAPTERS` with `give`, `search`, `remove`, `label`, and its name in `INVENTORIES` |
| Banking | `bridge/server/banking.lua` | An entry in `ADAPTERS` with `statement`, `reason` or `pay` / `charge`, and its name in `BANKS` |
| Keys | `bridge/server/keys.lua` | A line in `GIVE` and `TAKE`, and its name in `system()` (`bridge/client/keys.lua` for client-only key scripts) |
| Fuel | `bridge/client/fuel.lua` | Its name in the list. Only add to `SETTERS` if it doesn't use `exports[name]:SetFuel(vehicle, level)` |
| Notifications | `bridge/client/notify.lua` | An entry in `SENDERS` |
| Target | `bridge/client/target.lua` | A branch in each function |
