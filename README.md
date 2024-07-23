# homelab

My homelab.

## Network Rack

- [Tecmojo 12U Open Frame Network Rack](https://amzn.to/3y5hepV)
- []StarTech.com 8 Outlet Horizontal 1U Rack Mount PDU)(https://amzn.to/4fhcJZQ)
- [Iwillink 24 Port Blank Keystone Patch Panel)(https://amzn.to/3WhhPg9)
  - [VCE 20-Pack Blank Keystone Jack Inserts)(https://amzn.to/3yhkaj5)
- [iwillink 10Gbps CAT7 Coupler RJ45 Keystone Shielded Coupler)(https://amzn.to/46ocRTC)
- [Patch Cables Cat8 0.5ft (10 Pack)](https://amzn.to/3WdKXVv)

## Tower

### Hardware

- __Motherboard:__ ASUS Maximus VIII Hero Alpha
- __CPU:__ Intel Core i7-6700K 4.00GHz
- __Memory:__ 32GB DDR4 (max. installable capacity 64GB)
- __GPU:__ NVIDIA GeForce GTX 1080
- __Case:__ [DARKROCK Classico Storage Master ATX Computer Case Mid Tower](https://amzn.to/4cQ9HdP)
- __Network Card:__ [IO CREST 2.5 Gigabit Ethernet PCI-E NIC](https://amzn.to/4bP6MAA)

### Software

- __OS:__ Unraid 6.X

## Storage

![image](https://github.com/user-attachments/assets/7c6e6a46-aca4-43e7-ad47-4714d4f8b4a2)

### TODO

- [Seagate Exos Hard Drive](https://amzn.to/3VXDoSW)
  - Currently only have 8 TB drives, plan to upgrade to larger in the future.
  - I'm limited to 6 SATA ports (2xParity, 2xCache, 2xDisks) - So I'll need a sata expansion card.
- Upgrade to a 10G NIC

## Plugins

![image](https://github.com/user-attachments/assets/1a651175-669f-4b07-bc25-606c3d043eae)

## Shares

![image](https://github.com/syntaqx/homelab/assets/6037730/c62053b1-52f6-4a73-b8e6-d75317b4a86e)

## Docker

![image](https://github.com/user-attachments/assets/580af1f9-1bca-4583-a503-54e8a89c971d)

> [!NOTE]
> Traefik is configured to bind to ports `80` and `443` so I can route application traffic through
> it, such as overseerr. To make this possible, Unraid's Management Access is bound to ports
> `8001` and `44301` respectively.

## External Services

- [Cloudflare](https://www.cloudflare.com/)
- [Private Internet Access](https://www.privateinternetaccess.com/)
- [Plex](https://www.plex.tv/)
