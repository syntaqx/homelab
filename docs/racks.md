# Racks

Two racks in the basement utility room: a wall-mounted network rack and a rolling server rack
underneath it. The full phased plan for the server rack lives in [roadmap.md](roadmap.md).

## Network rack

12U open frame, wall mounted. This is where the internet comes in and where every 10GbE link meets.

| Item | Notes |
| --- | --- |
| [Tecmojo 12U Open Frame Network Rack](https://amzn.to/3y5hepV) | Wall mounted |
| GFiber Fiber Jack | 5 Gig service |
| GFiber Wi-Fi 6E Router | Plus 2× GFiber Wi-Fi 6E Extenders around the house |
| TP-Link TL-SX1008 | 8-port 10G/Multi-Gig, unmanaged. Added June 2026, replacing the [MokerLink 8 Port 10Gbps switch](https://amzn.to/4cdCKqy) |
| [Iwillink 24 Port Blank Keystone Patch Panel](https://amzn.to/3WhhPg9) | [VCE blank keystone inserts](https://amzn.to/3yhkaj5), [iwillink 10Gbps CAT7 keystone couplers](https://amzn.to/46ocRTC), [Cat8 0.5ft patch cables](https://amzn.to/3WdKXVv) |
| [1U Hinged Vented Blank Panel](https://amzn.to/4d1FhVH) | |
| [StarTech.com 8 Outlet 1U Rack Mount PDU](https://amzn.to/4fhcJZQ) | |

## Server rack

[StarTech.com 4-Post 15U Mobile Open Frame Server Rack](https://amzn.to/4dfhAZY) on casters.

| Item | Notes |
| --- | --- |
| [Iwillink 24 Port Blank Keystone Patch Panel](https://amzn.to/3WhhPg9) | Same keystone setup as the network rack |
| [1U Hinged Vented Blank Panel](https://amzn.to/4d1FhVH) | |
| Dell PowerEdge R630 | Racked, powered off until the rack has its own UPS. See [servers/r630.md](servers/r630.md) |
| Darkrock (Unraid tower) | Sits on a loose plywood top. Retiring in Phase 1. See [servers/darkrock.md](servers/darkrock.md) |

### Elevation today

Top unit heights are as found; confirm the drawer's real height before re-racking.

| U | Today | After Phase 3 |
| --- | --- | --- |
| 15–14 | Drawer | Drawer |
| 13 | Keystone patch panel | Keystone patch panel |
| 12 | 1U shelf | 1U shelf |
| 11 | open | Vented blank |
| 10 | open | **Dell R630** (Proxmox) |
| 9 | Dell R630 (off) | Vented blank |
| 8–7 | open | open, kept free for later |
| 6–3 | open | **45HomeLab X15** (Unraid) |
| 2–1 | CyberPower 1500VA, shared by both racks | **2U rack UPS**, server rack only |
| top | Darkrock on plywood | clear |

## TODO

- [ ] Measure the server rack's post depth, then order the X15's 27″ or 36.4″ rail kit.
- [ ] Rack-mounted UPS for the server rack, so the CyberPower 1500VA only carries the network rack. See [power.md](power.md).
- [ ] Replace the plywood top with a proper top (butcher block?) once Darkrock is gone, instead of the
      navepoint 1U shelf that doesn't give full use of the top.
