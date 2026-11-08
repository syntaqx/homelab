# Network

The diagram at the top of the [README](../README.md) is the picture; this page is the detail behind it.

## Internet

- [Google Fiber](https://fiber.google.com), 5 Gig (want 8, but we'll wait for a bit)
- GFiber Fiber Jack → GFiber Wi-Fi 6E Router, with 2× GFiber Wi-Fi 6E Extenders around the house

## Switching

TP-Link TL-SX1008 in the network rack: 8 ports, 10G/Multi-Gig, unmanaged. Every wired link in the
basement meets here through the keystone patch panels.

Because it's unmanaged:

- No VLANs. The X15's IPMI port and the R630's iDRAC sit on the main LAN; leave them unplugged when
  they aren't needed if that matters.
- No link aggregation. One 10GbE link per server is enough.

## Links

| From | To | Speed | Notes |
| --- | --- | --- | --- |
| GFiber router | TL-SX1008 | Multi-Gig | Uplink for the house runs |
| GFiber router | Server-rack 2.5G switch | 2.5GbE | Serves darkrock and the R630 today |
| Darkrock | Server-rack 2.5G switch | 2.5GbE | IO CREST NIC; retires in Phase 1 |
| X15 | TL-SX1008 | 10GbE | Phase 1 · Intel X550-T2, one port in use, via the keystone panels |
| R630 | TL-SX1008 | 10GbE | Phase 3 · depends on its daughter card |
| Sentinel | TL-SX1008 | 2.5GbE | DNS (AdGuard Home), Cloudflare Tunnel |
| X15 IPMI / R630 iDRAC | Server-rack 2.5G switch | 1GbE | Management |

## Devices by room

Same as the diagram, in text so changes show up in diffs.

| Room | Wired | Wi-Fi |
| --- | --- | --- |
| Server room · network rack | Fiber Jack → GFiber 6E Router → TP-Link TL-SX1008 → sentinel.local | |
| Server room · server rack | 2.5G switch (off the router) → darkrock.local, r630.local | |
| Bedroom 2 | GUEST desktop → TL-SX1008 | |
| Bedroom 3 (office) | 2.5G switch → TL-SX1008, serving SYNTAQX desktop, Hue Bridge, SureFlap Bridge, GFiber 6E AP | Chromecast |
| Bedroom 4 | MAXXI desktop → TL-SX1008 | |
| Family room | GFiber 6E AP → TL-SX1008; Chromecast wired to the AP | |
| Bedroom 1 | | Chromecast |
| Master bedroom | | Chromecast |
| Garage | | Chromecast, myQ Smart Garage |
| Outdoors | | Nest Outdoor Camera, Nest Doorbell |

## Remote access and services

- [Cloudflare](https://www.cloudflare.com/)
- [Private Internet Access](https://www.privateinternetaccess.com/)
- [Plex](https://www.plex.tv/)
