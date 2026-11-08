# Power

## Today

One old CyberPower 1500VA carries both racks. That's why the R630 stays off: on battery, two
servers would drain it and take the network down with them.

## Plan (Phase 2)

- A 2U rack UPS for the server rack only: ≥1,500VA, ≥1,000 W output, pure sine wave, with a USB or
  network shutdown signal to Unraid (and later the R630) so the array stops cleanly on battery.
- The CyberPower 1500VA goes back to just the network rack: fiber jack, router, switch.
- Test it: pull the plug, time the runtime, confirm Unraid shuts down cleanly.
- Candidate noted in 2024: <https://www.amazon.com/dp/B0016P8OII/>. Check it against the sizing above.

## Load estimates

Estimated peak at the wall, server rack only.

| Phase | Load | Peak |
| --- | --- | --- |
| P1–P2 | X15 + 11 drives | ~400 W |
| P3 | X15 + R630 | ~800 W |

Both fit the existing 15A circuit (1,440 W continuous at 80% of the breaker). No new circuit needed.
