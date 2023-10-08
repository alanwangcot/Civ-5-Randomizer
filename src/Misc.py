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
    for root, dirs, files in os.walk("assets/icons"):
        for filename in files:
            if sys.platform.startswith('win'):
                line += " --add-data \"assets/icons/" + filename + ";assets/icons/\""
            else:
                line += " --add-data \"assets/icons/" + filename + ":assets/icons/\""
    for root, dirs, files in os.walk("assets/wonders"):
        for filename in files:
            if sys.platform.startswith('win'):
                line += " --add-data \"assets/wonders/" + filename + ";assets/wonders/\""
            else:
                line += " --add-data \"assets/wonders/" + filename + ":assets/wonders/\""
    if sys.platform.startswith('win'):
        line += " --add-data \"assets/background/background.png;assets/background/\""
    else:
        line += " --add-data \"assets/background/background.png:assets/background/\""
    line += " src/MainWindow.py"
    with open('build.txt', 'w', encoding='utf8') as f:
        f.write(line)


def convert_webp():
    from PIL import Image
    import os

    # Directory containing WebP images
    input_directory = "assets/wonders/"

    # Output directory for converted images
    output_directory = "assets/wonders1/"

    output_format = 'png'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.webp'):
            input_path = os.path.join(input_directory, filename)
            output_filename = os.path.splitext(filename)[0] + '.' + output_format.lower()
            output_path = os.path.join(output_directory, output_filename)

            im = Image.open(input_path)
            im.save(output_path, output_format)

    print("Conversion completed.")


if __name__ == "__main__":
    gen_build_command()
