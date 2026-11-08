# Runbook: R630 bring-up

Only after the server rack's UPS upgrade (Phase 2); the current 300 W unit can't carry it.

1. Plug in iDRAC and power on. Update iDRAC, BIOS and firmware (Lifecycle Controller or Dell's update packages).
2. Record CPU model(s) and the network daughter card in [servers/r630.md](../servers/r630.md).
3. If the daughter card is 1GbE-only, swap in a 2×10GbE one. Connect one 10GbE port to the TL-SX1008.
4. Install the two SSDs for VM storage.
5. Install Proxmox VE (no-subscription repository).
6. Add an NFS share on the X15 as a Proxmox backup target; schedule VM backups.
7. Wire the UPS shutdown signal to Proxmox as well as Unraid.
8. Test: shut it down and power it back on from iDRAC.
