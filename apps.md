# Apps

| App | What it does |
| --- | --- |
| Phone | Calls with mute, speaker (people near you hear it) and ringback. Recents, contacts, contact sharing with people next to you, **voicemail** |
| Messages | Texts and group chats with photos, videos, money and your location |
| Mail | An address for every phone (`3105550111@hmail.com`, or a name the player picks). Inbox, Sent, replies, and buttons in mail from scripts |
| FaceLink | Video calls with front and back camera. Switch a voice call to video without hanging up |
| Camera & Photos | Walk around while aiming, photos and video clips with voices, **AirDrop** to people next to you |
| Notes | Notes saved on the phone, pinning and search |
| Calculator | A standard calculator (keyboard works too) |
| Clock | Alarms that ring even with the phone away, a timer and a stopwatch |
| Instashot · Bird Box | Photo and video posts, reactions, comments, follows, profiles |
| SneakyFan | Creator subscriptions with locked posts and payouts |
| UPoppin | Live streams with camera and voice, chat and gem gifts |
| Music | Your server's music, playlists, speaker mode for people nearby, and GTA radio |
| Garage · Cribs | Your vehicles with GPS and valet delivery; your homes, locks and keys |
| Wallet · Fleeca | Balance, transfers and bank history |
| Services · Maps · Weather | 911 and your businesses routed to whoever is on duty, a full map, live weather |
| App Store · Settings | Download apps per phone; wallpapers, accent colours, sounds, passcode, **blocked numbers** and **language** |

Mail, Notes, Calculator and Clock are on every phone. Everything outside `Config.Apps.preinstalled` is downloaded from the App Store.

## Social accounts

Accounts on Instashot, Bird Box, SneakyFan and UPoppin have a username and password and work on any phone.

* **Several accounts:** tap your @name on your profile (SneakyFan: My SneakyFan) to switch accounts without the password, add one, or remove one from the phone. Up to `Config.Social.maxSavedAccounts` (5) per app. Notifications reach every account on the phone and say which @account they're for.
* **Log out** takes the account off the phone and opens your next one. **Log out of all accounts** is on the accounts screen.
* **Forgot password?** mails a 6-digit code to the account's **recovery email** (Edit profile). Left empty, it goes to the phone that made the account. The code works for 10 minutes and resetting logs the account out on every other phone. No recovery email? Staff can use `/phone_resetpw`.

## Blocked numbers

Block a number from a contact or in Settings. Blocked numbers can't call, text, mail or leave a voicemail, and they aren't told.
