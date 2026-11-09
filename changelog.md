# Changelog

## 1.1.4

* **Fix: selfies and photos turned into videos.** The camera couldn't tell photos were set up after the Fivemanage key moved to `config_server.lua`, so it switched every photo and selfie to video.

## 1.1.3

* **Fix: you couldn't hear anything on speaker.** Speaker now sets the call volume to 90 (it was almost 0), and it goes back to normal when you turn speaker off or hang up.
* **Several accounts** on Instashot, Bird Box and SneakyFan. Tap your @name on your profile to switch (no password), add an account or remove one. Up to 5 per app on a phone (`Config.Social.maxSavedAccounts`).
* **Forgot password?** on the login screen mails a 6-digit code to the account's recovery email (set in Edit profile; empty = the phone that made the account).
* `/phone_resetpw <app> <username> <new password>` for staff.
* `Config.Social.maxAccountsPerPhone` now defaults to 3.

## 1.1.2

* **Background apps:** custom apps added with `background = true` keep running outside the app, so music keeps playing.

## 1.1.1

* **Fix: the phone wouldn't open on some servers.** Scripts written for lb-phone or npwd that turn "their" phone off are ignored unless `Config.Compat.honorDisable = true`. F8 names the script that tried.
* `/phonedebug` prints in F8 why the phone won't open.

## 1.1.0

* **Mail** with an address per phone, replies, a Sent folder and buttons from scripts.
* **Notes, Calculator and Clock** (alarms, timer, stopwatch) on every phone.
* **Voicemail** after a missed call, recorded or typed.
* **Block numbers** from contacts or Settings.
* **AirDrop** photos and videos to people next to you.
* **Staff tools** in the social apps and the `/phone_ban` and `/phone_unban` commands.
* **Discord logs** for posts, lives, money, mail, AirDrop and staff.
* **Works with scripts made for qb-phone, qs-smartphone, qs-smartphone-pro, lb-phone and npwd.**
* **Five languages** and a language picker in Settings.
* **The Fivemanage key moved to `config_server.lua`**, which is never sent to players.

## 1.0.16

* The 3D phone models are built into `hw_phone`. One resource, nothing extra to install.

## 1.0.15

* Custom apps are listed in the App Store and downloaded per phone. `preinstalled = true` keeps one on every phone.

## 1.0.14

* More inventories, banking, garage and housing scripts, all auto-detected.
