# TOOLS.md - Local Notes

Short, durable notes that make external tools work reliably in this
particular setup: device nicknames, host aliases, preferred voices, and
environment-specific quirks. Skills describe how tools work in general; this
file holds only what is unique here. Leave it empty until there is something
worth recording.

## Gateway laptop terminal (Lubuntu, ollama >>> prompt)

- Scrolling up with mouse wheel / touchpad goes blank. Shift+PageUp works to scroll back through a Spark reply (confirmed 2026-11-04). Use that to capture the top half of a long reply before sending the next prompt.

## Gateway flash drive (32GB onn, /media/cliff/onn. Disk)
- **FAT32 (vfat) — 4GB max file size.** Big bundles must be split into ≤2GB chunks (`split -b 2000M`) and md5-verified per part on the Gateway side. Reassemble with `cat *.part-* > file`. (Learned Nov 17: a 6.1GB bundle died at exactly 4.0GB.)

## scrcpy — old Moto on the Gateway (2026-11-12)
- apt scrcpy 1.25 is too old for the Moto's Android — crashes with NoSuchMethodException on SurfaceControl.createDisplay. Use snap scrcpy 5.0.1: `sudo apt remove scrcpy`, `sudo snap install scrcpy`, `sudo snap connect scrcpy:raw-usb` (joystick/Gamepad warning is ignorable, press ENTER). Bash may hash the old /usr/bin/scrcpy — run `hash -r` if it says no such file. Works clean Nov 12: moto g 5G - 2024 mirrored, no cracks/blobs on the laptop screen, USB debugging ON.

## Hearth bottom panel (LXQt) — taskbar
- 2026-11-25: minimize made windows vanish — the bottom panel's `taskbar` plugin was missing from `~/.config/lxqt/panel.conf` (plugins list had no `taskbar`). Windows weren't closing, just hidden (Alt+Tab brings them back). Fix: back up panel.conf, add `taskbar` to the plugins list after `showdesktop`, add a `[taskbar]` section (alignment=Left, type=taskbar), kill lxqt-panel and restart it with the session env (DISPLAY=:0, DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus, XAUTHORITY from /proc/<pid>/environ). Backup: `~/.config/lxqt/panel.conf.bak-2026-11-25-taskbar`. Verify one lxqt-panel process owns the manager selection after restart.
