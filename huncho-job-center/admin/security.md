# Security

The server picks every route, so clients can't choose their stops. Each completed task is checked for being in order, the player's distance from the stop, and a minimum time per task. Each task pays the job's fixed `payPerTask`, set on the server. Pay only goes out at clock-out, at the depot, and leaving mid-shift forfeits it. If the resource restarts, players are paid what they had earned plus their deposit.

## What the server checks

* **Routes:** the server picks every stop. Clients can't choose or skip them.
* **Order:** each task must be the next one in the route.
* **Distance:** the player must be near the stop (`Config.StopValidationDistance`).
* **Time:** a minimum time per task (`minStopTime` in each job file).
* **Pay:** each task pays the job's `payPerTask`, set on the server. Shop prices and item rewards are rolled on the server too.
* **Job-specific checks:** fish can't be landed faster than possible, papers must really be thrown from the job bike, dog walks measure the distance actually walked.

Failed checks are sent to Discord as **flags** (see [Discord logs](../configuration/discord-logs.md)).
