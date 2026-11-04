# Changelog

## 1.15.0

- **Translations: Spanish, Portuguese (Brazil), French and German** for all eight games and the admin panel. Every notification, prompt, panel, rules page and result screen is translated, plus the Oh Bih Please and Oh Bih Roulette cards, the Slumlords cards and squares, and the Dominoes and Tumbling Towers text that used to be built into the code. Set one language for the whole pack with `Config.Language` in `games/admin/config.lua` (`'es'`, `'pt-br'`, `'fr'`, `'de'`), or set `Config.Locale` per game.
- **Update notice:** when the pack starts (and every 6 hours) it checks for a newer version and prints a notice in the server console with what's new. Turn it off with `Config.UpdateCheck.enabled = false` in `games/admin/config.lua`.
- Game versions: Card Hub 1.5.0, Cee-lo 1.1.0, Dominoes 1.3.0, Beer Pong 1.1.0, Oh Bih Please 1.3.0, Oh Bih Roulette 1.1.0, Slumlords 1.1.0, Tumbling Towers 1.4.0.

## 1.14.0

- **New: one admin panel for the whole pack (`/gamepack`).** Server admins (`group.admin`, or any ace group you set in `games/admin/config.lua`) get three tabs:
  - **Live tables:** every table someone is at, in every game: what's being played, who's seated, bots, stakes and the pot. **Go to** teleports you next to it; **End game** stands everyone up and refunds every stake.
  - **Games:** turn any game **on or off** (off ends its games with refunds, hides its permanent tables and stops new ones), switch **item / command / both**, and set the **stake limits**. Saved changes are kept on the server, survive updates to the pack, and **Reset to config file** goes back to the config. Stake limits and on/off work right away; changing how a game starts needs a restart, and the panel tells you.
  - **Permanent tables:** place Card Hub, Dominoes, Beer Pong, Oh Bih Please, Oh Bih Roulette and Slumlords tables yourself. A preview appears in front of you; turn it and press E. They come back after every restart, and you can go to or remove them from the list. (Cee-lo and Tumbling Towers are set up by players on the spot.)

## 1.13.3

- No changes in this edition (internal update).

## 1.13.2

- **Card Hub 1.4.2:** the top card of the pile is always the last one played (Last Card, Crazy 8s, Tonk). Before, once the pile had 12 cards, new cards landed level with the old top and an older card could show on top.

## 1.13.1

- **Card Hub 1.4.1:** the pile, deck and moving cards are drawn at real size flat on the table (they were showing huge above the players), and Look mode is easy to leave again: a clear bar on screen, and E, Backspace or a left click gives the cursor back.

## 1.13.0

- **Fixed: placing tables with the command (or the item) wouldn't move or place** in Card Hub, Oh Bih Please and Oh Bih Roulette. The preview now follows where you look, stays within reach, sits on the floor, and goes just in front of you when you look level or up.
- **Card Hub 1.4.0:** cards sit on the real table top (no more floating hands, rows, deck or pile); players place their cards on the table: a played card leaves their row, drops onto the pile and lands on top of the stack, and draws, gives, tricks, spreads and books move row to table; your own ped is hidden on your screen while the table camera is on, so it can't block the view.

## 1.12.0

- **Card Hub 1.3.0: every card at the table matches.** The draw stack, the pile, Spades tricks, Tonk spreads, Go Fish books and cards in flight use the same card art as the hands (no more casino card props with a different back). Last Card gets its own back. Other players' rows lie nearly flat so they read from every seat.

## 1.11.0

- **Card Hub 1.2.0: everyone's hand on the table, like Dominoes.** Each player's cards stand in a row in front of them, backs out, with the real card count, and your own stay face-up. `Config.TablePlay.handsOnTable = false` brings back the fan in each player's hand.
- **Tumbling Towers 1.3.2:** turning the tower is easier. A / D, the arrow keys or a right-mouse drag, at any time while seated (`Config.Camera.orbitAlways`). The hint bar shows the keys on your turn, and X takes you back to your chair.

## 1.10.1

- **Fixed: using the item did nothing** for Card Hub (`card_table`), Oh Bih Please (`ohbihplease_deck`), Oh Bih Roulette (`bihroulette_wheel`) and Tumbling Towers (`tumbling_towers`) on Qbox + ox_inventory. Those games now hook ox_inventory's item use directly, on any framework, like the other games already did. The `server = { export = ... }` lines in `install/items/ox_inventory.lua` are now on by default as a backup; you don't have to re-paste the items, but it doesn't hurt.

## 1.10.0

- **Item, command or both for every game.** Each game has one setting for how a table is started: `'item'`, `'command'` or `'both'` (default both). New for Cee-lo (`Config.Start.method`), Dominoes (`Config.TableItem.method`, command `/dominotable`) and Slumlords (`Config.TableItem.method`, command `/slumlordstable`); Card Hub now defaults to both. See *Commands at a glance* in the README.
- **Tumbling Towers 1.3.0:**
  - Look around the table with the mouse (hold the right mouse button on your turn), X recenters, Q / E lower and raise your view.
  - On your turn A / D take your view all the way around the tower to check every side; it eases back to your chair when your turn ends.
  - Players nearby can **watch** a game: aim at the table (or press G) for a camera around the table, the scoreboard, the tumbles and the results.
  - Shots before you're out: Sudden death, 1, 2, 3, 4, 5, 7 or 10.
  - Setting up and joining work like the other tables: see-through table and chairs, Scroll rotates, E places; ox_target / qb-target on the chairs and table.
  - A proper results screen with standings, **Run it back** for the host, Leave, and a countdown back to the table menu.
  - Fixed the menu jumping around and the screen blurring when you switched designs.

## 1.9.0

- **Tumbling Towers 1.2.0:** new item `tumbling_towers` (Tumbling Towers Set). Use it to set up a table, or keep using `/tumblingtowers`. Added to every file in `install/items/`, with its image in `install/images/`.

## 1.8.1

- **Tumbling Towers 1.1.1:** the block now follows the player's hand. It waits while they reach in, slides out as their hand draws back, and is drawn along the table into their hand. A safe pull nudges the stack slightly while the block drags out.

## 1.8.0

- New game: **Tumbling Towers** (`games/towers/`, from `tumbling_towers` 1.1.0), the block-stacking tower game at a real table. Everyone sits in casino chairs with synced seated animations, and while you play your view is your own eyes in your chair: lean around the tower and lean in. Players reach for the tower, the block slides out of the stack into their hand, and they set it on top. Whoever knocks it over takes a whiskey shot in their chair. NPCs, free or cash games, four designs.
- Start a table with `/tumblingtowers` (no item needed).

## 1.7.0

- New game: **Oh Bih Roulette** (`games/bihroulette/`), the spin-the-wheel party game. A game-show wheel lies in the middle of the table and everyone nearby watches it spin and land; the same wheel spins big in the panel. Slices: Truth, Dare, Take a Shot, Wild Card, Hot Seat (the table votes "who's most likely to..."), Give Out, Social, Spin Again, plus Make It Rain, Pay Up and Jackpot.
- Two modes, picked by the host: **Dare or Pay** (everybody starts with play-money racks; skip a truth or dare and pay into the pot or drink, hit Jackpot to take the pot, most racks at the end runs the table) and **Party** (drinks only). Racks never touch real money.
- About 130 new cards in Truth, Dare, Shot, Hot Seat and Wild piles (Clean or Spicy), including the racks wilds Snatch and Tax Day. Cash stacks sit in front of players in Dare or Pay.
- Same table, chairs, shot glasses, drunk effects, bots and awards as Oh Bih Please. New item `bihroulette_wheel` (command `/bihroulette`) in every `install/items/` file, plus its image.

## 1.6.0

- **Card Hub 1.1.0, table play**: your cards now sit on the table in front of you as real cards, the same way Dominoes shows its tiles. The camera leans in over your seat, you hover a card to lift it and click to play it, and click the deck to draw. Playable cards glow, the top card shows face-up on the pile, and a slim bar keeps the buttons cards can't do (bids, pass, drop, Go Fish asks). The full panel is one click away and each player's choice is remembered.
- New Card Hub setting `Config.TablePlay` for the camera, card size, tilt, spacing, highlight colours and card backs.

## 1.5.2

- Changelog cleaned up so it only lists changes in this edition.

## 1.5.1

- No changes in this edition (internal update).

## 1.5.0

- New game: **Slumlords** (from `sage_slumlords` 1.0.2), the 2-6 player property trading board game played at a real table: the live board on the tabletop, 3D dice and pins, houses and hotels, auctions, trades, bots and buy-in pots (`games/slumlords/`).
- `install/` now includes the `slumlords_board` item for every inventory, plus its image. On ox_inventory it uses `server = { export = 'hunchoworld_gamepack.useBoard' }`.
- Slumlords exports also have pack names: `IsPlayingSlumlords` / `GetSlumlordsTableId` (server) and `IsSeatedAtSlumlords` (client). The original names still work.

## 1.4.0

- No changes in this edition (internal update).

## 1.3.0

- Oh Bih Please 1.2.0: cap is now for truths (call cap when you think someone's lying); dares are Completed or Skip & Drink.

## 1.2.0

- Oh Bih Please 1.1.0: new 130-card deck where every card matches its type, cap votes for dares only (truths finish on ANSWERED), and clearer, more reliable drinking (cards land before drinks, DRINK UP banner, fallback drink animation). See `games/ohbihplease/CHANGELOG.md`.

## 1.1.1

- Oh Bih Please: fixed the "call out" menu showing `T_UNDEFINED` as its heading when no card was in play.

## 1.1.0

- New game: **Oh Bih Please**, the party card game. Truth, dare, shots and wild cards at a real table, with cap calls, votes, drinking buddies, house rules, bots, light drunk effects and its own UI and card designs (`games/ohbihplease/`).
- `install/` now includes the `ohbihplease_deck` item for every inventory, plus its image.

## 1.0.1

- Card Hub: fixed `attempt to index a nil value (global 'Locales')` on start. The English text now loads, so menus show real text instead of keys. Translation files you add later load correctly too.
- The top-level `install/` folder is now left readable under escrow, so the item files can be opened.

## 1.0.0

First release of the Huncho World Game Pack: Card Hub, Cee-lo Street Dice, Dominoes (with streamed props) and Beer Pong in one resource.

- One `ensure` for all four games, with each game kept in its own folder and config.
- One `install/` folder with every item for every supported inventory, plus item images.
- Dominoes ships with no fixed tables; players place their own with the table item (fixed tables are optional in `config/tables.lua`).

Each game's own history is in `games/<game>/CHANGELOG.md`.
