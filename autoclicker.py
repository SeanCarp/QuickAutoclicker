import tkinter as tk
import pyautogui
import threading
import keyboard
import time

class MouseTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Autoclicker")
        self.root.geometry("500x300")
        self.root.attributes("-topmost", True)

        # Labels
        tk.Label(root, text="Mouse Pos. X:").grid(row=0, column=0)
        tk.Label(root, text="Mouse Pos. Y:").grid(row=1, column=0)

        # Entry boxes for mouse coordinates
        self.x_entry = tk.Entry(root)
        self.y_entry = tk.Entry(root)
        self.x_entry.grid(row=0, column=1)
        self.y_entry.grid(row=1, column=1)

        # Move button
        move_button = tk.Button(root, text="Move Mouse", command=self.move_mouse)
        move_button.grid(row=2, column=0, columnspan=2, pady=5)

        # Click interval
        tk.Label(root, text="Click interval (s):").grid(row=3, column=0, columnspan=2)
        self.interval_entry = tk.Entry(root)
        self.interval_entry.insert(0, "1.0")
        self.interval_entry.grid(row=5, column=0, columnspan=2)

        # Autoclicker Control
        self.clicking = False
        self.auto_button = tk.Button(root, text="Start Autoclicker", command=self.toggle_autoclicker)
        self.auto_button.grid(row=5, column=0, columnspan=2, pady=5)

        tk.Label(root, text="ctrl+alt+m to move mouse").grid(row=6, column=1)
        tk.Label(root, text="ctrl+alt+c to (start/stop) autoclicker").grid(row=7, column=1)

        self.update_position()

        threading.Thread(target=self.listen_hotkey, daemon=True).start()

    def update_position(self):
        if not self.x_entry.focus_get():
            self.x_entry.delete(0, tk.END)
            self.x_entry.insert(0, str(pyautogui.position().x))
        if not self.y_entry.focus_get():
            self.y_entry.delete(0, tk.END)
            self.y_entry.insert(0, str(pyautogui.position().y))
        # Repeat after 100 ms
        self.root.after(100, self.update_position)
    
    def move_mouse(self):
        try:
            x = int(self.x_entry.get())
            y = int(self.y_entry.get())
            pyautogui.moveTo(x, y)
        except ValueError:
            print("Please enter valid integers.")

    def toggle_autoclicker(self):
        if not self.clicking:
            self.clicking = True
            self.auto_button.config(text="Stop Autoclicker")
            threading.Thread(target=self.autoclick, daemon=True).start()
        else:
            self.clicking = False
            self.auto_button.config(text="Start Autoclicker")

    def autoclick(self):
        try:
            interval = float(self.interval_entry.get())
        except ValueError:
            interval = 1.0
            self.interval_entry.delete(0, tk.END)
            self.interval_entry.insert(0, "1.0")
        
        while self.clicking:
            pyautogui.click()
            time.sleep(interval)
        
    def listen_hotkey(self):
        keyboard.add_hotkey("ctrl+alt+c", self.toggle_autoclicker)
        keyboard.add_hotkey("ctrl+alt+m", self.move_mouse)        
        keyboard.wait()


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MouseTrackerGUI(root)
    root.mainloop()