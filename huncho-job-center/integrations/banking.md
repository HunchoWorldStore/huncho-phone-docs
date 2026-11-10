# Banking

Paychecks, vehicle deposits and refunds paid through the bank show in the player's banking history. Money always comes from the framework's bank account, so every banking script works for paying players. This page shows what each one records.

| Banking script | What the player sees |
|---|---|
| **hunchoworld_banking** | Pays and charges through its own exports, so every payment is logged with its reason, e.g. "Job center paycheck" |
| **Renewed-Banking** | A statement line from (or to) the employment office with the reason |
| **fd_banking** | Logs bank changes itself; payments show as from (or to) the employment office with the reason |
| **okokBanking** | A transfer from (or to) "Employment Office: Job center paycheck" |
| **qs-banking** | A bank statement for every payment |
| **ps-banking** | Logs every bank change itself, with its own generic description |
| **omes_banking** | A deposit or withdrawal with the reason |
| **esx_banking** (ESX) | A Deposit or Withdraw line with the amount and balance (it has no reason text) |

## Settings

```lua
Banking = 'auto', -- or a name from the table, 'custom' or 'none'
```

**qs-banking:** the statement uses the personal account name `personal_main`. If yours differs, change `QS_ACCOUNT` at the top of the qs-banking section in `bridge/server/banking.lua`.

## What each payment is called

The readable text for each payment is in the `TEXT` table at the top of `bridge/server/banking.lua`. Change it to rename "Job center paycheck", "Work vehicle deposit" and so on.
