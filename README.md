# homelab

My home lab, project, builds, etc.

## Tower

### Hardware

- __Motherboard:__ ASUS Maximus VIII Hero Alpha
- __CPU:__ Intel Core i7-6700K 4.00GHz
- __Memory:__ 32GB DDR4 (max. installable capacity 64GB)
- __GPU:__ NVIDIA GeForce GTX 1080

### Software

- __OS:__ Unraid 6.1.79

## Storage

### Array Devices

| Device | Identification                                       | Capacity |
|--------|------------------------------------------------------|----------|
| Parity | ST-2000DX001-1NS164_Z4Z5PQKQ - 2 TB (sdc)            | 2 TB     |
| Disk 1 | Samsung_SSD_850_PRO_1TB_S252NX0H504724B - 1 TB (sdb) | 1 TB     |

### Pool Devices

| Device | Identification                                           | Capacity |
|--------|----------------------------------------------------------|----------|
| Cache  | Samsung_SSD_840_EVO_250GB_S1DBNSBFA84493X - 250 GB (sdd)	| 250 GB  |

#### Boot Device

| Device | Identification                                           | Capacity |
|--------|----------------------------------------------------------|----------|
| Flash  | Silicon-Power32G - 32.2 GB (sda)                         | 32.2 GB  |

The planned modifications for this as I have the budget for it are:

- 2x [Seagate IronWolf Pro 14 TB Enterprise NAS Internal HDD](https://www.amazon.com/dp/B0B94P481H/)
- Swap the Parity and Disk 1 drives for the new 14 TB drives
- Swap the Cache drive to the Samsung 850 Pro 1 TB drive
- Add a second 1 TB drive to the cache pool
- Add the ST-2000DX001-1NS164_Z4Z5PQKQ 2 TB drive to the pool
- Throw away the Samsung 840 EVO 250 GB drive

## Plugins

- [Community Applications](https://forums.unraid.net/topic/38582-plug-in-community-applications/)
- [CPU Statistics](https://forums.unraid.net/topic/38582-plug-in-community-applications/)
- [Nvidia Driver](https://forums.unraid.net/topic/38582-plug-in-community-applications/)
- [User Scripts](https://forums.unraid.net/topic/38582-plug-in-community-applications/)

## Shares

- `appdata` - Array
- `domains` - Cache ← Array
- `downloads` - Cache ← Array
- `downloads` - Cache ← Array
- `isos` - Cache ← Array
- `media` - Array
- `system` - Cache ← Array
- `tmp` - Array

Most of the shares are meant to be set to prefer cache, but given my current
storage setup, I have things set up this way.

## Apps

The following are the apps I have installed on my Unraid server, in order of
installation:

- [Pihole-DoT-DoH](https://hub.docker.com/r/testdasi/pihole-dot-doh)
- [binhex-plexpass](https://hub.docker.com/r/binhex/arch-plexpass)
- [binhex-delugevpn](https://hub.docker.com/r/binhex/arch-delugevpn
- [binhex-flaresolverr](https://hub.docker.com/r/binhex/arch-flaresolverr)
- [binhex-proxarr](https://hub.docker.com/r/binhex/arch-proxarr)
- [binhex-radarr](https://hub.docker.com/r/binhex/arch-radarr)
- [binhex-sonarr](https://hub.docker.com/r/binhex/arch-sonarr)
- [tdarr](https://hub.docker.com/r/haveagitg/tdarr)
- [tdarr_node](https://hub.docker.com/r/haveagitg/tdarr_node)
- [binhex-overseerr](https://hub.docker.com/r/binhex/arch-overseerr)
- [traefik](https://hub.docker.com/r/traefik/traefik)
- [Cloudflare-DDNS](https://github.com/oznu/docker-cloudflare-ddns)

![image](https://github.com/syntaqx/homelab/assets/6037730/357230b9-92a5-4874-bb83-df0b4e9a31f8)

## Services

- [Cloudflare](https://www.cloudflare.com/)
- [Private Internet Access](https://www.privateinternetaccess.com/)
- [Plex](https://www.plex.tv/)
