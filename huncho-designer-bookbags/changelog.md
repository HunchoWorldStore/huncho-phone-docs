# Changelog

## 1.2.1

* Tuned default bag and strap positions for every wear style, for male and female characters. Bookbags and minis sit closer to the body and their straps line up on the shoulders out of the box.

## 1.2.0

* 24 new designs made for women, 3 per house: 88 designs, 176 items and images, 528 props
* Added tgiann-inventory and ak47_inventory support
* wasabi_inventory now uses this script's straps, wear styles and bag storage
* qs-inventory: fixed stash IDs for searches and removing bags put inside bags
* qb-inventory: bag storage is created before searches read it
* Qbox: items can be made usable on inventories other than ox_inventory
* New `server/bridge/custom.lua` for connecting your own framework or inventory

## 1.1.5

* Mini bookbags now have their own straps that connect to the bag
* Tuned default positions for all wear styles

## 1.1.4

* Using the bag you are wearing now opens a menu to open it, change style or take it off

## 1.1.3

* Removed the opening animation and the in-hand pose. Bags stay on the player and open straight away
* Added `Config.WearAnimations` to turn the put-on and take-off gestures off

## 1.1.2

* `/bagfix` now saves every part and style you changed, including when you switch parts or close the panel
* The server console reports how many saved positions and shops loaded, and warns if a save fails

## 1.1.1

* Tuned default positions for every wear style, the in-hand pose and the opening pose

## 1.1.0

* Straps now sit over the shoulders: every bag has its own strap props (256 props in total)
* Wear styles: on the back, on the chest or one strap, picked from a menu when putting a bag on
* `/bagstyle` changes the style of the bag you are wearing
* Animations for putting a bag on, taking it off and opening it
* `/bagfix` can now position the bag and each strap per style, plus the in-hand and opening poses

## 1.0.8

* Updated default bookbag positions for male and female characters

## 1.0.7

* Shops and prop fixes now save to the server's key-value storage, so restarts, updates and read-only files cannot wipe them

## 1.0.6

* Tuned default bag positions for male and female characters

## 1.0.5

* Fixed shop peds not spawning: the default ped model name was wrong
* A shop with a bad ped model now uses the default ped and prints a console warning
* Press E still works at a shop if its ped cannot spawn

## 1.0.4

* Police scripts can now search bags: new server exports `GetCarriedBags(src)` and `RemoveFromBag(src, bagId, item, count, slot)`
* Bag contents can be read on ox_inventory, qs-inventory and qb-inventory v2

## 1.0.3

* Worn bags now stay on after relogging, switching characters and server or script restarts

## 1.0.2

* Prepared for Cfx.re Asset Escrow: props are now encrypted, and buyers keep access to config and bridge files
* Protected the NUI code in the store build
* Prop fix panel button renamed to Copy fixes

## 1.0.1

* Props now ship as finished `.ydr` files with `hw_bookbags.ytyp` in `stream/`. No CodeWalker import needed

## 1.0.0

* First release: 8 houses, 64 designs, bookbag and mini sizes
* Auto-detects Qbox, QBCore, ESX and ox, qb, ps, lj, qs and wasabi inventories
* Wearable bags with their own storage
* In-game shop creator and storefront
* `/bagfix` live prop position tool with save and export
