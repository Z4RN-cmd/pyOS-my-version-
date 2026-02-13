import os
import sys

print("=== pyOS Notepad ===")

# Ask for filename safely
while True:
    filename = input("Enter your file name (example: note.txt): ").strip()

    if filename == "":
        print("Error: File name cannot be empty.")
        continue
    break

# Force .txt extension
if not filename.endswith(".txt"):
    filename += ".txt"

# Always save in same folder as Notepad.py
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, filename)

# Show existing content if exists
if os.path.exists(file_path):
    print("\n--- Existing File Content ---")
    with open(file_path, "r", encoding="utf8") as f:
        print(f.read())
    print("--- End Of File ---\n")
else:
    print("File does not exist. New file will be created.")

print("Type your text below.")
print("Type SAVE to save file.")
print("Type EXIT to quit without saving.\n")

lines = []

while True:
    text = input()

    if text == "SAVE":
        try:
            with open(file_path, "w", encoding="utf8") as f:
                for line in lines:
                    f.write(line + "\n")
            print("File saved successfully.")
        except Exception as e:
            print("Error saving file:", e)
        break

    elif text == "EXIT":
        print("Exited without saving.")
        break

    else:
        lines.append(text)