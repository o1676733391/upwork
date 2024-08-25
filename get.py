import json
import pyperclip
import keyboard

# Load the JSON data from the file
json_file_path = 'output.json'

with open(json_file_path, mode='r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Extract each `Prompt`
prompts = [item['Prompt'] for item in data if 'Prompt' in item]

# Initialize a counter to keep track of the current prompt
current_prompt_index = 0

def copy_next_prompt():
    global current_prompt_index
    if current_prompt_index < len(prompts):
        pyperclip.copy(prompts[current_prompt_index])
        print(f"Copied prompt {current_prompt_index + 1} to clipboard: {prompts[current_prompt_index]}")
        current_prompt_index += 1
    else:
        print("No more prompts to copy.")
# start at 52 
current_prompt_index = 8
# Set up a key listener for the "N" key
keyboard.add_hotkey('\\', copy_next_prompt)

print("Press '\' to copy the next prompt to the clipboard.")

# Keep the script running
keyboard.wait('esc')  # Press 'esc' to exit the script