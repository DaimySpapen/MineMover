import argparse
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

# Remove the suffix so names look nicer in the output
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
            print(f"Couldn’t copy: {file}")  # not handling everything here
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

# CLI interface
def main():
    parser = argparse.ArgumentParser(description="MineMover - Switch Minecraft mods (CLI version)")
    parser.add_argument("target", nargs="?", help="Name of the folder in Documents\\MineMover to switch to")
    parser.add_argument("--list", action="store_true", help="List available mod folders")

    args = parser.parse_args()

    if not os.path.exists(MINEMOVERT_DIR):
        print(f"❌ MineMover folder not found at:\n{MINEMOVERT_DIR}")
        return

    if args.list:
        folders = get_mod_folders()
        if not folders:
            print("No mod folders found in MineMover.")
            return

        print("Available mod folders:\n")
        for f in folders:
            loader = guess_loader(f)
            print(f" - {f}  [{loader}]")
        return

    if not args.target:
        print("⚠️  No target provided.\nUse --list to see available mod folders.")
        return

    folder = args.target
    print(f"🔄 Trying to switch to: {folder}")

    if switch_mods_to(folder):
        print(f"✅ Switched to: {trim_suffix(folder)}")
        print(f"🔧 Mod loader: {guess_loader(folder)}")
    else:
        print("❌ Something went wrong while switching mods.")

if __name__ == "__main__":
    main()