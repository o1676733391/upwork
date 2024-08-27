import json
import pyperclip
import keyboard
import threading

# Load the JSON data from the file
json_file_path = 'output.json'

with open(json_file_path, mode='r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Extract each `Prompt`
prompts = [item['Prompt'] for item in data if 'Prompt' in item]

# Initialize a counter to keep track of the current prompt
current_prompt_index = 105

# Flag to track the paused state
paused = True  # Start in a paused state

def copy_next_prompt():
    global current_prompt_index
    if current_prompt_index < len(prompts):
        pyperclip.copy(prompts[current_prompt_index])
        print(f"Copied prompt {current_prompt_index + 1} to clipboard: {prompts[current_prompt_index]}")
        current_prompt_index += 1
    else:
        print("No more prompts to copy.")
        # stop the program
        

def press_key_sequence():
    global paused
    if not paused:
        # Copy the next prompt to the clipboard
        copy_next_prompt()
        # Press `Ctrl+V` to paste
        keyboard.press_and_release('ctrl+v')
        # Press `Enter`
        keyboard.press_and_release('enter')
        print("Automatically pressed 'Ctrl+V', 'Enter'")
    else:
        print("Script is paused.")
    # Schedule the function to run again after 2 minutes
    threading.Timer(130, press_key_sequence).start()  # 120 seconds = 2 minutes

def toggle_pause():
    global paused
    paused = not paused
    state = "paused" if paused else "resumed"
    print(f"Script {state}.")

def start_script():
    global paused
    paused = False
    print("Script started.")
    press_key_sequence()

# Set up a key listener for the `\` key to toggle pause/resume
keyboard.add_hotkey('\\', toggle_pause)

# Set up a key listener for the `PgDn` key to start the script
keyboard.add_hotkey('page down', start_script)

print("Script is ready. Press 'PgDn' to start, '\\' to pause/resume, and 'esc' to exit.")

# Keep the script running
keyboard.wait('esc')  # Press 'esc' to exit the script