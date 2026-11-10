# How it plays

1. **Job Center.** Browse jobs by category and see each one's description, pay, vehicle, deposit and duties, then sign up. GPS is set to that job's depot.
2. **Depot.** Talk to the supervisor and start the shift. The player changes into the job's uniform and the work vehicle spawns with keys and a full tank. A refundable deposit is taken from the bank.
3. **Work.** Each task is marked on the map. The on-screen time card shows tasks done, the running total and what to do next. Tasks are done by walking to the yellow marker and pressing **E**.
4. **Clock out.** Tasks keep coming until the player heads back to the depot and clocks out. A pay stub shows tasks times pay per task, every bonus, the deposit refund and any damage fee. Their own clothes come back.

## Ending a shift early

* **At the depot:** choose "Clock out and get paid". The vehicle has to be parked back at its spawn point to refund the deposit.
* **Anywhere:** type `/endshift`, press **F7**, or target the work vehicle and pick "End shift". A confirm box shows the pay and what happens to the deposit. The deposit is refunded (minus damage) if the work vehicle is within 15 m, otherwise it's forfeited.

All of this is set in `Config.EndShift`: turn it off, change the command or key, set the distance, or pay less than 100% away from the depot (`payPercent`) to reward driving back.

If a player disconnects mid-shift, that shift's earnings are forfeited and the vehicle is removed. If the resource restarts, everyone on shift is paid what they had earned plus their deposit.
