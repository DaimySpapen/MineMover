# Minemover - A small Minecraft mod switcher application

## How does it work?
You just run the application and it should make a folder named "MineMover" in your Documents folder. If there are no mod folders, it will say that there are no mod folder found.

If you make a folder named something like "1.21.1 Create Neo" it will show as "1.21.1 Create (Neoforge)" in MineMover. Click the name of the folder and select the big green button saying "Switch Mods".

MineMover then deletes the mods that are currently inside your .minectaft/mods folder and puts the mods from "1.21.1 Create Neo" inside of it.

(WARNING: make sure no important mods are inside your mods folder that aren't added with MineMover!!! MineMover does not care about your mods and deletes them.)

## Windows defender blocked the .exe. Windows says...
Yes, it will probally say something like "application comes from an untrusted publisher" or something. I can guarentee that the application doesn't steal your crypto coins, but if you don't trust me you can always build the .exe yourself if you have Python installed.

## How do i build the .exe myself?
- Make sure you have [Python](https://www.python.org/downloads/) and [git](https://git-scm.com/install/windows) installed and added to system path. I only tested it with [Python 3.12](https://www.python.org/downloads/release/python-31210/) but it should work with any still supported Python version.

- Clone this repo by running this in cmd or powershell:
```powershell
git clone https://github.com/DaimySpapen/MineMover.git
```

- Make sure PyInstaller is installed by running this in cmd or powershell:
```powershell
pip install pyinstaller
```

- Then run:
```powershell
pyinstaller --onefile --windowed minemover.py
```

- Check the dist folder in the same folder and there should be a single .exe file there. That's it, just run it and you're good to go.

# Disclaimer
Yes i used AI in the making of this project. I wrote most of the code myself  but had the help of AI in the making of the UI and the CLI script. I also used AI in the old README, which is why i now rewrote it.