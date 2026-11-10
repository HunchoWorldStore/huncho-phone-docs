# Installation

## 1. Add the resource

Put the `hunchoworld_bookbags` folder in your resources. The 528 props and `hw_bookbags.ytyp` are already in `stream/`.

## 2. Add the items and images

Follow [Adding the items](items.md).

## 3. Start it

In `server.cfg`, after your framework and inventory:

```
ensure hunchoworld_bookbags
add_ace group.admin hwbags.admin allow
```

On start, the server console prints the framework and inventory it found. If it says it could not detect your setup, see [Custom framework or inventory](../integrations/custom-scripts.md).

{% hint style="warning" %}
Players need to reconnect after the first start so the props download.
{% endhint %}
