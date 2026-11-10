# Requirements

## Required

* **ox_lib**
* **oxmysql**
* One framework: **Qbox** (`qbx_core`), **QBCore** (`qb-core`) or **ESX Legacy** (`es_extended`)

## Detected automatically

Everything else is optional. The job center finds what your server runs and uses it. See [Supported scripts](../integrations/supported-scripts.md) for the full list.

| Part | What happens without one |
|---|---|
| Target | Players walk up to peds and press **E** |
| Inventory | The framework's own item functions are used |
| Vehicle keys | No keys are handed out |
| Fuel | GTA's own fuel level and the `fuel` state bag are set to full |
| Banking | Money still goes through the framework; it just isn't written to a banking history |
| Notifications | ox_lib |

When the resource starts, the server console prints which script it picked for each part.
