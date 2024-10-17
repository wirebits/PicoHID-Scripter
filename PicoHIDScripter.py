# PicoHID Scripter
# A GUI tool that generates CircuitPython HID scripts for Raspberry Pi Pico Series using Mnemonics.
# Author - WireBits

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

hidKeys = {
    'A': 'Keycode.A', 'B': 'Keycode.B', 'C': 'Keycode.C', 'D': 'Keycode.D', 'E': 'Keycode.E',
    'F': 'Keycode.F', 'G': 'Keycode.G', 'H': 'Keycode.H', 'I': 'Keycode.I', 'J': 'Keycode.J',
    'K': 'Keycode.K', 'L': 'Keycode.L', 'M': 'Keycode.M', 'N': 'Keycode.N', 'O': 'Keycode.O',
    'P': 'Keycode.P', 'Q': 'Keycode.Q', 'R': 'Keycode.R', 'S': 'Keycode.S', 'T': 'Keycode.T',
    'U': 'Keycode.U', 'V': 'Keycode.V', 'W': 'Keycode.W', 'X': 'Keycode.X', 'Y': 'Keycode.Y',
    'Z': 'Keycode.Z', 'F1': 'Keycode.F1', 'F2': 'Keycode.F2', 'F3': 'Keycode.F3', 'F4': 'Keycode.F4',
    'F5': 'Keycode.F5', 'F6': 'Keycode.F6', 'F7': 'Keycode.F7', 'F8': 'Keycode.F8', 'F9': 'Keycode.F9',
    'F10': 'Keycode.F10', 'F11': 'Keycode.F11', 'F12': 'Keycode.F12', 'LEFT': 'Keycode.LEFT_ARROW',
    'UP': 'Keycode.UP_ARROW', 'RIGHT': 'Keycode.RIGHT_ARROW', 'DOWN': 'Keycode.DOWN_ARROW',
    'TAB': 'Keycode.TAB', 'HOME': 'Keycode.HOME', 'END': 'Keycode.END', 'PGUP': 'Keycode.PAGE_UP',
    'PGDN': 'Keycode.PAGE_DOWN', 'CAPS': 'Keycode.CAPS_LOCK', 'NUM': 'Keycode.KEYPAD_NUMLOCK',
    'SCROLL': 'Keycode.SCROLL_LOCK', 'CTRL': 'Keycode.CONTROL', 'SHIFT': 'Keycode.SHIFT', 'ALT': 'Keycode.ALT',
    'GUI': 'Keycode.GUI', 'ESC': 'Keycode.ESCAPE', 'PRTSCR': 'Keycode.PRINT_SCREEN', 'PAUSE': 'Keycode.PAUSE',
    'SPACE': 'Keycode.SPACE', 'DEL': 'Keycode.DELETE', 'INSERT': 'Keycode.INSERT', 'BKSP': 'Keycode.BACKSPACE',
    'ENTER': 'Keycode.ENTER', 'APP': 'Keycode.APPLICATION'
}

class PicoHIDKeyboard:
    @staticmethod
    def convert_to_pico_script(pico_mnemonic):
        if pico_mnemonic.startswith("CMT"):
            comment_text = pico_mnemonic.split(" ", 1)[1]
            return f"# {comment_text}"
        elif pico_mnemonic.startswith("TIME"):
            return "import time"
        elif pico_mnemonic.startswith("HWD"):
            return "import board\nimport digitalio"
        elif pico_mnemonic.startswith("HID"):
            return "import usb_hid"
        elif pico_mnemonic.startswith("KEYBOARD"):
            hid_lib = "from adafruit_hid.keycode import Keycode\n"
            hid_lib += "from adafruit_hid.keyboard import Keyboard\n"
            hid_lib += "from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS\n\n"
            hid_lib += "kbd = Keyboard(usb_hid.devices)\nlayout = KeyboardLayoutUS(kbd)"
            return hid_lib
        elif pico_mnemonic.startswith("PIN"):
            led_code = f"led = digitalio.DigitalInOut(board.GP25)\nled.direction = digitalio.Direction.OUTPUT"
            return led_code
        elif pico_mnemonic.startswith("LED"):
            led_value = (pico_mnemonic.split(" ")[1])
            if led_value == "ON":
                return "led.value = 1"
            elif led_value == "OFF":
                return "led.value = 0"
        elif pico_mnemonic.startswith("WAIT"):
            delay_time = int(pico_mnemonic.split(" ")[1])
            return f"time.sleep({delay_time / 1000})"
        elif pico_mnemonic.startswith("TYPE"):
            string_text = pico_mnemonic.split(" ", 1)[1]
            return f"layout.write(\"{string_text}\")"
        else:
            keys = pico_mnemonic.split()
            keycodes = []
            for key in keys:
                if key in hidKeys:
                    keycodes.append(hidKeys[key])
                else:
                    return f"# Unknown key: {key}"
            
            if keycodes:
                keycodes_str = ", ".join(keycodes)
                return f"kbd.press({keycodes_str})\nkbd.release_all()"
            else:
                return pico_mnemonic

class PicoHIDMouse:
    @staticmethod
    def convert_to_pico_script(pico_mnemonic):
        if pico_mnemonic.startswith("CMT"):
            comment_text = pico_mnemonic.split(" ", 1)[1]
            return f"# {comment_text}"
        elif pico_mnemonic.startswith("MOUSE"):
            return "from adafruit_hid.mouse import Mouse\n\nmse = Mouse(usb_hid.devices)"
        elif pico_mnemonic.startswith("MOVE"):
            try:
                _, x, y, w = pico_mnemonic.split()
                x = int(x)
                y = int(y)
                w = int(w)
                return f"mse.move({x}, {y}, {w})"
            except ValueError:
                return "Invalid parameters for MOVE command!"
        elif pico_mnemonic.startswith("CLICK"):
            cvalue = pico_mnemonic.split(" ", 1)[1]
            if cvalue == "LEFT":
                return "mse.click(Mouse.LEFT_BUTTON)"
            elif cvalue == "MIDDLE":
                return "mse.click(Mouse.MIDDLE_BUTTON)"
            elif cvalue == "RIGHT":
                return "mse.click(Mouse.RIGHT_BUTTON)"
        elif pico_mnemonic.startswith("PRESS"):
            pvalue = pico_mnemonic.split(" ", 1)[1]
            if pvalue == "LEFT":
                return "mse.press(Mouse.LEFT_BUTTON)\nmse.release_all()"
            elif pvalue == "MIDDLE":
                return "mse.press(Mouse.MIDDLE_BUTTON)\nmse.release_all()"
            elif pvalue == "RIGHT":
                return "mse.press(Mouse.RIGHT_BUTTON)\nmse.release_all()"
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
        self.mnemonic_frame.insert(tk.END, "Enter Mnemonics")

        self.pico_frame = tk.Text(main_split_frame, font='courier 10', fg='black')
        self.pico_frame.pack(side="right", fill="both", expand=True)
        self.pico_frame.insert(tk.END, "Your CircuitPython Script")

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

        upload_button = ttk.Button(buttons_frame, text="From", command=self.from_mnemonics)
        upload_button.pack(side="left", padx=5, pady=5)

        exit_button = ttk.Button(buttons_frame, text="Exit", command=self.exit_window)
        exit_button.pack(side="right", padx=5, pady=5)

    def clear_placeholder(self, event):
        if event.widget == self.mnemonic_frame and self.mnemonic_frame.get(1.0, tk.END).strip() == "Enter Mnemonics":
            self.mnemonic_frame.delete(1.0, tk.END)
        if event.widget == self.pico_frame and self.pico_frame.get(1.0, tk.END).strip() == "Your CircuitPython Script":
            self.pico_frame.delete(1.0, tk.END)

    def convert_text(self):
        pico_script = []
        mnemonics = self.mnemonic_frame.get("1.0", "end").strip().splitlines()

        if not mnemonics or mnemonics == ["Enter Mnemonics"]:
            self.pico_frame.delete("1.0", tk.END)
            self.pico_frame.insert("1.0", "Enter Some Mnemonics To Convert!")
            return

        if mnemonics[0] == "MOUSE":
            pico_script.append(PicoHIDMouse.convert_to_pico_script(mnemonics[0]))
            for mnemonic in mnemonics[1:]:
                pico_script.append(PicoHIDMouse.convert_to_pico_script(mnemonic))
        else:
            pico_script.append(PicoHIDKeyboard.convert_to_pico_script(mnemonics[0]))
            for mnemonic in mnemonics[1:]:
                pico_script.append(PicoHIDKeyboard.convert_to_pico_script(mnemonic))

        self.pico_frame.delete("1.0", tk.END)
        self.pico_frame.insert("1.0", "\n".join(pico_script))

    def copy_text(self):
        self.main_window.clipboard_clear()
        self.main_window.clipboard_append(self.pico_frame.get("1.0", "end"))

    def reset_all(self):
        self.mnemonic_frame.delete("1.0", tk.END)
        self.mnemonic_frame.insert(tk.END, "Enter Mnemonics")
        self.pico_frame.delete("1.0", tk.END)
        self.pico_frame.insert(tk.END, "Your CircuitPython Script")

    def save_file(self):
        pico_script = self.pico_frame.get("1.0", "end")
        filename = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py")])
        if filename:
            with open(filename, "w") as file:
                file.write(pico_script)

    def from_mnemonics(self):
        file_name = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_name:
            with open(file_name, "r") as file:
                self.mnemonic_frame.delete("1.0", tk.END)
                self.mnemonic_frame.insert("1.0", file.read())

    def exit_window(self):
        self.main_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    PicoHIDMain(root)
    root.mainloop()
