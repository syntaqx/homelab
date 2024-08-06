# homelab

My homelab.

![image](https://github.com/user-attachments/assets/13682bba-4684-465f-889a-8a07bc100468)

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
- [Navepoint iU 19-Inch Rack Mount Server Shelf with Adjustable Depth](https://amzn.to/4dt4bNZ)
- [Iwillink 24 Port Blank Keystone Patch Panel](https://amzn.to/3WhhPg9)
  - [VCE 20-Pack Blank Keystone Jack Inserts](https://amzn.to/3yhkaj5)
  - [iwillink 10Gbps CAT7 Coupler RJ45 Keystone Shielded Coupler](https://amzn.to/46ocRTC)
  - [Patch Cables Cat8 0.5ft (10 Pack)](https://amzn.to/3WdKXVv)
- [1U Hinged Vented Rack Mount Blank Panel Spacer](https://amzn.to/4d1FhVH)

#### TODO

- Rack mounted battery UPS for both racks, they're currently sharing an old CyberPower 1500va
  - Maybe this one? https://www.amazon.com/dp/B0016P8OII/

## Servers

### "Darkrock"

#### Hardware

- __OS:__ Unraid 6.X
- __Motherboard:__ ASUS Maximus VIII Hero Alpha
- __CPU:__ Intel Core i7-6700K 4.00GHz
- __Memory:__ 32GB DDR4 2133MHz (max. installable capacity 64GB)
- __GPU:__ NVIDIA GeForce GTX 1080
- __Case:__ [DARKROCK Classico Storage Master ATX Computer Case Mid Tower](https://amzn.to/4cQ9HdP)
- __Network Card:__ [IO CREST 2.5 Gigabit Ethernet PCI-E NIC](https://amzn.to/4bP6MAA)

#### Storage

![image](https://github.com/user-attachments/assets/1b69ff5d-cdcc-4048-8a7e-289aadc57f7c)

#### TODO

- [Seagate Exos Hard Drive](https://amzn.to/3VXDoSW)
  - Currently only have 8 TB drives, plan to upgrade to larger in the future.
  - I'm limited to 6 SATA ports (2xParity, 2xCache, 2xDisks) - So I'll need a sata expansion card.
- Upgrade to a 10G NIC

#### Plugins

![image](https://github.com/user-attachments/assets/1a651175-669f-4b07-bc25-606c3d043eae)

#### Shares

![image](https://github.com/user-attachments/assets/b40490fd-06e6-4a77-a33b-f2b301e06517)

#### Docker

![image](https://github.com/user-attachments/assets/92e291de-e6e9-4961-a8fb-9cebb408cf6f)

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
