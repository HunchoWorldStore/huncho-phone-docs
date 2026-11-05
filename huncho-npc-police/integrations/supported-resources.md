# Supported resources

Everything is detected on its own. **Verified** = written against that resource's code or docs. **Untested** = built from public docs but not yet run on a live server; the console says so when one is picked. Please report anything that doesn't work.

| Category | Verified | Untested |
| --- | --- | --- |
| Framework | qbx\_core, qb-core, es\_extended, **standalone** | |
| Dispatch (alerts heard) | ps-dispatch, cd\_dispatch, core\_dispatch, qb-policejob alerts, ak47\_drugmanagerv2 / v3, esx\_outlawalert, esx\_policejob 911, linden\_outlawalert 911, origen\_police, redutzu-mdt, aty\_dispatch, bub-mdt, SonoranCAD 911, rcore\_dispatch, **built-in dispatch** | qs-dispatch, linden\_outlawalert / wf-alerts |
| Inventory | ox\_inventory, qb-inventory, ps-inventory, lj-inventory, ESX default | qs-inventory, codem-inventory, core\_inventory, origen\_inventory |
| Prison | rcore\_prison, xt-prison, qbx\_prison, qb-prison, esx\_jail, tk\_jail, esx-qalle-jail, esx\_communityservice, bc\_communityservice, **built-in jail** | pickle\_prisons\*, p\_policejob, origen\_police |
| Community service | Justice System, sleezy\_coms, randol\_service (with [exports](../gameplay/community-service.md)), bc\_communityservice, esx\_communityservice, mh-communityservice, rcore\_prison COMS, **built-in** | |
| Garage / impound | jg-advancedgarages, ak47\_garage, cd\_garage, vms\_garagesv2, esx\_garage, qbx\_garages, qb-garages, ESX owned\_vehicles | codem-garage, ak47\_qb\_garage, renzu\_garage |
| Garage (car removed only\*\*) | okokGarage, loaf\_garage, rcore\_garage, qs-advancedgarages, lunar\_garage, mGarage | |
| Banking (society deposit) | Renewed-Banking, qb-management, esx\_addonaccount | fd\_banking, wasabi\_banking, qs-banking, okokBanking, tgg-banking, qb-banking |
| Billing (fines) | direct from bank / cash (default), tgg-billing | okokBilling, esx\_billing, RxBilling, wasabi\_billing, qb-phone invoices |
| Insurance / registration | m-Insurance, owned vehicles table | ods\_vehicleinsurance |
| MDT | wasabi\_mdt, [Justice System](justice-system.md) | |
| Licenses | bcs\_licensemanager, esx\_license, QB / Qbox metadata, ID-card items (um-idcard, bl\_idcard, qs-licenses, jg-licenses, okokLicenses, ps-idcard...), license item, ace (standalone) | |
| Ambulance / death | qbx\_medical, ak47\_ambulancejob, osp\_ambulance, tk\_ambulancejob, brutal\_ambulancejob, p\_ambulancejob, randol\_medical, sky\_ambulancejob, qs-medical-creator, wasabi\_ambulance, qb-ambulancejob, esx\_ambulancejob, generic | ars\_ambulancejob, plt\_ambulance\_job, origen\_ambulance |
| Screenshot (mugshot) | screenshot-basic, "screenshot" fork | |
| Drug selling | [hunchoworld\_advancedtrapping, sage\_trapping](trapping.md) | |

\* The free pickle\_prisons has no export to call. When jailing through any prison script fails, the built-in jail is used.

\*\* These garages have no public impound function, so the car is taken off the street and nothing is written to the garage. Connect their impound in [Other scripts](other-scripts.md) if you want it there.

## Forcing a script

To use a specific adapter instead of auto-detection, set it in `Config.Bridge`:

```lua
Config.Bridge.prison = 'builtin'
```

{% hint style="info" %}
**Script not listed?** Most scripts can be connected from the config without Lua: [Other scripts (no code)](other-scripts.md). `/npcpolicedetect` lists running scripts that look unsupported.
{% endhint %}
