# PicoHID Scripter
# A GUI tool that generates CircuitPython HID scripts from mnemonics for Raspberry Pi Pico.
# Author - WireBits

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

class PicoHIDConverter:
    def convert_to_pico_script(pico_mnemonic):
        if pico_mnemonic.startswith("TIME"):
            return "import time"
        elif pico_mnemonic.startswith("BOARD"):
            return "import board"
        elif pico_mnemonic.startswith("DGIO"):
            return "import digitalio"
        elif pico_mnemonic.startswith("HID"):
            return "import usb_hid"
        elif pico_mnemonic.startswith("HLIB"):
            hid_lib = "from adafruit_hid.keycode import Keycode\n"
            hid_lib += "from adafruit_hid.keyboard import Keyboard\n"
            hid_lib += "from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS"
            return hid_lib
        elif pico_mnemonic.startswith("KYBD"):
            return "kbd = Keyboard(usb_hid.devices)\nlayout = KeyboardLayoutUS(kbd)"
        elif pico_mnemonic.startswith("PIN"):
            led_code = f"led = digitalio.DigitalInOut(board.GP25)\nled.direction = digitalio.Direction.OUTPUT"
            return led_code
        elif pico_mnemonic.startswith("LED"):
            led_value = (pico_mnemonic.split(" ")[1])
            if led_value == "ON":
                return "led.value = 1"
            elif led_value == "OFF":
                return "led.value = 0"
        elif pico_mnemonic.startswith("INTVL"):
            delay_time = int(pico_mnemonic.split(" ")[1])
            return f"time.sleep({delay_time / 1000})"
        elif pico_mnemonic.startswith("WRITE"):
            string_text = pico_mnemonic.split(" ", 1)[1]
            return f"layout.write(\"{string_text}\")"
        elif pico_mnemonic.startswith("SCODE"):
            keys = pico_mnemonic.split()[1:]
            key_sequence = [f"Keycode.{key}" for key in keys]
            formatted_sequence = ', '.join(key_sequence)
            output_string = f"kbd.send({formatted_sequence})"
            return output_string
        elif pico_mnemonic.startswith("PCODE"):
            keys = pico_mnemonic.split()[1:]
            key_sequence = [f"Keycode.{key}" for key in keys]
            formatted_sequence = ', '.join(key_sequence)
            output_string = f"kbd.press({formatted_sequence})\nkbd.release_all()"
            return output_string
        elif pico_mnemonic.startswith("WHILE"):
            condition = bool(pico_mnemonic.split(" ")[1])
            return f"while {condition}:\n"
        elif pico_mnemonic.startswith("GAP"):
            return "\n\n"
        elif pico_mnemonic.startswith("NXT"):
            return "\n"
        elif pico_mnemonic.startswith("SP"):
            return "  "
        else:
            return pico_mnemonic

class PicoHIDMain:
    def __init__(self, main_window):
        self.main_window = main_window
        self.create_widgets()

    def create_widgets(self):
        self.main_window.title("PicoHID Scripter")
        self.main_window.resizable(0, 0)

        main_split_frame = ttk.Frame(self.main_window)
        main_split_frame.pack(side="top", fill="both", expand=True)

        self.mnemonic_frame = tk.Text(main_split_frame, font='courier 10', fg='black')
        self.mnemonic_frame.pack(side="left", fill="both", expand=True)
        self.mnemonic_frame.insert(tk.END, "Enter your mnemonic")

        self.pico_frame = tk.Text(main_split_frame, font='courier 10', fg='black')
        self.pico_frame.pack(side="right", fill="both", expand=True)
        self.pico_frame.insert(tk.END, "Your pico script")

        self.mnemonic_frame.bind("<FocusIn>", self.clear_placeholder)
        self.pico_frame.bind("<FocusIn>", self.clear_placeholder)

        buttons_frame = ttk.Frame(self.main_window)
        buttons_frame.pack(side="top", fill="x")

        convert_button = ttk.Button(buttons_frame, text="Convert", command=self.convert_text)
        convert_button.pack(side="left", padx=5, pady=5)

        copy_button = ttk.Button(buttons_frame, text="Copy", command=self.copy_text)
        copy_button.pack(side="left", padx=5, pady=5)

        reset_button = ttk.Button(buttons_frame, text="Reset", command=self.reset_all)
        reset_button.pack(side="left", padx=5, pady=5)

        save_button = ttk.Button(buttons_frame, text="Save", command=self.save_file)
        save_button.pack(side="left", padx=5, pady=5)

        exit_button = ttk.Button(buttons_frame, text="Exit", command=self.exit_window)
        exit_button.pack(side="right", padx=5, pady=5)

    def clear_placeholder(self, event):
        if event.widget.get(1.0, tk.END).strip() == "Enter your mnemonic":
            event.widget.delete(1.0, tk.END)

    def convert_text(self):
        duckpy_script = self.mnemonic_frame.get(1.0, tk.END).strip()
        if not duckpy_script:
            self.pico_frame.delete(1.0, tk.END)
            self.pico_frame.insert(tk.END, "Enter some mnemonics to convert!")
        else:
            mnemonics = ""
            for line in duckpy_script.splitlines():
                converted_line = PicoHIDConverter.convert_to_pico_script(line.strip())
                mnemonics += converted_line
            self.pico_frame.delete(1.0, tk.END)
            self.pico_frame.insert(tk.END, mnemonics)

    def copy_text(self):
        self.main_window.clipboard_clear()
        self.main_window.clipboard_append(self.pico_frame.get(1.0, tk.END))

    def reset_all(self):
        self.mnemonic_frame.delete(1.0, tk.END)
        self.mnemonic_frame.insert(tk.END, "Enter your mnemonic")
        self.pico_frame.delete(1.0, tk.END)
        self.pico_frame.insert(tk.END, "Your pico script")

    def exit_window(self):
        self.main_window.destroy()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(filetypes=[('Python Files', '*.py')], defaultextension='.py')
        if not file_path:
            return
        with open(file_path, 'w') as file:
            file.write(self.pico_frame.get(1.0, tk.END))

main_window = tk.Tk()
app = PicoHIDMain(main_window)
main_window.mainloop()