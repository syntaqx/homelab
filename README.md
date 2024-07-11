# homelab

My home lab, project, builds, etc.

![image](https://github.com/syntaqx/homelab/assets/6037730/ceeb7686-1565-4e00-b213-617165db3bec)

> [!NOTE]
> Real photo coming once my case arrives and I rebuild the previous one (and clean it)

## Tower

### Hardware

- __Motherboard:__ ASUS Maximus VIII Hero Alpha
- __CPU:__ Intel Core i7-6700K 4.00GHz
- __Memory:__ 32GB DDR4 (max. installable capacity 64GB)
- __GPU:__ NVIDIA GeForce GTX 1080
- __Case:__ [DARKROCK Classico Storage Master ATX Computer Case Mid Tower](https://amzn.to/4cQ9HdP)

### Software

- __OS:__ Unraid 6.X

## Storage

### Array Devices

| Device | Identification                                         | Capacity |
|--------|--------------------------------------------------------|----------|
| Parity | `ST-2000DX001-1NS164_Z4Z5PQKQ - 2 TB (sdc)`            | 2 TB     |
| Disk 1 | `Samsung_SSD_850_PRO_1TB_S252NX0H504724B - 1 TB (sdb)` | 1 TB     |

### Pool Devices

| Device | Identification                                             | Capacity |
|--------|------------------------------------------------------------|----------|
| Cache  | `Samsung_SSD_840_EVO_250GB_S1DBNSBFA84493X - 250 GB (sdd)`	| 250 GB  |

#### Boot Device

| Device | Identification                                             | Capacity |
|--------|------------------------------------------------------------|----------|
| Flash  | `Silicon-Power32G - 32.2 GB (sda)`                         | 32.2 GB  |

The planned modifications for this that I have budgetted for are:

- Swap the USB boot device to a smaller (actually 32GB) drive, it's currently a 64GB formatted with FAT32
- [Seagate Exos Hard Drive](https://amzn.to/3VXDoSW) - At least 12 TB, maybe larger depending on budget.
  - I'm limited to 6 SATA ports (1 for Parity, 5 disks), but 60+ TB should be enough until I build a dedicated NAS
- Swap the Parity & Array drives for the new higher capacity drives
- Swap the Cache drive to the `Samsung 850 Pro 1 TB` drive
- Add a second 1 TB SSD drive to the cache pool
- Thow away the `ST-2000DX001-1NS164_Z4Z5PQKQ 2 TB` and `Samsung 840 EVO 250 GB` drives, they're starting to fail

## Plugins

![image](https://github.com/syntaqx/homelab/assets/6037730/7fc8007b-fdf9-450a-98a3-f917d179c87b)

## Shares

![image](https://github.com/syntaqx/homelab/assets/6037730/c62053b1-52f6-4a73-b8e6-d75317b4a86e)

## Docker

![image](https://github.com/syntaqx/homelab/assets/6037730/b596cd9c-0292-41d1-9bfc-1609a4d06741)

> [!NOTE]
> Traefik is configured to bind to ports `80` and `443` so I can route application traffic through
> it, such as overseerr. To make this possible, Unraid's Management Access is bound to ports
> `8001` and `44301` respectively.

## External Services

- [Cloudflare](https://www.cloudflare.com/)
- [Private Internet Access](https://www.privateinternetaccess.com/)
- [Plex](https://www.plex.tv/)
