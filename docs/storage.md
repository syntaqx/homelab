# Storage

Unraid 7 array on Darkrock today, moving to the 45HomeLab X15 in Phase 1. Figures are a snapshot
from 2026-11-07.

## Array

84 TB usable, 66.2 TB used (79%), 17.8 TB free. All XFS.

| Slot | Drive | Size | Used |
| --- | --- | --- | --- |
| Parity | Seagate Exos ST20000NM004E | 20 TB | — |
| Parity 2 | Seagate Exos ST20000NM004E | 20 TB | — |
| Disk 1 | Seagate Exos ST8000NM0045 | 8 TB | 5.51 TB |
| Disk 2 | Seagate Exos ST8000NM0045 | 8 TB | 5.52 TB |
| Disk 3 | Seagate Exos ST8000NM0045 | 8 TB | 5.51 TB |
| Disk 4 | Seagate Exos ST20000NM004E | 20 TB | 17.5 TB |
| Disk 5 | Seagate Exos ST20000NM004E | 20 TB | 17.0 TB |
| Disk 6 | Seagate Exos ST20000NM004E | 20 TB | 15.1 TB |

On hand, not yet installed: **1× Exos 20 TB spare**. It waits for the X15's first free bay rather
than replacing an 8 TB disk in Darkrock (a free bay adds 20 TB with no rebuild; a swap adds 12 TB and
rebuilds a disk). Preclear it ahead of time over USB with the Unassigned Devices Preclear plugin.

Last parity check: 2026-10-05, 0 errors, 1 day 9 hours at 167.8 MB/s. Drives run 30–36 °C.

## Pools

| Pool | Devices | Filesystem | Size | Used |
| --- | --- | --- | --- | --- |
| Cache | Samsung 850 PRO 1TB + Samsung 870 EVO 1TB (mirror) | btrfs | 994 GB | 193 GB |

## Boot

Silicon Power 32 GB USB 3.0 flash (vfat). No internal boot configured yet; the X15 ships with a
1 TB NVMe boot drive, so decide during migration whether to keep booting from flash or move to
internal boot. See [runbooks/x15-migration.md](runbooks/x15-migration.md).

## Growth plan on the X15

The X15 has 15 direct-wired 3.5″ bays on an LSI 9400-16i HBA, plus 4 M.2 slots (one holds the boot
drive).

| Bays | After migration |
| --- | --- |
| 01–02 | Parity, Parity 2 (20 TB) |
| 03–05 | Disk 1–3 (8 TB, swap candidates) |
| 06–08 | Disk 4–6 (20 TB) |
| 09–10 | Cache SSDs in 2.5″ adapters |
| 11 | Disk 7, the spare 20 TB |
| 12–15 | open |

| Step | Array size | How |
| --- | --- | --- |
| Today | 84 TB | — |
| Spare into bay 11 | 104 TB | day one, no rebuild |
| Fill bays 12–15 | 184 TB | +20 TB per drive, no rebuild |
| Swap 3× 8 TB for 20 TB | 220 TB | +12 TB each, one rebuild each |
| Move cache to M.2 | up to 260 TB | frees bays 09–10 for two more data disks |

Parity is 20 TB, so no data disk can be bigger than 20 TB until a larger parity disk goes in first.
Sizes are raw array space before filesystem overhead.
