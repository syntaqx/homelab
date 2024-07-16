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
- Add a 10G Network Card, currently only have 1G

## Plugins

![image](https://github.com/user-attachments/assets/1a651175-669f-4b07-bc25-606c3d043eae)

## Shares

![image](https://github.com/syntaqx/homelab/assets/6037730/c62053b1-52f6-4a73-b8e6-d75317b4a86e)

## Docker

![image](https://github.com/user-attachments/assets/0daf1c8a-98b9-48a0-b2e6-b02303fb6e20)

> [!NOTE]
> Traefik is configured to bind to ports `80` and `443` so I can route application traffic through
> it, such as overseerr. To make this possible, Unraid's Management Access is bound to ports
> `8001` and `44301` respectively.

## External Services

- [Cloudflare](https://www.cloudflare.com/)
- [Private Internet Access](https://www.privateinternetaccess.com/)
- [Plex](https://www.plex.tv/)
