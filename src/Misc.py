import os, sys

MY_FONT = "NSimSun"

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# run Misc.py directly from working directory ..
def gen_build_command():
    line = "pyinstaller --onefile --windowed --icon=civ.ico"
    for root, dirs, files in os.walk("assets"):
        for filename in files:
            if (filename == "background.png"):
                continue
            line += " --add-data \"assets/icons/" + filename + ";assets/icons/\""
    line += " --add-data \"assets/background/background.png;assets/background/\""
    line += " src/main.py"
    with open('build.bat', 'w', encoding='utf8') as f:
        f.write(line)

if __name__ == "__main__":
    gen_build_command()