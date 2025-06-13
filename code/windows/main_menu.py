# Import packages
import json

# Import PyQt5 stuff
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont

# Import local files

# Load global settings
with open("partials/glob-settings.json") as f:
    glob_settings = json.load(f)

class MainMenuWindow(QWidget):
    """
    Main menu for stock-GUI. Shows a welcome message, along with options on what the user would like to do. These
    options include:
    Stock Browser: browse all item images and descriptions check if something is checked for re-stock,

    Shopping List: List of all items needed for stock, can add or remove items manually and can act as a general
    shopping list as well. This list will be emailed to the user at the end of the week for shopping,

    Add/Remove Item: Add a new item or remove an existing item from the stock.

    Instructions: Short list of instructions on how to use this GUI.

    Functions:
    -__init__(self, main_stacked_widget)

    Previous versions can be found in the GitHub repository
    https://github.com/jrobo-gith/stock-tracker?tab=readme-ov-file
    """

    def __init__(self, main_stacked_widget):
        """
        Initialises the main menu window.
        """
        super().__init__()
        self.main_stacked_widget = main_stacked_widget

        # Create page container
        self.page_container = QVBoxLayout()

        # Add Navbar and menu instances
        self.title = QLabel("Main Menu")
        self.menu = QVBoxLayout()
        self.page_container.addWidget(self.title, stretch=1)
        self.page_container.addLayout(self.menu, stretch=19)
        self.title.setAlignment(Qt.AlignCenter)
        self.menu.setAlignment(Qt.AlignCenter)
        self.setLayout(self.page_container)

        # Set title details
        self.title.setStyleSheet(f"""background-color: {glob_settings['background-color']};
                                 color: {glob_settings['font-color']}""")
        self.title.setFont(QFont(glob_settings['font-family'], glob_settings['font-size']))

        # Set Menu details


