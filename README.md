# PicoHID-Scripter
A GUI tool that generates CircuitPython HID scripts from mnemonics for Raspberry Pi Pico.

# Credits
The mnemoics used in this tool is heavily inspired by <a href="https://github.com/hak5">Hak5</a> Ducky Script.<br>

# Demo Video

https://github.com/wirebits/PicoHID-Scripter/assets/159493381/bbdf189b-318c-45b6-afa4-1aa63fe0a0d9

# Setup and Installation of Circuit Python
1. Make sure the python is installed on your system (Windows/Linux/MacOS).<br>
2. Download Circuit Python <b>.uf2</b> file for Raspberry Pi Pico from <a href="https://downloads.circuitpython.org/bin/raspberry_pi_pico/en_US/adafruit-circuitpython-raspberry_pi_pico-en_US-8.2.10.uf2">here</a>.<br>
3. Connect Raspberry Pi Pico with a USB cable.<br>
4. Press and hold the bootsel button and connect to the PC/Laptop.<br>
-When it connects, then Raspberry Pi Pico show as a removable storage device named ```RPI-RP2```.<br>
-When ```RPI-RP2``` is showing, then release the bootsel button.<br>
5. Copy the uf2 file in the ```RPI-RP2```.<br>
-When it is copied, then it disconnects automatically and reconnect as ```CIRCUITPY```.<br>
Means circuit python is successfully flashed in the Raspberry Pi Pico.
6. Open ```CIRCUITPY```.<br>
-There are two important things in it : ```lib``` folder and ```code.py``` file<br>
7. Download Adafruit CircuitPython Bundle from <a href="https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20240301/adafruit-circuitpython-bundle-8.x-mpy-20240301.zip">here</a>.<br>
8. Extarct the ZIP file.<br>
9. Copy ```adafruit_hid``` folder in the ```lib``` folder of ```CIRCUITPY```.<br>
10. Done! Now, Raspberry Pi Pico is ready to use as a USB Rubber Ducky.

# Supported Boards
- Raspberry Pi Pico
- Waveshare RP2040 Zero

# Mnemonic Table
<table>
 <tr>
  <th>Mnemonics</th>
  <th>Description</th>
  <th>Example</th>
 </tr>
 <tr>
  <th>TIME</th>
  <th>It adds the <i>time</i> library in the code.</th>
  <th>Just type TIME</th>
 </tr>
 <tr>
  <th>BOARD</th>
  <th>It adds the <i>board</i> library in the code.</th>
  <th>Just type BD</th>
 </tr>
 <tr>
  <th>DGIO</th>
  <th>It adds the <i>digitalio</i> library in the code.</th>
  <th>Just type DGIO</th>
 </tr>
 <tr>
  <th>HID</th>
  <th>It adds the <i>usb_hid</i> library in the code.</th>
  <th>Just type HID</th>
 </tr>
 <tr>
  <th>HLIB</th>
  <th>It adds the <i>Keycode</i>, <i>Keyboard</i> and <i>KeyboardLayoutUS</i> libaries in the code.</th>
  <th>Just type HLIB</th>
 </tr>
 <tr>
  <th>KYBD</th>
  <th>It create objects for keycode and keyboard layout in the code.</th>
  <th>Just type KYBD</th>
 </tr>
 <tr>
  <th>PIN</th>
  <th>It add pin declaration in the code.</th>
  <th>Just type PIN</th>
 </tr>
 <tr>
  <th>LED</th>
  <th>It turns on/off the led in the code.<br>Values are ON and OFF.</th>
  <th>LED ON</th>
 </tr>
 <tr>
  <th>WAIT</th>
  <th>It add time in the code.<br>Time is in milliseconds.<br>1000 ms = 1 second.</th>
  <th>WAIT 1000</th>
 </tr>
 <tr>
  <th>TYPE</th>
  <th>It add text want to type in the code.</th>
  <th>TYPE Hello World!</th>
 </tr>
 <tr>
  <th>SCODE</th>
  <th>It press and release the key(s) immediately.</th>
  <th>SCODE A</th>
 </tr>
 <tr>
  <th>PCODE</th>
  <th>It press and hold the key(s) and release all key(s).</th>
  <th>PCODE S</th>
 </tr>
</table>

# Example
Mnemonic for Open Notepad and Type

```
TIME
HID

HLIB

KYBD

PCODE GUI R
WAIT 1000
TYPE notepad
WAIT 1000
SCODE ENTER
WAIT 1000
TYPE This is a test for Raspberry Pi Pico script developed by PicoHID Scripter!
```
after click on ```Convert``` button, the circuit python script of the following mnemonic is :<br>

```
import time
import usb_hid

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

kbd.press(Keycode.GUI, Keycode.R)
kbd.release_all()
time.sleep(1.0)
layout.write("notepad")
time.sleep(1.0)
kbd.send(Keycode.ENTER)
time.sleep(1.0)
layout.write("This is a test for Raspberry Pi Pico script developed by PicoHID Scripter!")
```
Just copy this code and paste it in the ```code.py``` file in the ```CIRCUITPY```.<br>
# Tested Systems
The tool is currently tested on : <br>
1. Windows (10)<br>
2. Kali Linux<br>
The testing is going on different systems.

# Install and Run
1. Download or Clone the Repository.<br>
2. Open the folder and just double click on PicoHIDScripter.py file.<br>
3. Type the mnemonics in the left window.<br>
4. Click on ```Convert``` button to get corresponding circuit python script.<br>
5. Click on ```Copy``` button to copy the circuit python script to the clipboard.<br>
6. Paste the code in the ```code.py``` file in the ```CIRCUITPY```.<br>
-Be Careful! As it is saved the script start executing.<br>
-To code Raspberry Pi Pico, use Thonny IDE.<br>

# Start/Stop the Raspberry Pi Pico
1. If want to stop Raspberry Pi Pico from execution, then connect the Male-To-Male jumper wires as shown in image below : <br>

![RPIPICO](https://github.com/wirebits/PicoHID-Scripter/assets/159493381/1be784c2-cc24-48e0-baa8-d3b94bc7646e)

2. If want to start again the execution, simply remove the jumper wires.
<h1>Key Features</h1>
<b>1. Simple and clean GUI.</b><br>
<b>2. Two large windows one for mnemonics and other for circuit python code.</b><br>
<b>3. Convert Button - Convert mnemonics to circuit python.</b><br>
<b>4. Copy Button - Copy circuit python code to the clipboard so that it can paste anywhere.</b><br>
<b>5. Reset Button - Clear all data from both windows.</b><br>
<b>6. Save Button - Save circuit python codes on the system for future use.</b><br>
<b>7. Exit Button - Close the application.</b><br>
