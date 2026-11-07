# Custom apps

Other resources can add their own app. It's listed in the App Store, players download it per phone, and it opens your page inside the phone.

```lua
exports.hw_phone:AddApp({
    id    = 'my_app',                                     -- letters, numbers, _ or -
    label = 'My App',
    ui    = 'my_resource/html/phone.html',                -- page shown in the phone
    icon  = 'https://cfx-nui-my_resource/html/icon.png',  -- optional
    description = 'What the app does.',                   -- App Store text
    category    = 'Business',
    size        = 25,                                     -- MB: bigger apps download a bit longer
    preinstalled = false,                                 -- true = on every phone (job apps)
    background   = false,                                 -- true = keeps running outside the app (music)
})
exports.hw_phone:RemoveApp('my_app')
exports.hw_phone:HasApp('my_app')
exports.hw_phone:SendAppMessage('my_app', { action = 'state', data = {} })
exports.hw_phone:peek('Title', 'Message', 'my_app')
```

The page talks to its own resource with `fetch('https://my_resource/callbackName')`. Its URL gets `?host=hunchphone&ui=ios|oneui&light=0|1` so it can match the phone. To let Escape and the phone key close the phone from your page: `window.parent.postMessage({ hunchphoneKey: e.key }, '*')`.

## Background apps

With `background = true` the page loads once and keeps running while the player uses other apps or puts the phone away, so music keeps playing. Opening the app again shows the same page. It stops when the player no longer has a phone item or uses a different phone. `SendAppMessage` reaches it the whole time, and its URL also gets `&background=1`. Needs 1.1.2 or newer.
