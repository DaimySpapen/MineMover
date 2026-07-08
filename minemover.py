from tkinter import messagebox
import tkinter as tk
import getpass
import shutil
import os
# Of course the autistic one (me) needs to import everything in order

# User-specific paths
USER = getpass.getuser()
MINEMOVERT_DIR = fr"C:\Users\{USER}\Documents\MineMover"
MINECRAFT_ACTIVE_MODS = fr"C:\Users\{USER}\AppData\Roaming\.minecraft\mods"

# Guess mod loader from folder name (suffixes are my own shorthand)
def guess_loader(foldername):
    if foldername.endswith(" fa"):
        return "Fabric"
    elif foldername.endswith(" fo"):
        return "Forge"
    elif foldername.endswith(" neo"):
        return "NeoForge"
    elif foldername.endswith(" qu"):
        return "Quilt"
    elif foldername.endswith(" li"):
        return "LiteLoader"
    elif foldername.endswith(" ri"):
        return "Rift"
    elif foldername.endswith(" rm"):
        return "Risugami's ModLoader"
    return "Unknown"

# Remove the suffix so names look nicer in the UI
def trim_suffix(foldername):
    suffixes = [" fa", " fo", " neo", " qu", " li", " ri", " rm"]
    for s in suffixes:
        if foldername.endswith(s):
            return foldername[:-len(s)]
    return foldername

# Wipe the Minecraft mods folder
def clear_mods_folder():
    if not os.path.exists(MINECRAFT_ACTIVE_MODS):
        os.makedirs(MINECRAFT_ACTIVE_MODS)  # make it if missing
        return

    for item in os.listdir(MINECRAFT_ACTIVE_MODS):
        full_path = os.path.join(MINECRAFT_ACTIVE_MODS, item)
        try:
            if os.path.isfile(full_path) or os.path.islink(full_path):
                os.unlink(full_path)
            elif os.path.isdir(full_path):
                shutil.rmtree(full_path)
        except Exception as e:
            print(f"Couldn't delete {full_path}: {e}")  # not ideal, but it happens

# Copy mods from selected folder into minecraft mods folder
def copy_mods_from(selected_folder):
    src = os.path.join(MINEMOVERT_DIR, selected_folder)
    if not os.path.exists(src):
        print("Source folder doesn't exist?")  # shouldn't happen
        return False

    for file in os.listdir(src):
        src_file = os.path.join(src, file)
        dest_file = os.path.join(MINECRAFT_ACTIVE_MODS, file)
        try:
            if os.path.isfile(src_file):
                shutil.copy2(src_file, dest_file)
        except:
            print(f"Couldn’t copy: {file}")  # also shouldn't happen
    return True

# Get folders that exist inside the mod storage directory
def get_mod_folders():
    if not os.path.exists(MINEMOVERT_DIR):
        return []

    # NOTE: I sometimes have random files in here too
    folders = []
    for f in sorted(os.listdir(MINEMOVERT_DIR)):
        full = os.path.join(MINEMOVERT_DIR, f)
        if os.path.isdir(full):
            folders.append(f)
    return folders

# Switch the mods by clearing and copying
def switch_mods_to(folder):
    clear_mods_folder()
    return copy_mods_from(folder)

# Main GUI logic
def main():
    if not os.path.exists(MINEMOVERT_DIR):
        os.mkdir(MINEMOVERT_DIR)

    folders = get_mod_folders()
    if not folders:
        messagebox.showerror("No Folders", "No mod folders found in MineMover.")
        return

    # Button action when user picks a mod set
    def on_select():
        selected = listbox.curselection()
        if not selected:
            messagebox.showwarning("No Selection", "Pick a folder first.")
            return

        folder = folders[selected[0]]
        print(f"Trying to switch to: {folder}")  # debug

        if switch_mods_to(folder):
            messagebox.showinfo(
                "Done!",
                f"✅ Switched to: {trim_suffix(folder)}\n🔧 Mod loader: {guess_loader(folder)}"
            )
        else:
            messagebox.showerror("Oops", "Something went wrong while switching mods.")

    # UI Setup
    root = tk.Tk()
    root.title("MineMover - Mod Switcher")
    root.geometry("400x300")
    root.resizable(False, False)

    tk.Label(root, text="Select a mod folder:", font=("Arial", 12)).pack(pady=10)

    # Listbox with scrollbar
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, font=("Arial", 10))
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    for f in folders:
        loader = guess_loader(f)
        display = trim_suffix(f)
        listbox.insert(tk.END, f"{display} ({loader})")

    tk.Button(
        root,
        text="Switch Mods",
        command=on_select,
        bg="#4CAF50",
        fg="white",
        font=("Arial", 12),
        pady=5
    ).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()