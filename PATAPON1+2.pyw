import time
import keyboard
import threading
import tkinter as tk

def center_window(win, width=400, height=230):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    
    win.geometry(f'{width}x{height}+{x}+{y}')

root = tk.Tk()
root.title('PATAPON 1+2 REPLAY Drum Macro')
root.geometry('400x230')
root.resizable(False, False)

center_window(root, width=400, height=230)

label = tk.Label(
    root,
    text='Drum Commands',
    font=('Calibri Light', 15,),
    pady=5
)
label.pack()

command_list = tk.Listbox(
    root,
    font=('Arial', 12),
    height=10,
    activestyle='none',
    selectmode='none'
)
command_list.pack(fill='both', expand=True, padx=10, pady=5)

commands = [
    'Y      PATA PATA (March)',
    'U      PON PON (Attack)',
    'I      CHAKA CHAKA (Defend)',
    'O      MIRACLE (Juju)',
    'H      PON PATA (Retreat)',
    'J      PON CHAKA (Charge)',
    'K      DON DON (Jump)',
    'L      DON CHAKA (Party)',
    'ESC    Exit Program'
]

for cmd in commands:
    command_list.insert(tk.END, cmd)
    
is_playing = False

def play_pattern(pattern, intervals, end_delay=0):
    global is_playing
    if is_playing:
        return
    is_playing = True

    if isinstance(intervals, (int, float)):
        intervals = [intervals] * len(pattern)

    for key, delay in zip(pattern, intervals):
        keyboard.press_and_release(key)
        time.sleep(delay)

    if end_delay > 0:
        time.sleep(end_delay)

    is_playing = False

def PATAPATA():
    play_pattern(['a', 'a', 'a', 'd'], 0.5)

def PONPON():
    play_pattern(['d', 'd', 'a', 'd'], 0.5)

def CHAKACHAKA():
    play_pattern(['w', 'w', 'a', 'd'], 0.5)
    
def MIRACLE():
    play_pattern(
        pattern=['s', 's', 's', 's', 's'],
        intervals=[0.45, 0.20, 0.55, 0.20, 0.20],
        end_delay=0.3
    )

def PONPATA():
    play_pattern(['d', 'a', 'd', 'a'], 0.5)

def PONCHAKA():
    play_pattern(['d', 'd', 'w', 'w'], 0.5)

def DONDON():
    play_pattern(['s', 's', 'w', 'w'], 0.5)

def DONCHAKA():
    play_pattern(['a', 'd', 's', 'w'], 0.5)

keyboard.add_hotkey('y', lambda: threading.Thread(target=PATAPATA, daemon=True).start())
keyboard.add_hotkey('u', lambda: threading.Thread(target=PONPON, daemon=True).start())
keyboard.add_hotkey('i', lambda: threading.Thread(target=CHAKACHAKA, daemon=True).start())
keyboard.add_hotkey('o', lambda: threading.Thread(target=MIRACLE, daemon=True).start())
keyboard.add_hotkey('h', lambda: threading.Thread(target=PONPATA, daemon=True).start())
keyboard.add_hotkey('j', lambda: threading.Thread(target=PONCHAKA, daemon=True).start())
keyboard.add_hotkey('k', lambda: threading.Thread(target=DONDON, daemon=True).start())
keyboard.add_hotkey('l', lambda: threading.Thread(target=DONCHAKA, daemon=True).start())

def close_app():
    root.destroy()

keyboard.add_hotkey('esc', close_app)

root.mainloop()