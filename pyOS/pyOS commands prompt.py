import time
import random
import sys
import os
import ctypes
import subprocess

print("Welcome to pyOS 0.0.3 Beta.")
name = input("type your username: ")
password = input("type your password: ")

username = name
userpassword = password

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

current_dir = os.path.join("C:\\Users", username)
if not os.path.exists(current_dir):
    current_dir = os.path.expanduser("~")


def get_cmd():
    return input(rf"pyOS:{current_dir}> ")
while True:
    cmd = get_cmd()
    if cmd == "exit":
        SC = input("type your password: ")
        if SC == userpassword:
            sys.exit()
        else:
            print(f"{SC} is not your password")
    elif cmd == "disconnect":
        if is_admin():
            os.system('netsh interface set interface "Wi-Fi" disable')
            print("Internet disconnected.")
        else:
            print("If you want use this command you must run this program as administrator")
    elif cmd == "cls":
        os.system("cls")
    elif cmd == "time":
        print(time.ctime())
    elif cmd.startswith("open "):
        target = cmd[5:].strip()
        
        if not os.path.isabs(target):
            path = os.path.join(current_dir, target)
        else:
            path = target
        
        if os.path.isfile(path):
            
            if os.lower().endswith(".exe"):
                try:
                    subprocess.run([path])
                except Exception as e:
                    print(f"cannot run file: {e}")
            else:
                try:
                    with open(path, "r", encoding="utf8") as f:
                        print("\n--- FILE CONTENT ---")
                        print(f.read())
                        print("---END FILE---\n")
                except Exception as e:
                    print(f"File exists but cannot be opened as text: {e}")
        else:
            print("file not found.")
 
    elif cmd.startswith("cd "):
        target = cmd[3:]
        if not os.path.isabs(target):
            target = os.path.join(current_dir, target)
        try:
            os.chdir(target)
            current_dir = os.getcwd()
        except FileNotFoundError:
            print("Directory not found")
    elif cmd == "status":
        if is_admin():
            print("Administrator")
        else:
            print("user")
    elif cmd == "help":
        print("""
            Available commands:
            - help        : show this help
            - exit        : exit pyOS
            - cls         : clear screen
            - time        : show system time
            - status      : show user status
            - open <file> : open file
            - cd <dir>    : change directory
            - disconnect  : disable internet (admin only)
            - calculator  : open the pyOS calculator
            - notepad     : open the pyOS notepad
            - whoami      : view the user data
            -file_manager : open the pyOS file manager
            -paint        : open the pyOS paint app
            """)
    elif cmd == "calculator":
        base_dir = os.path.dirname(os.path.abspath(__file__))
        calc_path = os.path.join(base_dir, "Calculator.py")
        
        if os.path.exists(calc_path):
            try:
                subprocess.run(["python", calc_path])
            except Exception as e:
                print(f"error while opening calculator: {e}")
        else:
            print("Error. Cannot open calculator or calculator not in the same folder.")
            print("Please put Calculator.py in the same folder as this file.")
            print("If there is no calculator file you can reinstall this OS in:")
            print("https://github.com/Z4RN-cmd/pyOS-my-version-")
    elif cmd == "notepad":
        base_dir = os.path.dirname(os.path.abspath(__file__))
        note_path = os.path.join(base_dir, "notepad.py")
        if os.path.exists(note_path):
            try:
                subprocess.run(["python", note_path])
            except Exception as e:
                print(f"Error {e}!")
                print("Error. Cannot open Notepad or Notepad not in the same folder.")
                print("Please put Notepad.py in the same folder as this file.")
                print("If there is no Notepad file you can reinstall this OS in:")
                print("https://github.com/Z4RN-cmd/pyOS-my-version-")
    
        else:
            print("Error. Cannot open Notepad or Notepad not in the same folder.")
            print("Please put Notepad.py in the same folder as this file.")
            print("If there is no Notepad file you can reinstall this OS in:")
            print("https://github.com/Z4RN-cmd/pyOS-my-version-")
    elif cmd == "whoami":
        print(f"username: {username}")
        print(f"password:******")
    elif cmd == "sudo$ whoami /all":
        print(f"username:{username}")
        print(f"password:{password}")
        print(f"email: NOT AVALAIBLE NOW")                
    elif cmd == "file_manager":
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filemanager_path = os.path.join(base_dir, "filemanager.py")
        if os.path.exists(filemanager_path):
            try:
                subprocess.run(["python", filemanager_path])
            except Exception as e:
                print(f"Error {e}!")
                print("Error. Cannot open File manager or File manager not in the same folder.")
                print("Please put filemanager.py in the same folder as this file.")
                print("If there is no filemanager file you can reinstall this OS in:")
                print("https://github.com/Z4RN-cmd/pyOS-my-version-")
    
        else:
            print("Error. Cannot open file manager or file manager not in the same folder.")
            print("Please put filemanager.py in the same folder as this file.")
            print("If there is no filemanager file you can reinstall this OS in:")
            print("https://github.com/Z4RN-cmd/pyOS-my-version-")
    elif cmd == "paint":
        base_dir = os.path.dirname(os.path.abspath(__file__))
        paint_path = os.path.join(base_dir, "paint.py")
        if os.path.exists(paint_path):
            try:
                subprocess.run(["python", paint_path])
            except Exception as e:
                print(f"Error {e}!")
                print("Error. Cannot open Paint or Paint not in the same folder.")
                print("Please put paint.py in the same folder as this file.")
                print("If there is no Paint file you can reinstall this OS in:")
                print("https://github.com/Z4RN-cmd/pyOS-my-version-")
        else:
            print("Error. Cannot open Paint or Paint not in the same folder.")
            print("Please put paint.py in the same folder as this file.")
            print("If there is no Paint file you can reinstall this OS in:")
            print("https://github.com/Z4RN-cmd/pyOS-my-version-")
        
        
    else:
        print(f"{cmd} is not a is not recognized as commands.")   