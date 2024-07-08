# JBUtils
A macro utility for Roblox Jailbreak, this script is primarily useful for private server owners or users with op privileges. 

It allows you to rapidly obtain a glider or a basic loadout for grinding with a single hotkey press. 

This script also lets you exploit a glitch with the sword item, giving you a significant speed boost by rapidly selecting, deselecting, and using it.

Edit `items_to_give.txt` with your preferred gun setup.

Change your keybinds in main.py, current keybinds:
- F2: Give yourself a glider
- F5: Give out your gun setup
- F8: Stop the train
- F1: Toggle on/off the sword macro

## Prerequisites
- Python 3.6+ on your system

## Usage(Windows, in cmd)
```
git clone https://github.com/DatCodeMania/JBUtils.git
cd JBUtils
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Change your name in .env.example
rename .env.example .env
python main.py
```

## Usage(Linux/Mac)
```
git clone https://github.com/DatCodeMania/JBUtils.git
cd JBUtils
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Change your name in .env.example
mv .env.example .env
python3 main.py
```

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.