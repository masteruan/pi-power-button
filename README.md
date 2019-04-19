# pi-power-button

Scripts used in the [Pi power button guide](https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi) on howchoo.

## Circuits
1. Connect a momentary push button to GPIO 5 and 6 of Raspberry Pi (GPIO 3 and GND)

## Installation

1. Clone down this repo to your Raspberry Pi git clone https://github.com/masteruan/pi-power-button/
2. chmod +x /script/install
3. Run `script/install` by using ./script/install

## Option
Use new_listen-for-shutdown.py if you want use a different method. Avoid false switch off/on.
Instruction:
1. Before the setup script you must delete "listen-for-shutdown.py" file
2. Rename new_listen-for-shutdown.py in "listen-for-shutdown.py"
3. Start the setup script

That's it!
