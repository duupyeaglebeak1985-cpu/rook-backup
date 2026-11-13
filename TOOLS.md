# TOOLS.md - Local Notes

Short, durable notes that make external tools work reliably in this
particular setup: device nicknames, host aliases, preferred voices, and
environment-specific quirks. Skills describe how tools work in general; this
file holds only what is unique here. Leave it empty until there is something
worth recording.

## Gateway laptop terminal (Lubuntu, ollama >>> prompt)

- Scrolling up with mouse wheel / touchpad goes blank. Shift+PageUp works to scroll back through a Spark reply (confirmed 2026-11-04). Use that to capture the top half of a long reply before sending the next prompt.

## scrcpy — old Moto on the Gateway (2026-11-12)
- apt scrcpy 1.25 is too old for the Moto's Android — crashes with NoSuchMethodException on SurfaceControl.createDisplay. Use snap scrcpy 5.0.1: `sudo apt remove scrcpy`, `sudo snap install scrcpy`, `sudo snap connect scrcpy:raw-usb` (joystick/Gamepad warning is ignorable, press ENTER). Bash may hash the old /usr/bin/scrcpy — run `hash -r` if it says no such file. Works clean Nov 12: moto g 5G - 2024 mirrored, no cracks/blobs on the laptop screen, USB debugging ON.
