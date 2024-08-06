# homelab

![image](https://github.com/user-attachments/assets/c98a602f-1b20-45f9-97ab-fa5cf45f8159)

## Racks

### Network Rack

- [Tecmojo 12U Open Frame Network Rack](https://amzn.to/3y5hepV)
- [Iwillink 24 Port Blank Keystone Patch Panel](https://amzn.to/3WhhPg9)
  - [VCE 20-Pack Blank Keystone Jack Inserts](https://amzn.to/3yhkaj5)
  - [iwillink 10Gbps CAT7 Coupler RJ45 Keystone Shielded Coupler](https://amzn.to/46ocRTC)
  - [Patch Cables Cat8 0.5ft (10 Pack)](https://amzn.to/3WdKXVv)
- [MokerLink 8 Port 10Gbps Ethernet Switch](https://amzn.to/4cdCKqy)
- [1U Hinged Vented Rack Mount Blank Panel Spacer](https://amzn.to/4d1FhVH)
- [StarTech.com 8 Outlet Horizontal 1U Rack Mount PDU](https://amzn.to/4fhcJZQ)

#### Networking Equiptment

- GFiber Fiber Jack
- GFiber Wi-Fi 6E Router
- 2x GFiber Wi-Fi 6E Extender

### Server Rack

- [StarTech.com 4-Post 15U Mobile Open Frame Server Rack](https://amzn.to/4dfhAZY)
  - Plywood Top
- [Iwillink 24 Port Blank Keystone Patch Panel](https://amzn.to/3WhhPg9)
  - [VCE 20-Pack Blank Keystone Jack Inserts](https://amzn.to/3yhkaj5)
  - [iwillink 10Gbps CAT7 Coupler RJ45 Keystone Shielded Coupler](https://amzn.to/46ocRTC)
  - [Patch Cables Cat8 0.5ft (10 Pack)](https://amzn.to/3WdKXVv)
- [1U Hinged Vented Rack Mount Blank Panel Spacer](https://amzn.to/4d1FhVH)

#### TODO

- Would like to make a custom top from butcher block or something for this instead of using
  the navepoint 1U shelf which doesn't give me full use of the top.
- Rack mounted battery UPS for both racks, they're currently sharing an old CyberPower 1500va
  - Maybe this one? https://www.amazon.com/dp/B0016P8OII/

## Servers

### "Darkrock"

#### Hardware

- __OS:__ Unraid 6.12.11
- __Motherboard:__ ASUS Maximus VIII Hero Alpha
- __CPU:__ Intel Core i7-6700K 4.00GHz
- __Memory:__ [Corsair Vengeance LPX 32GB DDR4 2133MHz](https://www.amazon.com/dp/B0196QNBU4) (max. installable capacity 64GB)
- __GPU:__ NVIDIA GeForce GTX 1080
- __Case:__ [DARKROCK Classico Storage Master ATX Computer Case Mid Tower](https://amzn.to/4cQ9HdP)
- __Network Card:__ [IO CREST 2.5 Gigabit Ethernet PCI-E NIC](https://amzn.to/4bP6MAA)

#### Storage

![image](https://github.com/user-attachments/assets/b7906515-8e5e-47dc-a1f8-9a8e40791b9e)

##### TODO

- [Seagate Exos Hard Drive](https://amzn.to/3VXDoSW)
  - Currently only have 8 TB drives, plan to upgrade to larger in the future.
  - I'm limited to 6 SATA ports (2xParity, 2xCache, 2xDisks) - So I'll need a sata expansion card.
- Upgrade to a 10G NIC

#### Shares

![image](https://github.com/user-attachments/assets/b6e0e4cc-e1e7-497d-a6f1-ea62b66b3b92)

#### Plugins

![image](https://github.com/user-attachments/assets/22dd0e1b-fd3f-47a5-9151-d55cbaffda74)

#### Docker

![image](https://github.com/user-attachments/assets/2280816f-5a7c-4446-bcb2-ef01b1bc4592)

### "R630"

> [!NOTE]
> The R630 is still currently in progress, as I'm not going to boot it up until I have a separate
> UPS for this rack - The power draw from both servers would bend my network to its knees if the
> power went out.

- Dell PowerEdge R630
- __Memory:__ 256GB DDR4 1866MHz

#### Storage

- 3x [Dell 1.2TB 10K 12GB/s SAS 2.5" HDD](https://amzn.to/3WtA3v0)

Still want 2x SSDs for cache and since SAS drives are so expensive I'll probably fill the box with
1.2TBs. This will primarily be a self-hosting box for my apps and maybe a minecraft server or
whatever.

## External Services

- [Google Fiber](https://fiber.google.com) - 5 gig (want 8, but we'll wait for a bit)
- [Cloudflare](https://www.cloudflare.com/)
- [Private Internet Access](https://www.privateinternetaccess.com/)
- [Plex](https://www.plex.tv/)

## Basement

![image](https://github.com/user-attachments/assets/243164f1-f375-400a-ba96-d2f22d7170b5)
