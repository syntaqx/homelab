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

![image](https://github.com/user-attachments/assets/ef4b8754-00fa-4c31-b893-4a923144b716)

### TODO

- [Seagate Exos Hard Drive](https://amzn.to/3VXDoSW)
  - Currently only have 8 TB drives, plan to upgrade to larger in the future.
  - I'm limited to 6 SATA ports (2xParity, 2xCache, 2xDisks) - So I'll need a sata expansion card.
- Add a second 1 TB SSD drive to the cache pool

## Plugins

![image](https://github.com/syntaqx/homelab/assets/6037730/7fc8007b-fdf9-450a-98a3-f917d179c87b)

## Shares

![image](https://github.com/syntaqx/homelab/assets/6037730/c62053b1-52f6-4a73-b8e6-d75317b4a86e)

## Docker

![image](https://github.com/syntaqx/homelab/assets/6037730/224c7e9e-d0cf-42c8-bd25-58aa0cd2a25a)

> [!NOTE]
> Traefik is configured to bind to ports `80` and `443` so I can route application traffic through
> it, such as overseerr. To make this possible, Unraid's Management Access is bound to ports
> `8001` and `44301` respectively.

## External Services

- [Cloudflare](https://www.cloudflare.com/)
- [Private Internet Access](https://www.privateinternetaccess.com/)
- [Plex](https://www.plex.tv/)
