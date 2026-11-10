# Crews, bonuses and leaderboards

## Crews

Jobs with `crew` set in their file can be worked together, sized to the seats in each job's vehicle: up to 4 for garbage, construction, landscaper, janitor, graffiti removal, news crew, package delivery and postman, and 2 for road crew, lumberjack, electrician and window washer. The food truck seats only the driver, so it stays solo. Someone starts a shift as normal. Anyone else signed up for that job sees them in a **Join a crew** list at the depot and asks to join, and the leader gets a pop-up to accept. The crew shares the leader's stops and work vehicle (members get keys). Each person does their own part at every stop, and the next stop comes once everyone has finished. Everyone earns their own task pay plus the crew bonus (`Config.Crew`, +10% by default). Set `crew = 2` (or any number) in a job's file to change its crew size. A crew is also capped at the seats in the leader's actual vehicle, so a swapped-in model can't overfill it. Members can clock out any time. If the leader clocks out or disconnects, the crew is paid out and sent home.

## Job of the day

Each day one job (picked automatically, same for everyone, only jobs that pay per task) pays a bonus (`Config.DailyJob`, +25% by default). It's highlighted in the job center and on the depot time card, and locked in for the whole shift at clock-in. Admins can change it with `/jcdaily <job>`.

## Work streak

Clock out with at least `minTasks` tasks done on consecutive days and the bonus grows: day 2 +2%, day 3 +4%, up to +10% (`Config.Streak`). Missing a day starts it over. With the level system off, the streak shows in the job center where the level would be.

## Leaderboard

A Leaderboard tab in the job center shows this week's top earners (resets Monday) and all-time records: biggest paycheck, most tasks in one shift, heaviest catch and most valuable find (`Config.Leaderboard`).

Every bonus is listed on the pay stub.

## Settings

```lua
Config.Crew = {
    enabled        = true,
    maxSize        = 4,     -- most players in any crew, leader included
    bonus          = 0.10,  -- +10% per task while in a crew
    requestTimeout = 20,    -- seconds the leader has to accept
}

Config.DailyJob = {
    enabled = true,
    bonus   = 0.25,         -- +25% in that job today
    exclude = {},           -- e.g. { valet = true }
}

Config.Streak = {
    enabled  = true,
    perDay   = 0.02,
    max      = 0.10,
    minTasks = 3,           -- tasks needed in a shift for the day to count
}

Config.Leaderboard = { enabled = true, size = 10 }
```
