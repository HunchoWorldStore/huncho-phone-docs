# Changelog

## 1.23.1

* **The police radio no longer warns suspects that police are coming.** The "units responding" line is off (`Config.Radio.toSuspect = false`), and radio chatter and officer lines are only heard with an officer within `hearRange` (30 m)
* The update check in the server console now works: it reads the version published with these docs

## 1.23.0

* **Community service finds your script:** the Justice System, sleezy\_coms, randol\_service, bc\_communityservice, esx\_ / mh-communityservice and rcore\_prison COMS are used automatically (`provider`, `order`), with the built-in one as the fallback
* Built-in community service on the aircraft carrier (sleezy\_coms task spots, map loaded automatically), GPS to each spot, released at LSIA
* `/npcpoliceremovecs [id]` ends a player's community service

## 1.22.0

* **Felony stops** for serious suspects in vehicles: officers behind their doors, step-by-step orders, pulled out + Resisting for staying in
* **Searching after losing sight:** officers search where you were last seen instead of always knowing where you are
* **Suspect descriptions:** change clothes, mask or car while out of sight and you're only recognised up close
* **Police radio:** radio clicks, chatter and GTA voice lines
* **Plead guilty** and **community service** in the holding cell
* **Staff case view:** `/npcpolicecases`

## 1.21.0

* Trapping integration: drugs from hunchoworld\_advancedtrapping / sage\_trapping are illegal items and evidence automatically, cuffing ends a trapping session, seizures show in its dashboard

## 1.20.0 - 1.20.1

* Shooting victims no longer get the police on them; the shooter does
* Only real players shooting at you count by default (`npcAttackers = false`)

## 1.19.0

* Officers vault low fences, climb ladders and drop off ledges in foot chases
* Police can't get into locked areas or houses
* Arrest after being downed is a switch (`Config.JailOnDeath`), with a warrant instead (`Config.DownedWarrant`)
* An officer always comes to you before questions, tests and the search

## 1.18.0

* Gameplay and Justice System lines merged into one script
* Officer-requested backup follows taser range, close range, line of sight and sheriff territory

## 1.17.0

* Release cooldown after jail and bail
* Getting away works: patrols leave wanted players alone, and the warrant's charges are added to the next arrest
* Fixed arrest steps being skipped

## 1.16.0 - 1.16.1

* Sheriff territory: Sandy Shores, Grapeseed and Paleto Bay are answered by sheriff units with BCSO plates
* Minor leftovers after the evidence check: fined and released instead of jailed
* Players in their homes are no longer picked or arrested

## 1.15.0 - 1.15.6

* One-switch difficulty (easy / normal / hard / custom), and your own single values are kept
* Ramming officers can be switched off (`Config.Calls.officerram`)
* Officers walk right up before cuffing, tickets, questions and tests; lower taser range
* `/npcpoliceoutfit`, sheriff and SWAT livery and extras
* Justice System: backup units that fight back, cuff & search and chase by the officer's own units, a reworked air unit, `/npcpoliceclearrecord` clears the Justice MDT

## Earlier

* AI air unit, Justice System integration, built-in dispatch, Bond & Counsel screen, written citations, license / registration / insurance checks, consent and vehicle searches, GSR tests, evidence stash, robbery and drug-sale detection for any script, standalone mode, no-code integrations, and support for dozens of dispatch, prison, garage, banking, billing and ambulance scripts
