# syntaqx/homelab

Documentation for Chase's home network and basement racks. Markdown only, plus generated diagrams.

## Layout

- `README.md`: overview, network diagram, links into `docs/`. Keep it short.
- `docs/`: one page per area (racks, servers, storage, network, power, services, roadmap, runbooks).
- `assets/network-{dark,light}.svg`: the README diagram. Generated; never hand-edit.
- `scripts/network_diagram.py`: the diagram's source. Run `python3 scripts/network_diagram.py assets`.
- `assets/plans/`: PNG/PDF exports of the build-plan sheets (Claude Design canvas on claude.ai).

## Conventions

- When hardware changes, update the affected `docs/` page, the README "At a glance" table, and the
  diagram script in the same commit.
- Prices carry an "as of" date. Label planning estimates "est."
- Never commit secrets: no passwords, API keys, license keys or flash backups. Scrub Docker templates
  before adding them.
- Retired hardware moves to `docs/archive/` rather than being deleted.

## Design system

Used by the network diagram and the build-plan sheets.

- Colors (dark): ground #0A1A2B, accent #00D1CA (syntaqx teal), caution #F2B33D, text #E4F3F2, muted #93B4B6
- Colors (light): ground #F4F8F8, accent #007873, caution #9A5F00, text #0A1A2B, muted #4A6670
- Typography: Space Grotesk for headings, IBM Plex Mono for labels and body
- Style: blueprint drafting sheet on a 20/100 px grid, square corners, dashed lines for racks and
  planned or logical things
