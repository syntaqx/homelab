# Sentinel

The network server: a mini PC in the network rack that keeps DNS and remote access up independently
of the storage server. Runs Unraid with no array, just a single NVMe pool. Read from the Unraid web
UI, 2026-11-07.

## Hardware

- __Model:__ GMKtec Mini PC N100
- __CPU:__ Intel N100 (4 cores)
- __Memory:__ 8 GB DDR4
- __Storage:__ 256 GB NVMe pool (xfs)
- __Boot:__ Transcend JetFlash 16 GB USB
- __Network:__ 2.5GbE
- __OS:__ Unraid 7, Starter license
- __UPS:__ USB to the network rack's CyberPower OR700LCDRM1U. See [power.md](../power.md)

## Containers

| Container | Does |
| --- | --- |
| AdGuard Home | DNS and ad blocking |
| Cloudflared | Cloudflare Tunnel for remote access |

Darkrock runs the same two containers, so DNS and the tunnel survive either server going down.

## Plugins

Community Applications, CA Auto Update Applications, Fix Common Problems, Dynamix System Buttons,
Unassigned Devices (+ Plus, Preclear), Unraid Connect.
