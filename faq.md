# FAQ

## Nobody can hear on speaker

Update to 1.1.3 or newer: older versions turned the call volume almost to 0 on speaker (pma-voice). `Config.Calls.speakerVolume` sets how loud it is (0.0 - 1.0). Speaker needs pma-voice or mumble-voip.

## Photos, video or voicemail recordings don't work

Set `ServerConfig.FivemanageKey` in `config_server.lua`. The console tells you when it's missing. Without a key, voicemail still works as a typed message.

## The phone says no banking, garage or housing system was detected

Check the console line at start-up. If your script uses a different resource name, set it in `Config.Integrations`.

## Can videos record game sounds?

No FiveM phone can. Clips record the camera and players' voices (push-to-talk is respected).

## My Fivemanage files use a custom domain

Add that domain to `Config.ProfileMedia.allowedHosts`.

## A script made for another phone still doesn't send mail

Some scripts check which phone is running before they send anything. Set that script's phone option to **qb-phone** (or lb-phone) in its own config.

## When do alarms ring?

Alarms use the player's own clock and ring while they carry that phone, even with it put away, once the phone has been opened that session.

## FaceLink or live video doesn't connect for some players

Video goes player to player. Add a TURN server in `Config.Video.iceServers` for players on strict networks. Without one, those players get lighter frames through your server.
