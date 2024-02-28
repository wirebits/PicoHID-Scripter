# PicoHID-Scripter
A GUI tool that generates CircuitPython HID scripts from mnemonics for Raspberry Pi Pico.

# Credits
The mnemoics used in this tool is heavily inspired by <a href="https://github.com/hak5">Hak5</a> Ducky Script.<br>

# Setup and Installation of Circuit Python
1. Make sure the python is installed on your system (Windows/Linux/MacOS).<br>
2. Download Circuit Python <b>.uf2</b> file for Raspberry Pi Pico from <a href="https://downloads.circuitpython.org/bin/raspberry_pi_pico/en_US/adafruit-circuitpython-raspberry_pi_pico-en_US-8.2.10.uf2">here</a>.<br>
3. Connect Raspberry Pi Pico with a USB cable.<br>
4. Press and hold the bootsel button and connect to the PC/Laptop.<br>
-When it connects, then Raspberry Pi Pico show as a removable storage device named <b>RPI-RP2</b>.<br>
-When <b>RPI-RP2</b> is showing, then release the bootsel button.<br>
5. Copy the uf2 file in the <b>RPI-RP2</b>.<br>
-When it is copied, then it disconnects automatically and reconnect as <b>CIRCUITPY</b>.<br>
Means circuit python is successfully flashed in the Raspberry Pi Pico.
6. Open <b>CIRCUITPY</b>.<br>
-There are two important things in it : <br>
-<b>lib</b> folder<br>
-<b>code.py</b> file<br>
7. Download Adafruit HID Library from <a href="https://github.com/adafruit/Adafruit_CircuitPython_HID/releases/download/6.1.0/adafruit-circuitpython-hid-8.x-mpy-6.1.0.zip">here</a>.<br>
8. Extarct the ZIP file.<br>
9. Copy <b>adafruit_hid</b> folder in the <b>lib</b> folder of <b>CIRCUITPY</b>.<br>
10. Done! Now, Raspberry Pi Pico is ready to use as a USB Rubber Ducky.

# Tested Systems
The tool is currently tested on : <br>
1. Windows (10)<br>
The testing is going on different systems.

# Install and Run
1. Download or Clone the Repository.<br>
2. Open the folder and just double click on PicoHIDScripter.py file.<br>

<h1>Key Features</h1>
<b>1. Simple and clean GUI.</b><br>
<b>2. Two large windows one for mnemonics and other for circuit python code.</b><br>
<b>3. Convert Button - Convert mnemonics to circuit python.</b><br>
<b>4. Copy Button - Copy circuit python code to the clipboard so that it can paste anywhere.</b><br>
<b>5. Reset Button - Clear all data from both windows.</b><br>
<b>6. Save Button - Save circuit python codes on the system for future use.</b><br>
<b>7. Exit Button - Close the application.</b><br>
