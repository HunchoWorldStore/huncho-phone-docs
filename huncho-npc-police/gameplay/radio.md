# Police radio

`Config.Radio`: on arrival, shots fired, pursuits, foot chases, backup, losing and spotting the suspect, felony stops, custody and escapes, the suspect:

* hears a radio click,
* sees a line of radio chatter at the bottom of the screen (the `radio_*` texts in the locales),
* hears the officers say one of GTA's own voice lines (`voiceLines`, for example the megaphone "pull over").

{% hint style="info" %}
**The radio never warns a suspect that police are coming.** It's only heard with an officer within `hearRange` (30 m by default), the way you'd really hear their radio. The "units responding" line when a call goes out is off (`toSuspect = false`); set `toSuspect = true` if you want suspects warned.
{% endhint %}

A voice line GTA doesn't know just stays silent. GTA's police scanner reports are all story-mission lines, so they're off by default; add your own per event in `scanner`.
