# Shop creator

Type `/bagshops` as an admin.

1. Stand where the shop should be and press **+ New shop at my location**.
2. **Location:** rename the shop or move it to where you stand.
3. **Stock & pricing:** turn each house on or off and set the bookbag and mini price. The storage fields change slots and weight for every bag of that size.
4. **Ped & blip:** turn the clerk and map blip on or off, and set the ped model, blip sprite, color and scale.
5. **Access:** choose cash, bank or both, and optionally limit the shop to certain jobs.
6. Press **Save shop**.

Shops save to the server's key-value storage, so they survive restarts and updates. Players buy from the clerk with ox\_target or qb-target, or with **E** if neither is running.
