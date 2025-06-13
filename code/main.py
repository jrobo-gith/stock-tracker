# Main file that will incorporate all windows and run the GUI

# Run requirements.txt
import sys
import subprocess
req_file = 'requirements.txt'
cmd = [sys.executable, "-m", "pip", "install", "-r", req_file]
subprocess.run(cmd, check=True)

# Import Packages
import json

# Import PyQt5 Packages
from PyQt5.QtWidgets import QMainWindow, QApplication

# Import local files


# Load global settings
with open("partials/glob-settings.json") as f:
    glob_settings = json.load(f)

class MainWindow(QMainWindow):
    """Main class to run everything, takes all other windows and puts them into a stacked widget.
    Note: This is NOT a window itself, it just takes in the other windows and sorts them, loading the main menu first.

    Imports .json file 'global_settings' containing the essential info for the entire window to provide easy access to
    changes if they need to be made.

    'global_settings' includes:
    "font-family":
    "background-color":
    "matrix-color":
    "font-color":
    "screen-height":
    "screen-width":

    Functions:
    - __init__(self):

    Previous versions can be found in the GitHub repository
    https://github.com/jrobo-gith/stock-tracker?tab=readme-ov-file"""

    def __init__(self):
        """Loads each window into a stacked widget to be navigated through"""

        super().__init__()

        self.setWindowTitle("Stock Tracker")
        self.resize(glob_settings['screen-height'], glob_settings['screen-width'])
        self.setStyleSheet(f"background-color:{glob_settings['background-color']};")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


