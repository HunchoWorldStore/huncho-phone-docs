# Requirements

## Needed

| Resource | Why |
| --- | --- |
| [ox\_lib](https://github.com/overextended/ox_lib) | Menus, notifications, callbacks |
| [oxmysql](https://github.com/overextended/oxmysql) | Records, warrants and the built-in jail |
| OneSync | On by default on current servers |

## Optional

Everything else is optional and **detected on its own**: framework (Qbox, QBCore, ESX or none), inventory, dispatch, prison, garage, banking, billing, MDT, licenses, insurance, ambulance and screenshot scripts. The full list is on [Supported resources](../integrations/supported-resources.md).

| Missing | What happens |
| --- | --- |
| A framework | [Standalone mode](../integrations/standalone.md) |
| A dispatch script | The [built-in dispatch](../setup/built-in-dispatch.md) turns on |
| A prison script | The built-in jail at Bolingbroke ([Jail, warrants & release](../gameplay/jail-and-warrants.md)) |
| An MDT | Records and warrants are kept in the resource's own tables |
| screenshot-basic | Bookings are posted without a mugshot photo |
