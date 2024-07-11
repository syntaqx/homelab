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

- ![image](https://github.com/syntaqx/homelab/assets/6037730/dba1f98c-5ff8-4045-a9f0-807d2873ac20)

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

![image](https://github.com/syntaqx/homelab/assets/6037730/4f7f941c-d518-488c-af7c-f6ceb67c337f)

> [!NOTE]
> Traefik has been configured to use port `80` and `443` so I can route applications, such as overseerr externally.
> To make this possible, I changed the Unraid Management Access to use ports `8001` and `44301`

## External Services

- [Cloudflare](https://www.cloudflare.com/)
- [Private Internet Access](https://www.privateinternetaccess.com/)
- [Plex](https://www.plex.tv/)
