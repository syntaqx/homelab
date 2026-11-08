# Roadmap

Storage first, then power, then compute the rack already owns. No GPU node and no new electrical
circuit. Prices are USD as of 2026-11-07, before tax and shipping; "est." is a planning estimate.

The build plan is drawn as two blueprint sheets: phased rack elevations, and systems, storage,
power and cost. Exports live in [`assets/plans/`](../assets/plans/).

| Phase | What | Cost |
| --- | --- | --- |
| P1 · Storage | 45HomeLab X15 replaces Darkrock | $3,941–3,991 |
| P2 · Power | Bigger UPS for the server rack | $500–1,000 est. |
| P3 · Compute | R630 back on with Proxmox | ≤$150 est. + SSDs |
| | **Total** | **$4,441–5,141** + SSDs, drives |

## P0 · Before buying

- [ ] Measure the server rack's post depth → choose the X15 rail kit (27″ or 36.4″)
- [ ] Confirm the top unit's real height (drawn as a 2U drawer)
- [ ] Check the R630's network daughter card: 10GbE or 1GbE?
- [ ] Decide the Unraid boot path: carry the current flash over, or use the X15's license and internal boot

## P1 · Storage (now)

- [ ] Order the X15: 64GB ECC, rails, 2× 2.5″ bay adapters
- [ ] Power for the X15: its ~400 W peak overruns the server rack's 300 W UPS, so land P2's UPS first or run it from the 1500VA tower
- [ ] Preclear the spare 20 TB Exos over USB while waiting
- [ ] Rack the X15 above the UPS; update BIOS and microcode; burn in
- [ ] Migrate: [runbooks/x15-migration.md](runbooks/x15-migration.md)
- [ ] Spare 20 TB into bay 11 as Disk 7 (104 TB array)
- [ ] Retire Darkrock and the plywood top; move the R630 up to U10
- [ ] Gate: array healthy after a clean parity check, tower empty

## P2 · Power (next)

- [x] A UPS per rack (CyberPower OR700 network, OR500 server)
- [ ] Replace the server rack's OR500 with a 2U UPS: ≥1,500VA, ≥1,000 W, pure sine, shutdown signal
- [ ] Gate: UPS live, runtime tested by pulling the plug, clean shutdown confirmed

## P3 · Compute (when wanted)

- [ ] R630 bring-up: [runbooks/r630-bringup.md](runbooks/r630-bringup.md)
- [ ] 2× SSDs for VM storage
- [ ] 10GbE daughter card, if needed
- [ ] VM backups to the X15

## Growing the array

Fill bays 12–15 with 20 TB disks first (no rebuild), then swap the three 8 TB disks. Details in
[storage.md](storage.md).
