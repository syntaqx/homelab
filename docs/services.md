# Services

What runs where. Container and plugin lists live on each server's page.

| Service | Host | Notes |
| --- | --- | --- |
| Plex | [Darkrock](servers/darkrock.md) | GTX 1080 transcoding today; Intel Quick Sync on the X15 |
| Sonarr, Radarr, Prowlarr, Seerr | [Darkrock](servers/darkrock.md) | Library automation and requests |
| DelugeVPN | [Darkrock](servers/darkrock.md) | Downloads over Private Internet Access |
| Tautulli | [Darkrock](servers/darkrock.md) | Plex stats |
| AdGuard Home | [Sentinel](servers/sentinel.md) + [Darkrock](servers/darkrock.md) | DNS, one per server |
| Cloudflare Tunnel | [Sentinel](servers/sentinel.md) + [Darkrock](servers/darkrock.md) | Remote access without open ports |
| Cloudflare DDNS | [Darkrock](servers/darkrock.md) | |
| Proxmox VE | [R630](servers/r630.md) | Phase 3: self-hosted apps, VMs, the occasional game server |

## External

- [Google Fiber](https://fiber.google.com)
- [Cloudflare](https://www.cloudflare.com/)
- [Private Internet Access](https://www.privateinternetaccess.com/)
- [Plex](https://www.plex.tv/)

## TODO

- [x] Replace the 2024 screenshots with a current list of containers and plugins.
- [ ] Decide which apps stay on Unraid and which move to Proxmox.
- [ ] Export the Unraid Docker templates into the repo, scrubbed of passwords and API keys.
