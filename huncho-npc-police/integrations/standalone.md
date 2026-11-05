# Standalone servers

With no Qbox, QBCore or ESX running, the resource switches to standalone mode by itself (`Config.Standalone`).

| | Standalone |
| --- | --- |
| Identity | The player's Rockstar license and FiveM name (records, warrants and paperwork all work) |
| Police | Players with the ace `huncho.police` |
| Fines and bond | The ox\_inventory `money` item if ox\_inventory runs, otherwise skipped (`freeWithoutMoney`) |
| Search / confiscation | ox\_inventory if it runs |
| Weapon license | Optional aces in `licenseAces` |

```cfg
add_ace group.police huncho.police allow
add_principal identifier.license:YOUR_LICENSE group.police
```

Set `requireDuty = true` to make police toggle duty with `/npcduty` first.

Everything else (pursuits, arrests, booking, the built-in jail, the built-in dispatch) works the same.
