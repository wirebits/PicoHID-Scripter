// JavaScript File for PicoHIDWeb
// Author - WireBits

function convertMnemonics() {
    var mnemonicsContent = document.getElementById("mnemonicsArea").value;

    const hidKeys = {
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
    };

    function convertText(text) {
        text = text.replace(/TIME/g, "import time");
        text = text.replace(/HWD/g, "import board\nimport digitalio");
        text = text.replace(/HID/g, "import usb_hid\nfrom adafruit_hid.keycode import Keycode\nfrom adafruit_hid.keyboard import Keyboard\nfrom adafruit_hid.keyboard_layout_us import KeyboardLayoutUS");
        text = text.replace(/KYBD/g, "kbd = Keyboard(usb_hid.devices)\nlayout = KeyboardLayoutUS(kbd)");
        text = text.replace(/PIN/g, "led = digitalio.DigitalInOut(board.LED)\nled.direction = digitalio.Direction.OUTPUT");
        text = text.replace(/LED (ON|OFF)/g, function(match, p1) {
            return p1 === "ON" ? "led.value = 1" : "led.value = 0";
        });

        text = text.replace(/WAIT (\d+)/g, function(_match, p1) {
            var delayTime = parseInt(p1, 10);
            return `time.sleep(${delayTime / 1000})`;
        });

        text = text.replace(/TYPE (.+)/g, function(_match, p1) {
            var stringText = p1
                .replace(/\\/g, '\\\\')
                .replace(/"/g, '\\"');

            return `layout.write("${stringText}")`;
        });

        text = text.replace(/\b([A-Z0-9]+(?:\s[A-Z0-9]+)*)\b/g, function(_match, p1) {
            var keys = p1.split(' ');
            var keySequence = keys.map(key => hidKeys[key]).filter(key => key !== undefined);
            var formattedSequence = keySequence.join(', ');

            if (formattedSequence.length > 0) {
                return `kbd.press(${formattedSequence})\nkbd.release_all()`;
            }
            return _match;
        });

        return text;
    }

    var convertedContent = convertText(mnemonicsContent);
    document.getElementById("picoArea").value = convertedContent;
}

function copyPicoArea() {
    var content = document.getElementById("picoArea").value;
    navigator.clipboard.writeText(content);
}

function resetTextArea() {
    document.getElementById("mnemonicsArea").value = '';
    document.getElementById("picoArea").value = '';
}

function saveFile() {
    var content = document.getElementById("picoArea").value;
    var blob = new Blob([content], { type: "text/plain;charset=utf-8" });
    var link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "code.py";
    link.click();
}