# Scripts made for other phones

Many job, heist and bank scripts send mail, texts or notifications through a specific phone. When that phone isn't installed, Huncho Phone picks them up, so those scripts work with no changes.

| Made for | What works |
| --- | --- |
| qb-phone | Mail events `sendNewMail`, `sendNewMailToOffline`, `sendNewEventMail` with their button; `CustomNotification` |
| qs-smartphone | The same mail events and notifications as qb-phone |
| qs-smartphone-pro | Mail events, `sendNewMail`, `GetPhoneNumberFromIdentifier`, `getMetaFromSource`, `sendNewMessageFromApp` |
| lb-phone | `SendMail` with action buttons (or to `"all"`), `GetEmailAddress`, `SendNotification`, `NotifyEveryone`, `SendMessage`, `GetEquippedPhoneNumber`, `GetSourceFromNumber`, `HasPhoneItem`, `AddContact`; client `SendNotification`, `IsOpen`, `ToggleOpen`, `ToggleDisabled` |
| npwd | `emitMessage`; client `createNotification`, `createSystemNotification`, `isPhoneVisible`, `setPhoneVisible`, `setPhoneDisabled` |

If a script asks which phone you use in its own config, choose **qb-phone** or **lb-phone**. Texts sent from a name instead of a number (for example "Dispatch") arrive in Mail. Turn any phone off in `Config.Compat.phones`.
