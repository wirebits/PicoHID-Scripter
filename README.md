# PicoHID-Scripter
A GUI tool that generates CircuitPython HID scripts from mnemonics for Raspberry Pi Pico.

# This project is only working for Raspberry Pi Pico!

# Credits
The mnemoics used in this tool is heavily inspired by <a href="https://github.com/hak5">Hak5</a> Ducky Script.<br>

# Demo Video

https://github.com/wirebits/PicoHID-Scripter/assets/159493381/c7a531c7-b79f-46bb-b125-bbbec8d331d7

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
-There are two important things in it : <br>
-<b>lib</b> folder<br>
-<b>code.py</b> file<br>
7. Download Adafruit HID Library from <a href="https://github.com/adafruit/Adafruit_CircuitPython_HID/releases/download/6.1.0/adafruit-circuitpython-hid-8.x-mpy-6.1.0.zip">here</a>.<br>
8. Extarct the ZIP file.<br>
9. Copy <b>adafruit_hid</b> folder in the <b>lib</b> folder of ```CIRCUITPY```.<br>
10. Done! Now, Raspberry Pi Pico is ready to use as a USB Rubber Ducky.

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
  <th>BD</th>
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
  <th>It add pin number of led in the code.</th>
  <th>PIN 25</th>
 </tr>
 <tr>
  <th>LV</th>
  <th>It turns on/off the led in the code.<br>Values are 0(OFF) and 1(ON).</th>
  <th>LV 1</th>
 </tr>
 <tr>
  <th>INTVL</th>
  <th>It add time in the code.<br>Time is in milliseconds.<br>1000 ms = 1 second.</th>
  <th>TIME 1000</th>
 </tr>
 <tr>
  <th>WRITE</th>
  <th>It add text want to type in the code.</th>
  <th>WRITE Hello World!</th>
 </tr>
 <tr>
  <th>SCODE</th>
  <th>It press and release the key immediately.</th>
  <th>SCODE A</th>
 </tr>
 <tr>
  <th>PCODE</th>
  <th>It press and hold the key until AR is called to release all keys.</th>
  <th>PCODE S</th>
 </tr>
 <tr>
  <th>AR</th>
  <th>It release all keys which is called by PCODE.</th>
  <th>Just type AR</th>
 </tr>
 <tr>
  <th>WHILE</th>
  <th>It add the while loop in the code.<br>It accepts 1 as argument.</th>
  <th>WHILE 1</th>
 </tr>
 <tr>
  <th>GAP</th>
  <th>It add a gap between two or more text vertically.</th>
  <th>Just type GAP</th>
 </tr>
 <tr>
  <th>NXT</th>
  <th>It push the cursor to the next line.</th>
  <th>Just type NXT</th>
 </tr>
 <tr>
  <th>SP</th>
  <th>It creates space for indentation.</th>
  <th>Just type SP</th>
 </tr>
</table>

# Tested Systems
The tool is currently tested on : <br>
1. Windows (10)<br>
The testing is going on different systems.

# Install and Run
1. Download or Clone the Repository.<br>
2. Open the folder and just double click on PicoHIDScripter.py file.<br>
3. Type the mnemonics in the left window.<br>
4. Click on ```Convert``` button to get corresponding circuit python script.<br>
5. Click on ```Copy``` button to copy the circuit python script to the clipboard.<br>
6. Paste the code in the ```code.py``` file in the ```CIRCUITPY```.<br>
-Be Careful! As it is saved the script start executing.

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
