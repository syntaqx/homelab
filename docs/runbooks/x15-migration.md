# Runbook: Darkrock → X15

Move the Unraid array from Darkrock into the 45HomeLab X15 without losing data. Unraid identifies
array disks by serial number, not by port, so assignments survive a move to new hardware.

## Before the X15 arrives

1. Preclear the spare 20 TB Exos over USB (Unassigned Devices Preclear plugin).
2. Screenshot **Main**: every disk's slot and serial.
3. Back up the flash drive: **Main → Boot Device → Flash → Flash Backup**. Keep the zip off the server.
4. Note which containers use the GTX 1080 (Plex, most likely). They'll switch to Quick Sync.
5. Decide the boot path. Either:
   - **Carry the flash over.** Plug the current USB flash into the X15 and boot from it; config and
     license come along unchanged.
   - **Use the X15's own install.** It ships with Unraid and a lifetime license on its NVMe. Restore
     your config from the flash backup onto it, and check with Unraid support how to handle the old
     license before you do.

## Day one

1. Rack the X15 on its rails, directly above the UPS. Don't install drives until it's racked.
2. Through IPMI: update the BIOS and CPU microcode, then run a memory test overnight.
3. Run one 10GbE port to the TL-SX1008. The MAC address changes, so update any DHCP reservation
   or static IP for the server.

## Move the array

1. On Darkrock: stop all containers and VMs, set the array to not auto-start, stop the array, shut down.
2. Move the disks into the X15:
   - Bays 01–02: Parity, Parity 2
   - Bays 03–08: Disk 1–6
   - Bays 09–10: cache SSDs in the 2.5″ adapters
3. Boot the X15. On **Main**, confirm every disk sits in its original slot by serial against your screenshot.
4. Start the array. Run a parity check (read-only) before trusting it.

## After

1. Add the precleared spare in bay 11 as Disk 7. A precleared disk joins without another clear: 104 TB.
2. Remove the NVIDIA driver plugin; pass `/dev/dri` to Plex and turn on hardware transcoding.
3. Set the array to auto-start again; start containers one by one.
4. Update [storage.md](../storage.md) and [racks.md](../racks.md); move `servers/darkrock.md` to `docs/archive/`.
