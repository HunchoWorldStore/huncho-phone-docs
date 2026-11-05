# Config overview

Everything is in `config.lua` (open, also on the escrowed version). The Discord webhook lives in `server/config_server.lua`, which only runs on the server.

| Area | Settings |
| --- | --- |
| General | `Config.Locale`, `Config.Debug`, `Config.VersionCheck`, `Config.Bridge` (force an adapter) |
| How tough | `Config.Difficulty`, `Config.DifficultyTweaks`, `Config.DifficultyPresets` ([Difficulty](../setup/difficulty.md)) |
| When they work | `Config.OnlyWhenNoPolice`, `Config.MaxPoliceOnDuty`, `Config.PoliceJobs`, `Config.CountAsPolice`, `Config.Handoff` ([Working with real police](../setup/real-police.md)) |
| Calls | `Config.Calls`, `Config.DispatchKeywords`, `Config.IgnoreKeywords`, `Config.DefaultCall` ([Calls & alerts](../setup/calls-and-alerts.md)) |
| Detection | `Config.Gunshots`, `Config.Detection`, `Config.Victims`, `Config.Accomplices` |
| Dispatch | `Config.Dispatch` ([Built-in dispatch](../setup/built-in-dispatch.md)) |
| Units | `Config.Units`, `Config.K9`, `Config.SheriffAreas`, `Config.FallbackWeapons`, `Config.Sirens` ([Units](../setup/units.md)) |
| On scene | `Config.ComplyTime`, `Config.SurrenderKey`, `Config.TaserRange`, `Config.CloseRange`, `Config.OfficerMovement`, `Config.Speech`, `Config.Radio` |
| Pursuits | `Config.PursuitBackup`, `Config.Roadblocks`, `Config.PIT`, `Config.BoxIn`, `Config.FelonyStop`, `Config.LostSuspect`, `Config.EscapeTime`, `Config.Descriptions`, `Config.AirUnit` ([Pursuits](../gameplay/pursuits.md)) |
| Downed / logout | `Config.JailOnDeath`, `Config.DownedWarrant`, `Config.JailOnDisconnect` |
| Charges | `Config.Charges` (label, sentence min / max, fine), `Config.MinSentence`, `Config.MaxSentence` |
| Traffic | `Config.TrafficStops`, `Config.Citations`, `Config.Fines` ([Traffic stops](../gameplay/traffic-stops.md)) |
| Evidence | `Config.Consent`, `Config.VehicleSearch`, `Config.Search`, `Config.Evidence` ([Search & evidence](../gameplay/search-and-evidence.md)) |
| Booking | `Config.Transport`, `Config.Booking`, `Config.Mugshot`, `Config.Paperwork` ([Booking](../gameplay/booking.md)) |
| Holding cell | `Config.Bail`, `Config.Lawyer`, `Config.Plea`, `Config.CommunityService` |
| Jail | `Config.BuiltinJail`, `Config.PrisonCheck`, `Config.Unjail`, `Config.ReleaseCooldown` ([Jail](../gameplay/jail-and-warrants.md)) |
| Records | `Config.Records`, `Config.Warrants`, `Config.MDT`, `Config.Impound` |
| Patrols | `Config.AmbientPatrols` |
| Staff | `Config.StaffCases` |
| Other scripts | `Config.Integrations` ([Other scripts](../integrations/other-scripts.md)), `Config.Standalone` ([Standalone](../integrations/standalone.md)), `Config.Justice` ([Justice System](../integrations/justice-system.md)) |

{% hint style="info" %}
Every setting has a comment next to it in `config.lua` saying what it does and what the values mean.
{% endhint %}
