# Darkrock

The current Unraid storage server: a mid-tower that sits on top of the server rack. It retires in
Phase 1 when its drives move into the [X15](x15.md); after that this page moves to `docs/archive/`.
Read from the Unraid web UI, 2026-11-07.

## Hardware

- __OS:__ Unraid 7, Lifetime license
- __Motherboard:__ ASUS Maximus VIII Hero Alpha
- __CPU:__ Intel Core i7-6700K 4.00GHz
- __Memory:__ [Corsair Vengeance LPX 32GB DDR4 2133MHz](https://www.amazon.com/dp/B0196QNBU4) (max. installable capacity 64GB)
- __GPU:__ NVIDIA GeForce GTX 1080 (Plex transcoding)
- __Case:__ [DARKROCK Classico Storage Master ATX Computer Case Mid Tower](https://amzn.to/4cQ9HdP)
- __Network Card:__ [IO CREST 2.5 Gigabit Ethernet PCI-E NIC](https://amzn.to/4bP6MAA)
- __UPS:__ USB to the server rack's CyberPower OR500LCDRM1U. See [power.md](../power.md)

Drive layout and capacity: [storage.md](../storage.md).

## Shares

| Share | Storage |
| --- | --- |
| media | Array |
| downloads | Cache → Array |
| backup | Array |
| appdata | Cache |
| isos | Array |
| domains | Array |
| system | Array |

## Containers

| Container | Does | State |
| --- | --- | --- |
| Plex (binhex-plexpass) | Media server | running |
| Tautulli | Plex stats | running |
| Seerr (binhex-seerr) | Media requests | running |
| Sonarr (binhex-sonarr) | TV | running |
| Radarr (binhex-radarr) | Movies | running |
| Prowlarr (binhex-prowlarr) | Indexers | running |
| FlareSolverr (binhex-flaresolverr) | Indexer proxy | running |
| DelugeVPN (binhex-delugevpn) | Downloads over PIA | running |
| Unpackerr | Extracts downloads | running |
| AdGuard Home | DNS, paired with [Sentinel](sentinel.md) | running |
| Cloudflared | Cloudflare Tunnel, paired with [Sentinel](sentinel.md) | running |
| Cloudflare DDNS | Dynamic DNS | running |
| MySpeed | Speed tests | stopped |

## Plugins

Appdata Backup, Community Applications, CA Auto Update Applications, Fix Common Problems,
Dynamix System Buttons, Dynamix System Temperature, Nvidia Driver, Unassigned Devices (+ Plus,
Preclear), Unraid Connect.

## Done since 2024

- [x] Seagate Exos upgrades: the array now runs 20 TB parity and three 20 TB data disks.
- [x] Past the 6-SATA-port limit: the array and cache now run 10 drives.
- [x] Replaced the 2024 screenshots with the lists above.
- [ ] ~~Upgrade to a 10G NIC~~: superseded, the X15 ships with 2×10GbE.

## Retiring

When the X15 is up, sell the tower whole or in parts (i7-6700K, Maximus VIII Hero Alpha, 32GB DDR4,
GTX 1080, case).
