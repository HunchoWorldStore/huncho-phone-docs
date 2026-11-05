# Drug selling (trapping)

**hunchoworld\_advancedtrapping** and **sage\_trapping** are found automatically.

* Every drug in the trapping script's live list (including ones made in its drug creator) is an illegal item and counts as drug-sale evidence. You don't need to add them to `Config.Search.items` or `Config.Evidence.items.drug_sale`.
* Getting cuffed ends a trapping session.
* Drugs taken off a player or out of a car show in the trapping economy dashboard (`/drugstats` → Police).
* Those drugs are never handed back (`Config.Search.returnItems.keepTrappingDrugs`).

Drug sales from any other script are spotted by the [built-in detection](../setup/calls-and-alerts.md).
