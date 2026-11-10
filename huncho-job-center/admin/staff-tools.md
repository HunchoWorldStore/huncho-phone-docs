# Staff tools

- **Discord logs** ([setup](../configuration/discord-logs.md)): shifts started and ended (pay, tasks, time, deposit, bonuses), crews, shop sales, admin actions, new records and **flags** for failed server checks (a task handed in away from the job site, a fish landed faster than possible, a paper "delivered" without one being thrown, someone leaving mid-shift). Big paychecks and sales are highlighted, and flags can ping a staff role. Messages are batched so Discord's rate limit isn't hit.
- **`/jcshifts`**: everyone on shift, with their job, tasks, earnings, time and crew. Teleport to them, or end their shift with or without pay.
- **`/jcpay`**: the pay overview. Real $/hour for every job from finished shifts (task pay, bonuses and shop sales included), hours worked, average time per task and total paid out. It's sortable, and jobs well above or below the median are marked **High** or **Low** so you can balance pay. `/jcpayreset` clears the numbers to start fresh.
- **`/jcdaily [job]`**: change today's job of the day (no job = back to automatic).
- **`/jclocations`**: move any location in game (see [Locations](../configuration/locations.md)).
- **`/jcuniforms`**: set job uniforms in game (see [Uniforms](../configuration/uniforms.md)).
