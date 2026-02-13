import os
import time

print("=== pyOS file manager ===")
current_dir = os.path.expanduser("~")

def show_path():
    return input(f"FileManager:{current_dir}> ")

while True:
    cmd = show_path()
    
    if cmd == "exit":
        print("exiting file Manager...")
        time.sleep(1)
        break
    elif cmd == "ls":
        try:
            files = os.listdir(current_dir)
            for f in files:
                print(f)
        except Exception as e:
            print("error:", e)
        time.sleep(1)
    elif cmd.startswith("mkdir "):
        folder_name = cmd[6:].strip()
        path = os.path.join(current_dir, folder_name)
        
        try:
            os.mkdir(path)
            print("folder created")
        except FileExistsError:
            print("Folder already exists.")
        except Exception as e:
            print("Error:", e)
    elif cmd.startswith("mkfile "):
        file_name = cmd[7:].strip()
        path = os.path.join(current_dir, file_name)
        
        try:
            with open(path, "w") as f:
                pass
            print("file created.")
        except Exception as e:
            print("Error:", e)
        time.sleep(1)
    elif cmd.startswith("del "):
        file_name = cmd[4:].strip()
        path = os.path.join(current_dir, file_name)     
        yn = input(f"(y/n)Are you sure want to delete {file_name}?(this action cannot be undone)")
        if yn == "y":
            try:
                os.remove(path)
                print("File deleted.")
            except FileNotFoundError:
                print("file not found.")
            except Exception as e:
                print("Error:", e)
            time.sleep(1)
        elif yn == "n":
            print("command stopped")
        else:
            print("Please answer y/n.")
    elif cmd.startswith("rmdir "):
        folder_name = cmd[6:].strip()
        path = os.path.join(current_dir, folder_name)
        
        try:
            os.rmdir(path)
            print("folder removed.")
        except OSError:
            print("Folder not empty or cannot be removed.")
        time.sleep(1)
    elif cmd.startswith("cd "):
        target = cmd[3:].strip()
        
        if target == "..":
            parent =os.path.dirname(current_dir)
            current_dir = parent
            print("Moved to parent directory.")
        else:
            new_path = os.path.join(current_dir, target)
            
            if os.path.isdir(new_path):
                current_dir = new_path
                print(f"moved to {current_dir}")
            else:
                print("Directory not found")
        time.sleep(1)
    elif cmd == "help":
            print("Available commands:\n")
            print("ls                  : show files and folders")
            print("cd <folder>         : change directory")
            print("cd ..               : go to parent directory")
            print()
            print("mkdir <name>        : create new folder")
            print("mkfile <name>       : create new file")
            print()
            print("del <file>          : delete file")
            print("rmdir <folder>      : remove empty folder")
            print()
            print("exit                : exit file manager")
            time.sleep(1)
        

    
        