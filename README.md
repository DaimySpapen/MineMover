# MineMover – Minecraft Mod Folder Switcher

**MineMover** is a small tool that helps you quickly swap between different sets of Minecraft mods. You can use it with a simple GUI or from the command line if you prefer.

---

## 📁 What's in the repo

- `minemover.py` – GUI version (uses `tkinter`)
- `minemover_cli.py` – CLI version
- `minemover.exe` – Windows build (for non-Python users)

---

## 🔧 What it does

- Replaces everything in your `.minecraft\mods` folder with a selected mod pack
- Reads mod folders from `Documents\MineMover`
- Tries to detect the modloader (like Forge, Fabric, etc.) based on folder naming
- Works with or without a GUI
- No extra libraries needed

---

## 🖥️ How to use the GUI

Just run:
```bash
python minemover.py
```

Or double-click `minemover.exe` if you're on Windows and don't want to mess with Python.

You'll see a list of your mod folders — pick one and click “Switch Mods.” That’s it.

---

## 💻 How to use the CLI

List your available mod folders:
```bash
python minemover_cli.py --list
```

Switch to a specific one:
```bash
python minemover_cli.py "1.20.1-create fa"
```

---

## ⚙️ Building a `.exe` (Optional)

If you want to build a standalone Windows app:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed minemover.py
```

---

## 🧩 How folder naming works

MineMover uses suffixes in folder names to detect which modloader it’s for. Here’s what it looks for:

| Suffix | Modloader              |
|--------|------------------------|
| ` fa`  | Fabric                 |
| ` fo`  | Forge                  |
| ` neo` | NeoForge               |
| ` qu`  | Quilt                  |
| ` li`  | LiteLoader             |
| ` ri`  | Rift                   |
| ` rm`  | Risugami's ModLoader  |

Example:  
A folder called `1.20.1-create fa` will show up as “1.20.1-create” and be tagged as Fabric.

---

## ✅ Requirements

- Python 3.6 or newer (only needed if you're not using the `.exe`)

---

## 📄 License

MIT License – do whatever you want with it.

---