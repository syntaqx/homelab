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

![image](https://github.com/syntaqx/homelab/assets/6037730/1bc6e777-70d7-49ee-bc75-6faa81f9799d)

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
