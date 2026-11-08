# Power

## Today

Each rack has its own 1U CyberPower UPS, and each reports to the server in that rack over USB.
Readings from each server's Unraid dashboard, 2026-11-07.

| Rack | UPS | Rating | Load | Runtime | Reports to |
| --- | --- | --- | --- | --- | --- |
| Network rack | CyberPower OR700LCDRM1U | 700VA / 400 W | 48 W (12%) | 75 min | [Sentinel](servers/sentinel.md) |
| Server rack | CyberPower OR500LCDRM1U | 500VA / 300 W | 186 W (62%) | 9 min | [Darkrock](servers/darkrock.md) |

The network rack (fiber jack, router, TL-SX1008, Sentinel) barely touches its UPS.

The server rack is the problem. Darkrock alone is 62% of a 300 W unit with nine minutes of runtime,
which is why the R630 stays off: together they'd overrun it.

The old CyberPower 1500VA tower sits on the floor beside the server rack.

## Plan (Phase 2)

Replace the server rack's OR500 with a 2U rack UPS. The network rack keeps its OR700.

- ≥1,500VA, ≥1,000 W output, pure sine wave, with a USB or network shutdown signal to Unraid (and
  later the R630) so the array stops cleanly on battery.
- Pure sine matters for the X15: its Corsair RM1000x has active PFC, which can drop out on the
  simulated sine wave the OR series puts out on battery.
- Test it: pull the plug, time the runtime, confirm Unraid shuts down cleanly.
- Candidate noted in 2024: <https://www.amazon.com/dp/B0016P8OII/>. Check it against the sizing above.

The X15 can't wait for Phase 2 on the OR500: its ~400 W peak is more than the OR500 can deliver.
Either do Phase 2 first, or run the X15 from the 1500VA tower until the rack UPS arrives.

## Load

Server rack only, against its UPS.

| Phase | Load | Draw | OR500 (300 W) | Phase 2 UPS (≥1,000 W) |
| --- | --- | --- | --- | --- |
| Today | Darkrock + 10 drives | 186 W measured | fits, 9 min | fits |
| P1 | X15 + 11 drives | ~400 W peak, est. | no | fits |
| P3 | X15 + R630 | ~800 W peak, est. | no | fits |

Drive spin-up at boot is the peak; steady-state draw is lower.

Everything fits the existing 15A circuit (1,440 W continuous at 80% of the breaker). No new circuit
needed.

## TODO

- [ ] Decide what the CyberPower 1500VA tower still powers, if anything, or retire it.
- [x] Connect each rack's UPS to its server over USB.
- [ ] Set Unraid's UPS shutdown thresholds on both servers and test them.
