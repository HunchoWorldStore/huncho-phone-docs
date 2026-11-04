# Exports

## Client

```lua
exports.hw_phone:openPhone()
exports.hw_phone:closePhone()
exports.hw_phone:isOpen()                              -- true / false
exports.hw_phone:peek(title, message, app)             -- pop-up notification
exports.hw_phone:SendMail({ sender = 'Boss', subject = 'Job', message = 'Meet at the docks' })
exports.hw_phone:SetDisabled(true)                     -- the phone can't be opened (cutscenes, cuffs)
exports.hw_phone:IsDisabled()
```

## Server

```lua
exports.hw_phone:GetPhoneNumber(source)
exports.hw_phone:GetSourceByNumber(number)
exports.hw_phone:SendNotification(source, title, message, app)
exports.hw_phone:SendText(from, toNumber, message)     -- from a number, or a name (goes to Mail)
exports.hw_phone:GetEmailAddress(number)
exports.hw_phone:SendMailToAll(mail)
exports.hw_phone:IsBlocked(number, byNumber)
exports.hw_phone:Log('social', 'Title', { { 'Field', 'Value' } })
```

## Mail with buttons

The target can be a player's server id, a phone number, an email address, or `{ citizen = 'ABC123' }`. A player without a phone gets the mail on the next phone they use.

```lua
exports.hw_phone:SendMail(source, {
    sender  = 'Fleeca Bank',
    subject = 'Loan approved',
    message = 'Tap Accept to get your money today.',
    actions = {
        { label = 'Accept', event = 'bank:acceptLoan', server = true, data = { id = 5 } },
    },
})

-- server = true: the player's client calls TriggerServerEvent, so `source` is the player
RegisterNetEvent('bank:acceptLoan', function(data, mailId)
    local src = source
    -- ...
end)
```

A button is used once. Add `keep = true` to an action to leave it on the mail. Up to three buttons per mail.
