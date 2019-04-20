# pi-power-button

Scripts used in the [Pi power button guide](https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi) on howchoo.

## Circuits
If you use Original code
Connect a momentary push button to GPIO 5 and 6 of Raspberry Pi (GPIO 3 and GND)

If you use New code
Connect a momentary push button to GPIO 6 and 12 of Raspberry Pi (GPIO 18 and GND)

## Installation

1. Clone down this repo to your Raspberry Pi git clone https://github.com/masteruan/pi-power-button/
2. chmod +x /script/install
3. Run `script/install` by using ./script/install

## Option
Use new_listen-for-shutdown.py if you want use a different method. Avoid false switch off/on.
Instruction:
1. Connect GPIO 6 and 18 to momentary switch (see the Raspberry Pi pinout)
2. Before the setup script you must delete "listen-for-shutdown.py" file
3. Rename new_listen-for-shutdown.py in "listen-for-shutdown.py"
4. Start the setup script

That's it!
